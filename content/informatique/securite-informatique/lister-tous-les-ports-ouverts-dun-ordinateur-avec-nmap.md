---
title: "Lister tous les ports ouverts d'un ordinateur avec nmap"
slug: "lister-tous-les-ports-ouverts-dun-ordinateur-avec-nmap"
date: "2020-08-24"
categories: 
  - "securite-informatique"
tags: 
  - "linux"
  - "nmap"
no: ""
---

Pour des raisons de sécurité, de recherche ou tout simplement de curiosité, il peut être nécessaire de scanner une ip pour en extraire une liste de ports ouverts. Ce tutoriel présente la façon, à ma connaissance, la plus rapide et la plus simple d'accomplir cette tâche grâce à nmap.

## Installer nmap

Pour ce tutoriel, nous utiliserons le programme nmap. Pour l'installer, rien de très compliqué :

Sous une distribution basée sur Debian :

```
sudo apt update
sudo apt install nmap
```

Sous ArchLinux :

```
pacman -Sy nmap
```

Sous plus de distributions ici : [https://nmap.org/download.html](https://nmap.org/download.html)

## Lister les ports ouverts

En fonction des paramètres envoyés à nmap, la recherche de ports peut aussi bien être très rapide que très lente.

Pour lister tous les ports ouverts pour une adresse ip ou domaine donné, je vous propose la commande suivante :

```
sudo nmap -p- -v -sS DOMAINE_OU_IP
```

L'option -p- signifie "Tous les ports".  
Pour scanner seulement certains ports, par exemple de 20 à 300, vous pouvez remplacer _"-p-"_ par _"-p 30-300"_.

L'option -v pour "verbose" signifie qu'on pourra avoir accès à l'avance de la recherche en cours, le retour programme sera plus "verbeux".

L'option -sS ou scan SYN est celui par défaut et le plus populaire pour de bonnes raisons. Il peut être exécuté rapidement et scanner des milliers de ports par seconde sur un réseau rapide lorsqu'il n'est pas entravé par des pare-feux. Le scan SYN est relativement discret et furtif, vu qu'il ne termine jamais les connexions TCP. \[2\]

Pour prendre un exemple :

```
sudo nmap -p- -v -sS google.fr
```

En moins de 3 secondes on obtient 2 ports communs découverts : Le 80 et le 443 correspondants aux ports ouverts pour les protocoles HTTP et HTTPS :

![](images/image-4-1024x583.png)

nmap google.fr

Avec un peu de patience, nous pouvons enfin avoir accès à ce magnifique tableau récapitulatif :

![](images/image-5.png)

Listes des ports ouverts de google.fr

## Sources

1. [Téléchargement nmap - nmap.org](https://nmap.org/download.html)
2. [Techniques de scan de ports - nmap.org](https://nmap.org/man/fr/man-port-scanning-techniques.html)
