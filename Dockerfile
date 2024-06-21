# Utiliser l'image officielle Python comme parent
FROM python:3.8

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers de dépendances et installer les packages
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Installer mysql pour avoir accès au dbshell
RUN apt update
RUN apt install -y default-mysql-client

# Copier le reste des fichiers du projet dans le conteneur
COPY . .

# Exposer le port sur lequel Django sera accessible
EXPOSE 8000

# Commande pour démarrer l'application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
