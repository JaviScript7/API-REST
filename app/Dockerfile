#Elegimos la imagen base y especiicamos la version
FROM python:3.8

#Indicamos quien es el responsable de mantener el contenedor
LABEL Maintainer = "JaviScript"

#Creamos el directorio de la aplicacion
RUN mkdir -p /home/app

#Copiar los archivos de la aplicacion
COPY *.py /home/app
COPY requirements.txt /home/app

#Establecemos el espacion de trabajo
WORKDIR /home/app

#Exponemos el puerto en este caso para Flkas
EXPOSE 5000

#Instalar las dependencias
RUN pip install --no-cache-dir -r /home/app/requirements.txt 

#CMD ["python","/home/app/categoria.py"]
#Ejecutar la aplicacion Flask usando Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "categoria:app"]