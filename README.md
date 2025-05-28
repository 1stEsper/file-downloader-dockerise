# file-downloader-dockerise

Application Flask simple permettant de lister et télécharger des files via une interface web ou une API. 
Le tout est conteneurisé par Docker.

## Fonctionnalités

- Interface HTML listant les fichiers disponibles dans un volume "/data"
- API JSON listant les fichiers
- Route de téléchargement pour chaque fichier
- Test automatiques avec "pytest"

## Installation locale 

python -m venv venv
venv\Scripts\activate #Windows
pip install -r requirements.txt
python run.py

