---
title: "Installer PHP7.4 pour Wordpress"
slug: "installer-php7-4-sur-un-raspberry-pi"
date: "2020-04-21"
categories: 
  - "informatique"
tags: 
  - "apache2"
  - "debian"
  - "php"
  - "raspberry-pi"
  - "wordpress"
description: "PHP7.4 est actuellement la dernière version de PHP. Sortie fin 2019, je vais vous montrer la méthode la plus simple pour installer cette version de php sous Raspbian."
latex: false
---
Vous avez peut-être remarqué que votre WordPress tourne sous une ancienne version de PHP ? Vous avez donc sans doute vu ce message :

![Problème Critique PHP Wordpress](image-3-1024x331.png#t5)



Prenez 10 min de votre temps pour régler ce problème.

## Prérequis :

- Vous devez avoir un ordinateur mis à jour, sous une distribution basée sur debian (raspbian pour moi).
- Avoir les droits de super utilisateur et donc avoir accès à la commande "sudo".
- Avoir de préférence Apache2.

Pour mettre à jour votre ordinateur, rien de plus simple:

```bash
sudo apt update && sudo apt upgrade
```

## Installation du repository :

Ajoutons la clé du repository sury avec wget.

```bash
wget -qO - https://packages.sury.org/php/apt.gpg | sudo apt-key add -
```

Ajoutons le repository sury.

```bash
echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" | sudo tee /etc/apt/sources.list.d/php7.x.list
```

Mettez à nouveau à jour votre ordinateur.

```bash
sudo apt update && sudo apt upgrade
```

## Installation de PHP7.4

Si vous aviez installer une version de PHP antérieur, il est probable que la commande précédente ait déjà installé la dernière version de PHP :).

Vous pouvez vérifier votre version de php avec

```bash
php -v 
```

Sinon, vous pouvez maintenant utiliser la commande suivante pour installer PHP7.4 et un module apache.

```bash
sudo apt install php7.4
sudo apt install libapache2-mod-php7.4
```

(optionnel) Vous pouvez installer directement toutes les extensions:

```bash
sudo apt install php7.4-*
```

(Si vous aviez déjà PHP) Désactivez votre ancienne version de PHP pour apache2 (dans mon cas PHP7.0)

```bash
sudo a2dismod php7.0
```

Et bien sûr, activez php7.4

```bash
sudo a2enmod php7.4
```

Vous pouvez maintenant redémarrer Apache2 :).

```bash
sudo service apache2 restart
```

Wordpress ne devrait maintenant plus vous lister de problème critique.

![0 problème critique](image-4-1024x85.png#t5)



### Sources:

- [https://www.php.net/ChangeLog-7.php](https://www.php.net/ChangeLog-7.php)
- [https://launchpad.net/~ondrej/+archive/ubuntu/php](https://launchpad.net/~ondrej/+archive/ubuntu/php)
- [https://deb.sury.org/](https://deb.sury.org/)
