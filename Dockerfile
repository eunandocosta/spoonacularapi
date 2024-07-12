# Use uma imagem base oficial do Python
FROM python:3.10-slim

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos requirements.txt para o contêiner
COPY requirements.txt .

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copie o conteúdo do diretório atual para o diretório de trabalho do contêiner
COPY . .

# Defina a variável de ambiente para o Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Exponha a porta em que a aplicação Flask estará escutando
EXPOSE 5000

# Comando para rodar a aplicação Flask
CMD ["flask", "run"]
