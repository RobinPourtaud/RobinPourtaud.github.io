---
title: "ISETL - Fonctions Mathématiques"
slug: "isetl-fonction-mathematiques"
date: "2020-06-18"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "isetl"
  - "tuto"
description: "Cet article a pour finalité de lister des fonctions mathématiques implémentées par défaut dans ISETL3.0."
---

## Prérequis :

Il est bien sur nécessaire d'avoir accès à un interpréteur ISETL sur votre ordinateur. Si ce n'est pas le cas, je vous renvoie vers mon article :

[ISETL 3.0 sur Windows 10](https://keskec.fr/sciences/informatique/robin/2690/)

## Liste de fonctions mathématiques ISETL :



Soit {{< latex "x" >}} et {{< latex "y" >}}, deux réels quelconques :

<table><tbody><tr><td><strong>Fonction ISETL</strong></td><td><strong>Fonction mathématiques</strong></td></tr><tr><td>abs(x)</td><td>{{< latex "|x|" >}}</td></tr><tr><td>exp(x)</td><td>{{< latex "e^x" >}}</td></tr><tr><td>ceil(x)</td><td>{{< latex "\lceil x \rceil" >}}</td></tr><tr><td>floor(x)</td><td>{{< latex "\lfloor x \rfloor" >}}</td></tr><tr><td>ln(x)</td><td>{{< latex "\ln x" >}}</td></tr><tr><td>log(x)</td><td>{{< latex "\log x " >}}</td></tr><tr><td>max(x,y)</td><td>{{< latex "\max (x,y)" >}}</td></tr><tr><td>min(x,y)</td><td>{{< latex "\min (x,y)" >}}</td></tr><tr><td>sgn(x)</td><td>{{< latex "\left\{\begin{array}{rcr} 1 &amp; si &amp; x&gt;0 \ 0 &amp; si &amp; x = 0 \ -1 &amp; si &amp; x&lt;0 \ \end{array}\right." >}}</td></tr><tr><td>sqrt(x)</td><td>{{< latex "\sqrt{x} " >}}</td></tr></tbody></table>

Fonctions Mathématiques ISETL

NB : Il ne faut pas oublier qu'ISETL est utilisé habituellement sur des ensembles finis, comme pour l'exemple suivant :

![fonctions](images/isetlmath-1024x664.png)

Fonction Mathématique en ISETL

Un ensemble fini ne possède pas une notation unique :

- Sans relation d'ordre : {{< latex "\{-6,-5\}=\{-5,-6\}" >}}.
- La répétition d'éléments entre les accolades ne modifie pas non plus l'ensemble : {{< latex "\{-5,-5\}=\{-5\}" >}}.

C'est pourquoi, dans l'exemple ci-dessus, {{< latex "E = \{-1,0,1\}" >}} et non {{< latex "\{-1,-1,0,1\}" >}}.

## Fonction Trigonométriques et Hyperboliques

Les fonctions trigonométriques et hyperboliques ISETL sont répertoriées dans un précédent article de KeskeC :

[ISETL – Fonctions trigonométriques et hyperboliques](https://keskec.fr/sciences/informatique/robin/3131/)
