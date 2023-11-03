# Use a imagem base do Python
FROM python:3.8

# Define o diretório de trabalho
WORKDIR /app

# Copie os arquivos de código fonte para o contêiner
COPY . /app

# Instale as dependências do aplicativo
RUN pip install -r requirements.txt

# Expõe a porta em que a aplicação estará em execução
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
