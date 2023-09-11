# Utilisez une image de base Python
FROM python:3.8

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt .

# Installez les dépendances
RUN pip install -r requirements.txt

# Copiez tout le contenu du répertoire actuel dans le conteneur
COPY . .

# Copier les fichiers médias dans l'image Docker
COPY images /DzPiecesStore/images

# Exposez le port sur lequel votre application Django écoute (par défaut : 8000)
EXPOSE 8000

# Commande pour exécuter votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
