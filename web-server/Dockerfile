# Version de python que correra en el contenedor.
FROM python:3.13.12

# Crear el directorio de trabajo dentro del contenedor.
WORKDIR /web-server

# Instalar las dependencias del proyecto.
# izquierda local, derecha contenedor
COPY requirements.txt /web-server/requirements.txt

# Instalar las dependencias del proyecto eb el contenedor.
RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt

# copiar el contenido del proyecto al contenedor.
COPY . /web-server

# Comando que se ejecutara al iniciar el contenedor, y lo mantendra operando.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]