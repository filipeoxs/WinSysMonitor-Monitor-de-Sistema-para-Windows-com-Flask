import psutil
from collections import defaultdict
import json

def collect_users_info():
    processos_por_usuario = defaultdict(list)
    
    for processo in psutil.process_iter(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_info']):
        try:
            info = processo.info
            usuario = info['username']
            
            if usuario and usuario != "NT AUTHORITY\\SYSTEM":
                processo_por_usuario = {
                    'pid': info['pid'],
                    'nome': info['name'],
                    'cpu_percent': round(info['cpu_percent'], 2),
                    'memoria_gb': round(info['memory_info'].rss / (1024 ** 3), 2)  # Memória em GB
                }
                processos_por_usuario[usuario].append(processo_por_usuario)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    uso_cpu_memoria_por_usuario = {}
    for usuario, processos in processos_por_usuario.items():
        uso_cpu = sum(processo['cpu_percent'] for processo in processos)
        uso_memoria = sum(processo['memoria_gb'] for processo in processos)
        uso_cpu_memoria_por_usuario[usuario] = {
            'cpu_percent': round(uso_cpu, 2),
            'memoria_gb': round(uso_memoria, 2)
        }
    save_to_json(uso_cpu_memoria_por_usuario)
    return uso_cpu_memoria_por_usuario

def save_to_json(file):
    # Salve os dados em um arquivo JSON
    with open(f'usuarios_info.json', 'w') as arquivo_json:
        json.dump(file, arquivo_json)