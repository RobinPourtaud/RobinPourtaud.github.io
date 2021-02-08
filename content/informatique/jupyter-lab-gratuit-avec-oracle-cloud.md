---
title: "Jupyter Lab gratuit avec Oracle Cloud"
slug: "jupyter-lab-gratuit-avec-oracle-cloud"
date: "2020-09-29"
categories: 
  - "informatique"
tags: 
  - "jupyter-notebook"
  - "linux"
no: ""
---

Gratuitement, de grandes entreprises (Google, IBM, Microsoft, ...) proposent un accès à leur Jupyter Notebook. Jupyter Lab, cependant, ne fait pas partie de leurs offres gratuites (sans durée limitée et sans restriction conséquentes). C'est dans cette optique que j'ai découvert l'accès "Always free" de Oracle, nous permettant aisément de créer notre Jupyter Lab personnel...

## Résumé

Oracle propose depuis bientôt un an une offre appelée "[Always Free](https://www.oracle.com/fr/cloud/free/#always-free)". Celle-ci comprend :

- Deux bases de données Oracle Autonomous Database avec des outils puissants tels qu’Oracle Application Express (APEX) et Oracle SQL Developer
- Deux machines virtuelles de calcul Oracle Cloud Infrastructure Compute ; stockage de niveau bloc, objet et archive ; équilibreur de charge et extraction de données ; surveillance et notifications
- Pendant les 30 premiers jours 300$ de crédit sur leur plateforme

![](images/image-7-1024x371.png)

Source : [oracle.com](https://www.oracle.com/fr/cloud/free/#always-free)

La configuration des machines virtuelles est la suivante :

![](images/image-11-1024x156.png)

Machine Virtuelle AMD - Oracle Cloud

Si vous souhaitez une configuration plus "confortable", il sera nécessaire de passer à un plan payant après 30 jours...

## Prérequis

Pour suivre ce tutoriel, il est nécessaire d'avoir un accès en ssh sur son ordinateur (sous Linux, avec wsl2, avec putty....).

## Inscription à Oracle Cloud

Durant l'inscription, vous aurez besoin de rentrer de nombreuses informations personnelles telles que votre adresse postale ou encore vos coordonnées de carte bleue.

Cependant, il est important de noter que vous ne serez ni prélevé maintenant, ni au bout de 30 jours (du moins pas sans votre accord).

Pour vous inscrire, connectez-vous ici :

[Oracle Cloud Account Signup](https://myservices.us.oraclecloud.com/mycloud/signup)

Suivez cette inscription. Cela dure maximum 5 min.

## Création d'une machine virtuelle

Une fois inscrit, vous devrez vous retrouver sur cette page :

![](images/image-8-1024x397.png)

Oracle Cloud - Accueil

1. Cliquez sur "Create a VM instance"
2. Nommez votre instance du nom de votre choix
3. Choisissez l'image "Always free" de votre choix (la suite du tutoriel peut varier selon l'image choisie)  
    

![](images/image-9-1024x765.png)

Choix du système d'exploitation - Oracle Cloud

4. Cliquez ensuite sur "Show Shape, Network and Storage Options"
5. Puis "Change Shape"
6. Ensuite "Virtual Machine"
7. Sur "Specialty and Legacy"
8. Et sélectionnez la ressource "Always Free Eligible" comme sur l'image ci-dessous (si aucune n'est disponible, essayez de modifier dans la fenêtre précédente "availability domain") :

![](images/image-10-1024x742.png)

Choix de la VM - Oracle Cloud

9. Enfin, sauvegardez la clé privée pour accéder à votre machine via ssh :

![](images/image-12-1024x341.png)

Sauvegarde des clés SSH - Oracle Cloud

10. Vous pouvez maintenant cliquer sur "Create" !

## Se connecter à la machine Virtuelle via SSH

Pour vous connecter avec putty, je vous renvoie vers [ce lien](https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/).

Pour vous connecter "traditionnellement" avec un terminal, **restez ici** !

Rendez-vous dans la liste des instances située dans :

"Menu de navigation en haut à gauche" > Compute > Instances

![](images/image-1024x288.png)

Liste des Instances - Oracle Cloud

Cliquez sur l'instance puis copiez l'IP public ainsi que le nom d'utilisateur.

Vous pouvez maintenant ouvrir un terminal et vous connecter à l'instance via SSH :

1. Ouvrez un terminal et allez dans le même dossier que votre "clé".
2. Entrez les 2 commandes suivantes :

```
chmod 500 <Votre clé>
ssh -i <Votre clé> <nom utilisateur>@<IP publique>
```

Résultat :

![](images/image-2-1024x603.png)

Connexion via SSH - Oracle Cloud

## Installation de Jupyter lab

Pour installer Jupyter Lab, nous aurons besoin de pip3. Pour l'installer :

```
sudo apt install python3-pip
```

Installons Jupyter Lab maintenant :

```
pip3 install jupyterlab 
```

Après son installation, terminez votre connexion ssh puis relancez là. Vous pouvez maintenant exécuter Jupyter Lab.

## Accès à Jupyter lab

Je vous propose de vous connecter à Jupyter Lab via un tunnel SSH, mais il est tout à fait possible de s'y connecter via l'IP public! Pour cela, je vous renvoie vers [la partie 2 d'un tutoriel de Oracle](https://docs.cloud.oracle.com/en-us/iaas/developer-tutorials/tutorials/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm).

Dans votre terminal, commencez par taper "jupyter lab" :

```
jupyter lab
```

Comme ceci :

![](images/image-3-1024x569.png)

Lancement de Jupyter Lab - Oracle Cloud

Laissez ce terminal ouvert en ayant bien en tête le port sur lequel est déployé Jupyter Lab.

Ouvrez un nouveau terminal et tapez la commande :

```
sudo ssh -i <Votre clé> -L 80:localhost:<Port Jupyter>  <nom utilisateur>@<IP publique>
```

Cette commande permet de rediriger le port 80 de votre ordinateur vers le port jupyter de votre instance. Ainsi, ouvrez un navigateur et tapez "localhost", vous devriez être en mesure de vous connecter à Jupyter Lab !

![](images/image-4-1024x703.png)

Connexion à Jupyter Lab - Oracle Cloud

Pour finir, récupérez sur votre premier terminal le "token" et collez-le.

![](images/image-5-1024x727.png)

Jupyter Lab - Oracle Cloud

Enjoy :).

## Sources

1. [The Oracle Cloud Free Tier - medium.com](https://medium.com/@FranckPachot/the-oracle-cloud-free-tier-37c27f3b1e19)
2. [Oracle Cloud Free Tier - oracle.com](https://www.oracle.com/fr/cloud/free/)
3. [Installation Jupyter lab - readthedocs.io](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html)
4. [Comprendre la redirection de port (Port Forwarding) - linux-france.org](http://www.linux-france.org/prj/edu/archinet/systeme/ch13s04.html)
