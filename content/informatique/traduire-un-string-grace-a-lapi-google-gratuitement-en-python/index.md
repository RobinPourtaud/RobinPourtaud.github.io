---
title: "Traduire un string grâce à Google Traduction en Python (for free)"
slug: "traduire-un-string-grace-a-lapi-google-gratuitement-en-python"
date: "2020-05-12"
categories: 
  - "informatique"
tags: 
  - "google-traduction"
  - "jupyter-notebook"
  - "python"
  
description: "Traduire du texte est quelque chose de complexe, demandant beaucoup de données et de ressources. C'est pourquoi, il n'est pas possible (difficile) de programmer soit même un algorithme performant de traduction."
---
La méthode la plus simple est encore de se relayer sur la puissance de Google. Google, ou plutôt Google Cloud propose un API, l'API **Google Cloud Translation**. Cet API, bien que très pratique, pose un certain problème, celui du **prix** : [20$ pour 1 million de caractères](https://cloud.google.com/translate/pricing). Bien que plutôt rentable pour de nombreux projets, si, comme moi, vous n'avez pas besoin d'utiliser autant de caractères, il serait intéressant de trouver une alternative **gratuite**. Et c'est pour cela que je vous propose cet article !

Pour ce tutoriel, j'utiliserai [Colab Research](https://colab.research.google.com/), le Jupyter Notebook de Google.

## Nécessaire :

Pour suivre ce tutoriel vous avez 2 possibilités :

- Vous utilisez un Jupyter Notebook en ligne tel que celui de [Google](https://colab.research.google.com/) ou de [Microsoft](https://notebooks.azure.com/), qui proposent une solution rapide et pré-configurée.
- Ou, un ordinateur avec **python** et **pip** correctement installé.

## Installation de la bibliothèque :

Pour ce projet, on va utiliser la bibliothèque (library) "googletrans". Trouvable [ici](https://pypi.org/project/googletrans/).

(si vous utilisez votre terminal) Pour l'installer, utilisez la formule magique habituelle :

```bash
sudo pip install googletrans
```

Si vous voulez l'installer depuis Jupyter Notebook :

```bash
!pip install -q googletrans
```

## Utilisation de googletrans :

Je vous propose un code tout simple qui traduit le mot "hello world" en "bonjour le monde" :

```python
from googletrans import Translator

tr = Translator()
output = tr.translate('hello world',src='en',dest='fr').text

print(output)
```

Comme on peut s'en douter, print(output) retourne bien "bonjour le monde".

Mais googletrans permet des choses plus folles ! Il permet de detecter automatiquement la langue !

```python
from googletrans import Translator

tr = Translator()
output = tr.translate('Chaton').text

print(output)
```

Ce code affichera donc "Kitten", étant donné que 'dest' est par défaut égal à 'eng'.

## Sources :

- [https://pypi.org/project/googletrans/](https://pypi.org/project/googletrans/)
- [https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb](https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb)
- [https://notebooks.azure.com/help/jupyter-notebooks/package-installation](https://notebooks.azure.com/help/jupyter-notebooks/package-installation)
