---
title: "Héberger un Wordpress Gratuitement sur un Raspberry Pi"
slug: "keske-cest-heberger-un-wordpress-gratuitement-sur-un-raspberry-pi"
date: "2020-04-23"
categories: 
  - "informatique"
tags: 
  - "apache2"
  - "mysql"
  - "php"
  - "raspberry-pi"
  - "raspbian"
  - "server-http"
  - "tuto"
  - "wordpress"
description: "WordPress est un système de gestion de contenu (SGC ou content management system (CMS) en anglais) gratuit, libre et open-source."
---
Wordpress est le CMS le plus utilisé au monde. De part sa simplicité d'utilisation et sa liberté de design, sa popularité s’explique d'elle même.

Malheureusement, utiliser Wordpress pour laisser libre cours à son imagination revient souvent à passer par son porte monnaie.

Pour un site personnel, 4€ par mois reste raisonnable, mais pour un site d'e-Commerce, 45€ semble moins attrayant....

![](image-1024x423.png)

Tarifs avril 2020

Il serait donc intéressent de pouvoir profiter de WordPress gratuitement, et ce sans être limité par les blocages du modèle "gratuit".

Héberger soit même, son site WordPress semble donc être la bonne chose à faire.

## Le nécessaire:

- Un ordinateur sous Linux (dans mon cas, j'utiliserais un raspberry Pi 3b sous raspbian). Il faut prendre en compte que cet ordinateur devra rester allumé en permanence...
- Une connexion rapide est préférée (pas nécessaire).
- Un nom de domaine (potentiellement payant).
- Une bonne heure :).

## Installer un Serveur HTTP

Avant tout, vérifiez que votre ordinateur est bien à jour:

```
sudo apt update
sudo apt upgrade
```

Pour pouvoir envoyer des pages web aux utilisateurs, nous avons besoin pour cela d'un serveur HTTP. Il existe Nginx, mais pour ma part, je vais utiliser Apache2.

```
sudo apt install apache2
```

```
sudo service apache2 start
```

Maintenant, vous devriez pouvoir accéder à l'adresse http://localhost sur votre ordinateur et voir ce magnifique message:

![](image-1-1024x535.png)

Apache2 Debian Default Page

> Bien sûr, vous pouvez paramétrer votre serveur à distance via SSH. Dans ce cas, veuillez taper son IP local à la place de localhost...
> 
> Petite info

## Installer PHP/MySQL

Wordpress est un programme développé en PHP, il est donc nécessaire d'installer PHP7. Wordpress utilise une base de données MySQL, nous devons donc l'installer également.

```
sudo apt install php mysql
wget https://dev.mysql.com/get/mysql-apt-config_0.8.13-1_all.deb
sudo dpkg -i mysql-apt-config_0.8.13-1_all.deb
```

![](image-2-1024x592.png)

Configure Mysql-apt-config

Appuyez sur "Ok"

```
sudo apt update
sudo apt install mysql-server
```

Si vous souhaitez avoir la dernière version de PHP, je vous conseille de suivre le tutoriel ci-dessous:

[Installer PHP7.3 pour Wordpress](https://keskec.fr/sciences/informatique/robin/786/)

## Configurer Mysql

Il faut maintenant configurer Mysql pour ajouter une base de données vide et un utilisateur avec mot de passe.

Pour cela, tapez:

```
sudo mysql -u root -p
```

Vous devriez maintenant voir ceci :

![](image-9-1024x281.png)

Ensuite, créez une nouvelle base de donnée :

```
CREATE DATABASE exempleDB;
```

Créez un nouvel utilisateur :

```
CREATE USER 'exempleUtilisateur' IDENTIFIED BY 'exempleMDP';
```

Et maintenant, donnez la permission à votre utilisateur de modifier à volonté exempleDB :

```
GRANT USAGE ON 'exempleDB'.* TO 'exempleUtilisateur'@localhost IDENTIFIED BY 'exempleMDP';
```

Et enfin, afin de rendre ces nouveaux privilèges effectifs :

```
FLUSH PRIVILEGES;
```

Fini le SQL pour ce tuto :). (exit pour quitter).

## Ouvrir le port HTTP et HTTPS du Router Internet

Pour rendre accessible votre serveur WEB sur internet, vous devez autoriser les connexions entrantes et sortantes sur le port HTTPS, par défaut le port 443.

Ce paramètrage est accessible sous l'onglet "Gestion des ports" sur les Freeboxs, ou sur un onglet "Virtual server" sur un Router Tp-link. Il existe un nombre important d'interfaces différentes. C'est pourquoi je ne peux vous montrer le moyen d’ouvrir les ports sur tous les router internet.

L'idée générale consiste à trouver ce menu, rajouter une redirection, et de la remplir ainsi :

![](image-5.png)

Redirection de port: Freebox

Faites de même avec le HTTP (port 80) si vous le souhaitez.

## Configurer un nom de Domaine

