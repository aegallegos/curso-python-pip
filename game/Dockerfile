# Version de python que correra en el contenedor.
FROM python:3.13.12

# Crear el directorio de trabajo dentro del contenedor.
WORKDIR /game

# Instalar las dependencias del proyecto.
# izquierda local, derecha contenedor
COPY requirements.txt /game/requirements.txt

# Instalar las dependencias del proyecto eb el contenedor.
RUN pip install --no-cache-dir --upgrade -r /game/requirements.txt

# copiar el contenido del proyecto al contenedor.
COPY . /game

# Comando que se ejecutara al iniciar el contenedor, y lo mantendra operando.
CMD bash -c "while true; do sleep 1; done;"