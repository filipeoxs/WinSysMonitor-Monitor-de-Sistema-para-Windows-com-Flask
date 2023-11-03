from flask import Flask, render_template
from collect_system_info import collect_system_info
from collect_users_info import collect_users_info

app = Flask(__name__)

@app.route('/usuarios_info')
def usuarios_info():
    # Lógica para coletar informações sobre o uso de CPU e memória de cada usuário
    return render_template('usuarios.html', info_usuarios=collect_users_info())

@app.route('/')
def index():
    cpu_percent, memoria_info, disco_info = collect_system_info()

    # Crie uma lista de pares (core, percent) a partir da lista de percentuais da CPU
    cpu_percent_pairs = [(core, percent) for core, percent in enumerate(cpu_percent)]

    return render_template('index.html', cpu_percent_pairs=cpu_percent_pairs, memoria_info=memoria_info, disco_info=disco_info)

if __name__ == '__main__':
    app.run(debug=True)