Votre site web est maintenant accessible sur internet, mais uniquement depuis une adresse IP. Si vous voulez donner accès à votre site aux utilisateurs grâce à une adresse du type www.votre-site.com, vous devez posséder un nom de domaine. Pour cela, vous pouvez acheter un nom de domaine. Par exemple sur le site Google Domain. (il existe aussi des sous-domaines gratuit, comme ceux que propose Azote: [https://www.azote.org/](https://www.azote.org/)).

[https://domains.google.com/](https://domains.google.com/)

Une fois votre domaine acheté, vous devrez configurer vos règles de type A.

Dans l'onglet DNS, vous pouvez rajouter cette règle, c'est ici que vous configurer les sous-domaines éventuels de votre site.

![](image-7-1024x307.png)

## Installer un Certificat SSL gratuit pour HTTPS

Optionnel: Si vous souhaitez avoir plusieurs sous-domaines, il est préférable de configurer proprement Apache2.

La façon d'avoir un certificat gratuit le plus facilement est d'utiliser l'outil Certbot, il vous délivrera et configurera seul le certificat SSL. Pour cela, ajoutez le PPA de certbot :

```
sudo apt-get update
sudo apt-get install software-properties-common
sudo add-apt-repository universe
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
```

Et installez-le :

```
sudo apt-get install certbot python-certbot-apache
```

Une fois installé, vous pouvez maintenant l’exécuter :

```
sudo certbot
```

Vous devriez maintenant recevoir la question suivante :

![](image-8-1024x408.png)

Ensuite, acceptez la redirection. Apache doit maintenant redémarrer et vous pourrez (normalement) voir la page Apache s’afficher à l’adresse : https://votre-site.com

## Télécharger et Installer Wordpress

Veuillez prendre en compte qu'il aurait été préférable de pré-paramétrer son Wordpress en local, mais pour simplifier ce tutoriel, je vais vous montrer comment directement avoir un Wordpress accessible depuis le nom de domaine.

Positionnez-vous dans le dossier /var/www/

```
cd /var/www
```

Téléchargez l'archive avec la commande :

```
wget https://wordpress.org/latest.zip
```

Ensuite, extrayez l'archive :

```
unzip latest.zip
```

Un nouveau dossier nommé "Wordpress" est apparu dans le dossier courant. Vous devez maintenant indiquer à Apache2 de regarder dans ce dossier :

```
sudo nano /etc/apache2/sites-available/000-default-le-ssl.conf
```

Ensuite, indiquez la localisation du dossier comme ceci :

```
<IfModule mod_ssl.c>
<VirtualHost *:443>
        ServerName NOMDUSITE.COM
        ServerAdmin NOMADMIN
        Documentroot /var/www/wordpress
        RewriteEngine on
        <Directory "/var/www/wordpress">
                AllowOverride All
                Allow from All
        </Directory>
Include /etc/letsencrypt/options-ssl-apache.conf
SSLCertificateFile /etc/letsencrypt/live/NOMDUSITE.COM/fullchain.pem
SSLCertificateKeyFile /etc/letsencrypt/live/NOMDUSITE.COM/privkey.pem
</VirtualHost>
```

Configuration de Apache2 basique, suffisante pour que le site fonctionne mais des modifications seront peut-être nécessaires en fonction de ce que vous ferez du site.

Redémarrez Apache2 :

```
sudo service apache2 restart
```

## Configuration basique de Wordpress

Rendez-vous sur votre site : https://NOMDUSITE.COM

Appuyez sur "C'est parti !"

Et pour finir, rentrez toutes les informations comme ceci :

- Nom de la base de données : exempleDB
- Identifiant: exempleUtilisateur
- Mot de passe: exempleMotdepasse
- Adresse de la base de données: localhost
- Préfixe des tables: wp_

Et voilà, tout doit maintenant marcher pour le mieux :). Amusez-vous bien avec votre nouveau site Wordpress.

## Sources:

- [https://certbot.eff.org/lets-encrypt/ubuntubionic-apache](https://certbot.eff.org/lets-encrypt/ubuntubionic-apache)
- [https://www.azote.org/](https://www.azote.org/)
- [https://domains.google.com/](https://domains.google.com/)
- [https://www.ibm.com/support/knowledgecenter/SSGSCT_9.1.3/install_guide/pac_createdbschema_mysql_noha.html](https://www.ibm.com/support/knowledgecenter/SSGSCT_9.1.3/install_guide/pac_createdbschema_mysql_noha.html)
- [https://www.daniloaz.com/en/how-to-create-a-user-in-mysql-mariadb-and-grant-permissions-on-a-specific-database/](https://www.daniloaz.com/en/how-to-create-a-user-in-mysql-mariadb-and-grant-permissions-on-a-specific-database/)
- [https://wordpress.org/download/](https://wordpress.org/download/)
- [https://doc.ubuntu-fr.org/wget](https://doc.ubuntu-fr.org/wget)
- [https://lea-linux.org/documentations/Trucs:Compresser_d%C3%A9compresser_ZIP](https://lea-linux.org/documentations/Trucs:Compresser_d%C3%A9compresser_ZIP)
- [https://alvinalexander.com/blog/post/mysql/show-users-i-ve-created-in-mysql-database/](https://alvinalexander.com/blog/post/mysql/show-users-i-ve-created-in-mysql-database/)
