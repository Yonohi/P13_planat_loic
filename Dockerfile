# Plus d'info: https://hub.docker.com/_/python
# Donne des détail sur les variants -slim, -alpine, -windowsservercore
# Pour des détail sur l'écriture du Dockerfile:
# https://www.pythoniste.fr/python/fastapi/deployer-une-application-python-avec-docker/
# Remarque : une image django n'est apparemment pas souhaitable,
# on nous conseille de faire usage de python
FROM python:3.8

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY requirements.txt .
# On pourrait rajouter '&& rm requirements.txt' pour supprimer le fichier
RUN pip install -r requirements.txt
COPY . .
# Remarque: si on met EXPOSE 8000, on ne peut apparemment pas accéder au port
# de l'extérieur, il n'est pas 'publié', il faudra donc utiliser dans notre
# commande docker l'argument -p <host_port>:<container_port>
CMD python3 .manage.py runserver 8000