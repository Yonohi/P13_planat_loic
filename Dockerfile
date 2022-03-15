# Plus d'info: https://hub.docker.com/_/python
# Donne des détail sur les variants -slim, -alpine, -windowsservercore
# Remarque : une image django n'est apparemment pas souhaitable,
# on nous conseille de faire usage de python
FROM python:3.8
COPY requirements.txt
# On pourrait rajouter '&& rm requirements.txt' pour supprimer le fichier
RUN pip install -r requirements.txt
COPY ..
CMD python3 manage.py runserver