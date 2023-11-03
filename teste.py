import psutil

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

    return cpu_percent, memoria_info, disco_info

cpu_percent, memoria_info, disco_info = collect_system_info()

print("Consumo de CPU por núcleo:")
for i, percent in enumerate(cpu_percent):
    print(f"Núcleo {i}: {percent}%")

print("\nInformações de Memória:")
print(f"Total: {memoria_info['total']} GB")
print(f"Disponível: {memoria_info['disponivel']} GB")
print(f"Usada: {memoria_info['usada']} GB")
print(f"Porcentagem de uso: {memoria_info['porcentagem']}%")

print("\nInformações de Disco:")
print(f"Total: {disco_info['total']} GB")
print(f"Disponível: {disco_info['disponivel']} GB")
print(f"Usado: {disco_info['usado']} GB")
print(f"Porcentagem de uso: {disco_info['porcentagem']}%")
