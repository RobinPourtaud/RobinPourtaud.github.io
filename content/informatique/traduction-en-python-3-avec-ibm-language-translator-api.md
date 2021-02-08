---
title: "Traduction en Python 3 avec IBM Language Translator API"
slug: "traduction-en-python-3-avec-ibm-language-translator-api"
date: "2020-07-05"
categories: 
  - "informatique"
tags: 
  - "ibm-language-translator"
  - "jupyter-notebook"
  - "python"
  - "traduction"
description: "Pour traduire du texte en Python, on pense à Google Traduction API. Cependant, il existe de nombreuses alternatives. Parmi celles-ci se trouve Language Translator API, qui propose de traduire gratuitement 1 000 000 de caractères par mois. Cet article vous aidera a le paramétrer et l'utiliser."
---

## Nécessaire

1. Un compte IBM Cloud (gratuit). Pour se connecter ou s'inscrire, c'est ici : [IBM Cloud](https://cloud.ibm.com/login).
2. Avoir installé Python et pip sur votre ordinateur. Une alternative est l'utilisation de [Jupyter Notebook](https://colab.research.google.com/).

## Obtenir la clé de l'API

Une fois connecté à IBM cloud, vous pouvez maintenant ajouter le service Language Translator :

[Language Translator - IBM Cloud](https://cloud.ibm.com/catalog/services/language-translator)

Sélectionnez le "plan lite" :

![](images/image-12-1024x243.png)

Plan lite

Une fois créé, dans l'onglet _Manage_, copiez l'API key et l'URL. Ils seront tous deux nécessaires pour la suite.

![](images/image-14-1024x407.png)

Language Translator API

## Installation de la librairie ibm_watson

Pour installer ibm_watson depuis le terminal, exécutez la commande suivante :

```
sudo pip install ibm_watson
```

Sinon depuis Jupyter Notebook :

```
!pip install ibm_watson
```

## Paramétrage de l'API

Premièrement, importez _LanguageTranslatorV3_ et _IAMAuthenticator_.

```
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
```

Vous pouvez entrer vos informations précédemment copiées comme ceci :

```
key = '***'
url = '***'
version = '2018-05-01'
```

Enfin :

```
Translator = LanguageTranslatorV3(version=version,authenticator=IAMAuthenticator(key))
Translator.set_service_url(url)
```

## Utilisation de l'API

Je vous propose de traduire "Ceci est une phrase très utile" en Anglais. C'est donc une traduction de français vers l'anglais.

```
Translator.translate(text="Ceci est une phrase très utile", model_id='fr-en').get_result()
```

Si vous avez suivi ce tutoriel comme prévu, vous devriez obtenir :

![](images/image-15-1024x115.png)

Traduction du français vers l'anglais

Pour donner un autre exemple : changer le paramètre "model_id='fr-en'" par "mode_id='fr-es'" permettrait donc de traduire cette phrase en espagnol.

## Alternative à IBM translate ?

Il est possible de traduire gratuitement du texte avec Google Traduction en Python. Pour cela, rien de plus simple :

[Traduire un string grâce à Google Traduction en Python](https://keskec.fr/sciences/informatique/robin/1933/)

## Source

1. [Language Translator IBM Python](https://cloud.ibm.com/apidocs/language-translator?code=python)
