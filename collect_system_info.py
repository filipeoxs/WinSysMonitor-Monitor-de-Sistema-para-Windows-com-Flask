import psutil
import json

def collect_system_info():
    # Coleta informações de CPU
    cpu_percent = psutil.cpu_percent(interval=1, percpu=True)

    # Coleta informações de memória
    memoria = psutil.virtual_memory()
    memoria_info = {
        'total': round(memoria.total / (1024 ** 3), 2),  # Memória total em GB
        'disponivel': round(memoria.available / (1024 ** 3), 2),  # Memória disponível em GB
        'usada': round(memoria.used / (1024 ** 3), 2),  # Memória usada em GB
        'porcentagem': memoria.percent  # Porcentagem de uso de memória
    }

    # Coleta informações do espaço em disco
    disco = psutil.disk_usage('/')
    disco_info = {
        'total': round(disco.total / (1024 ** 3), 2),  # Espaço total em disco em GB
        'disponivel': round(disco.free / (1024 ** 3), 2),  # Espaço disponível em disco em GB
        'usado': round(disco.used / (1024 ** 3), 2),  # Espaço usado em disco em GB
        'porcentagem': disco.percent  # Porcentagem de uso do disco
    }
    # Crie um dicionário que contém todas as informações
    system_info = {
        'CPU_percent': cpu_percent,
        'Memoria_info': memoria_info,
        'Disco_info': disco_info
    }
    save_to_json(system_info)
    return cpu_percent, memoria_info, disco_info

def save_to_json(file):
    # Salve os dados em um arquivo JSON
    with open(f'system_info.json', 'w') as arquivo_json:
        json.dump(file, arquivo_json)