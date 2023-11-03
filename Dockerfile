# Use a imagem base do Windows com suporte ao Python
FROM python:3.8-windowsservercore-ltsc2019

# Defina o diretório de trabalho no contêiner
WORKDIR C:\app

# Copie os arquivos do seu aplicativo para o contêiner
COPY . .

# Instale as dependências do aplicativo (se houver)
RUN pip install -r requirements.txt

# Comando a ser executado quando o contêiner for iniciado
CMD ["python", "app.py"]
