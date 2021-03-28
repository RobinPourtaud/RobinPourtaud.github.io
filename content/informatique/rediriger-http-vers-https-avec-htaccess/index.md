---
title: "Rediriger le trafic HTTP vers HTTPS avec .htaccess."
slug: "rediriger-http-vers-https-avec-htaccess"
date: "2020-06-04"
categories: 
  - "informatique"
tags: 
  - "apache2"
  - "htaccess"
  
  - "wordpress"
description: ".htaccess est un fichier de configuration utilisé par Apache2 permettant de paramétrer le comportement du serveur HTTP dans un dossier précis. Ainsi, sans toucher aux fichiers de configuration du serveur HTTP directement, on pourra facilement réécrire l'URL afin de permettre la redirection du trafic HTTP vers HTTPS."
---
_Ce tutoriel **n'est donc pas** à destination des utilisateurs de serveur Nginx._

## Accéder au fichier

### Manuellement

Un fichier .htaccess peut se situer dans n'importe quel dossier de votre site web. Si vous souhaitez appliquer la redirection à tout le site, je vous conseille donc de modifier celui positionné à la **racine de votre site.**

Vous pouvez bien-sûr le faire via FTP/SSH manuellement.

_Attention ! Si vous ne le trouvez pas, il est possible que **le fichier soit caché** ! Un fichier commençant par un point sous linux est un fichier caché._

S'il n'existe pas, créez-le !

### Sur Wordpress : Via une extension

Certaines extensions permettent la modification de .htaccess directement depuis l'interface d'administration de votre wordpress. Par exemple : Rank Math SEO le permet dans "Réglages généraux" -> "Modifier le .htaccess".

## Modifier le fichier

Je vous propose d'ajouter ces lignes de codes dans votre fichier .htaccess :

```
RewriteEngine On
RewriteCond %{HTTPS} off
RewriteRule (.*) https://%{HTTP_HOST}%{REQUEST_URI} [R=301,L]
```

Pour paraphraser ce code :  
La ligne 1 : permet d'activer la réécriture d'URL ([En savoir plus](https://httpd.apache.org/docs/2.4/fr/mod/mod_rewrite.html)).  
La ligne 2 : si la requête ne se sert pas de HTTPS alors :  
La ligne 3 : pour n'importe quelle requête (le regex de début), on redirige de façon permanente ([R=301](https://httpd.apache.org/docs/2.4/fr/rewrite/flags.html)) l'URL vers une URL utilisant le protocole HTTPS. "L" est un drapeau permettant de stopper le processus de réécriture.

Pour plus de redirections, veuillez vous référer à [un article de Mozilla](https://developer.mozilla.org/fr/docs/Web/HTTP/Redirections).

Une alternative à "RewriteCond %{HTTPS} off" est :

```
RewriteCond %{SERVER_PORT} 80
```

Le port de HTTP étant par défaut le 80, celui du HTTPS le 443.

## Sources :

1. [RedirectSSL Apache2](https://cwiki.apache.org/confluence/display/HTTPD/RedirectSSL)
2. [HTTP to HTTPS redirect not working with .htaccess - Stack Overflow](https://stackoverflow.com/questions/51352344/http-to-https-redirect-not-working-with-htaccess)
3. [Multiple RewriteConditions: How to chain them before a set of rules? - Stack Overflow](https://stackoverflow.com/questions/5305987/multiple-rewriteconditions-how-to-chain-them-before-a-set-of-rules)
4. [.htaccess - Wikipédia](https://fr.wikipedia.org/wiki/.htaccess)
