---
title: "1 site web, 2 domaines dont 1 référencé (avec robots.txt et .htaccess)"
slug: "1-site-web-2-domaines-1-domaine-reference-avec-robots-txt-et-htaccess"
date: "2020-06-14"
categories: 
  - "informatique"
tags: 
  - "apache2"
  - "htaccess"
  - "robots-txt"
  
  - "wordpress"
description: "Au cours de la création de notre site DevMath.fr, nous avons souhaité créer un sous-domaine afin de faciliter notre gestionp du site web. Ce sous-domaine utilisait les mêmes fichiers que notre site web principal, mais nen devait pas être référencé sur les moteurs de recherches ! Nous avons vite rencontré un problème en raison de l'unicité du fichier robots.txt. Ce tutoriel a pour but de vous montrer sa résolution."
---
Nb : Ce tutoriel nécessite un fichier .htaccess, il sera donc à destination des utilisateurs de Apache2 et non de Nginx.

## Modification et création de robots.txt

Un fichier robots.txt est un fichier utilisé par de nombreux moteurs de recherche afin d'indiquer si un site (ou une page / un document) doit être référencé ou non.

Pour ce tutoriel, prenons 2 site web : "_site.com_" et "_no-ref.site.com_". Comme leurs noms le suggèrent, on souhaite que le site "_site.com_" soit le seul à être référencé sur [Google, Bing, etc.](http://robots-txt.com/ressources/)

Par défaut, sans robots.txt, le moteur de recherche référencera votre site web s'il est accessible et respecte ses standards. C'est pourquoi, nous ne créerons pas de robots.txt pour "_site.com_".

A la racine de votre site, créez un fichier .txt avec le nom de votre choix, pour ma part : _robots2.txt_.

```
User-agent: *
Disallow: / 
```

[Pour en savoir plus](http://robots-txt.com/ressources/robots-txt-disallow-all/)

_robots2.txt_ ne sera pas traité par les moteurs de recherche, ils analysent uniquement les fichiers _robots.txt_.  
Il sera alors nécessaire, pour le domaine "_no-ref.site.com_" uniquement, de faire passer le fichier _robots2.txt_ comme un fichier _robots.txt_. C'est là qu'entre en jeu le fichier _.htaccess_.

## Configuration du .htaccess

Un fichier _.htaccess_ est un fichier de configuration Apache2. Il permet de paramétrer le serveur HTTP depuis un dossier spécifique. Nous allons nous en servir pour permettre aux moteurs de recherche d'accéder au contenu de robots2.txt depuis no-ref.site.com/robots.txt. Pour cela :

```
RewriteEngine on
RewriteCond %{HTTP_HOST} ^no-ref\.site\.com$
RewriteRule ^robots\.txt$ robots2.txt [L]
```

Littéralement, une requête à destination de no-ref.site.com/robots.txt renverra le contenu de robots2.txt.

Les moteurs de recherches (principaux) ne référenceront donc pas votre deuxième domaine !
