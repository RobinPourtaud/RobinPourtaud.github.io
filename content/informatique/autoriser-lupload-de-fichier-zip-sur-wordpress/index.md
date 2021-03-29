---
title: "Autoriser l'upload de fichiers non-autorisés sur Wordpress"
slug: "autoriser-lupload-de-fichier-zip-sur-wordpress"
date: "2020-06-03"
categories: 
  - "informatique"
tags: 
  
  - "wordpress"
  - "zip"

latex: false
description: "Désolé, ce type de fichier n’est pas autorisé pour des raisons de sécurité. J'ai repoussé à de nombreuses reprises sa résolution pensant que c'était une opération complexe. Finalement, en moins de 5 min, c'était résolu et c'est ce que je vais vous montrer dès maintenant ! "
---

Je traiterai l'upload de fichiers zip en particulier.

## Résolution manuelle :

### Accéder au fichier function.php :

Le fichier "function.php" est censé se situer dans le dossier du thème de votre site web. Accedez-y via SFTP, SSH ou de la façon de votre choix.

### Modifier function.php

Pour comprendre la fonction ci-dessous, il faut savoir ce qu'est un type Mime :

Un type de média, ou type MIME est un identifiant de format de données composé de 2 parties, appelées type, et sous-types.

Dans notre cas, notre type MIME est "application/zip", mais il en existe pleins d'autres :

- **application/pdf** pour le format pdf
- **application/msword** pour le format .doc de Microsoft Word
- **image/gif** pour les images GIF
- **text/css** pour le CSS

Pour en voir plus : [Type Mimes - Wikipédia](https://fr.wikipedia.org/wiki/Type_de_m%C3%A9dias)

Pour ajouter les fichiers "zip", ajoutez-y ces lignes entre les balises php.

```php
function zip_up($mimes=array()) { 
   $mimes['zip'] = 'application/zip';
   return $mimes;
}
add_filter('upload_mimes', 'zip_up');
```

N'oubliez pas d'enregistrer !

_Nb : Vous pouvez bien sûr ajouter autant d'extensions que vous souhaitez..._

### Optionnel : désactiver totalement le filtrage

Pour autoriser l'upload de n'importe quel fichier, il suffit d'ajouter la ligne suivante au fichier wp-config.php à la racine de votre site web.

```php
define('ALLOW_UNFILTERED_UPLOADS', true);
```

## Alternative : Utiliser une extension

J'utilise personnellement l'extension : [WP add Mimes Types](https://fr.wordpress.org/plugins/wp-add-mime-types/) par [Kimiya Kitani](http://kitaney-wordpress.blogspot.jp/)

Une fois installée, vous la trouverez sous "Réglage" puis "Mime types settings".

Vous y trouverez également une liste d'extension autorisé sous "List of allowed mime types and file extensions by WordPress".

![Add Values - WP add Mimes Types](image-3-1024x519.png#t4)


Ajoutez-y cette ligne et enregistrez.
