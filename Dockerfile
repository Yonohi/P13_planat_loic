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
# Remarque: EXPOSE 8000 n'a pas l'air obligatoire avec les commandes que l'on utilise,
# cela précise sur quel port il y a écoute mais le port n'est pas publié,
# il faudra donc utiliser  l'argument -p <host_port>:<container_port>
EXPOSE 8000
# 0.0.0.0 signifie « toutes les adresses IPv4 de la machine locale »
# 2 choix:
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python3 manage.py runserver 0.0.0.0:8000