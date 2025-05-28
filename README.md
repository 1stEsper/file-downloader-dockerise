# file-downloader-dockerise

Application Flask simple permettant de lister et télécharger des files via une interface web ou une API. 
Le tout est conteneurisé par Docker.

## Fonctionnalités

- Interface HTML listant les fichiers disponibles dans un volume "/data"
- API JSON listant les fichiers
- Route de téléchargement pour chaque fichier
- Test automatiques avec **"pytest"**

## Installation locale 

'''bash
> python -m venv venv
> venv\Scripts\activate #Windows
> pip install -r requirements.txt
> python run.py



## Lancement avec Docker 

1. Construire l'image

> docker build -t file-downloader .

2. Lancer le contener

> docker run -v ${PWD}\data:/data -p 5000:5000 file-downloader

## Endpoints 

| Méthode | URL                         | Description                    |
| ------- | ---------------------       | ------------------------------ |
| GET     | `/`                         | Page HTML listant les fichiers |
| GET     | `/api/files`                | Renvoie la liste en JSON       |
| GET     | `/download/<path:filename>` | Télécharge le fichier spécifié |


## Lancer les test

> pytest tests/

## Structure de projet

file-downloader-dockerise/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── templates/
│       └── index.html
├── tests/
│   └── test_routes.py
├── data/
│   └── test.txt
├── run.py
├── requirements.txt
├── Dockerfile
└── README.md
