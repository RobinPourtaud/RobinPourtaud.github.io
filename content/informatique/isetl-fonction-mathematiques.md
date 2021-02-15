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



Soit $x$ et $y$, deux réels quelconques :

<table><tbody><tr><td><strong>Fonction ISETL</strong></td><td><strong>Fonction mathématiques</strong></td></tr><tr><td>abs(x)</td><td>$|x|$</td></tr><tr><td>exp(x)</td><td>$e^x$</td></tr><tr><td>ceil(x)</td><td>$\lceil x \rceil$</td></tr><tr><td>floor(x)</td><td>$\lfloor x \rfloor$</td></tr><tr><td>ln(x)</td><td>$\ln x$</td></tr><tr><td>log(x)</td><td>$\log x $</td></tr><tr><td>max(x,y)</td><td>$\max (x,y)$</td></tr><tr><td>min(x,y)</td><td>$\min (x,y)$</td></tr><tr><td>sgn(x)</td><td>$\left\{\begin{array}{rcr} 1 &amp; si &amp; x&gt;0 \ 0 &amp; si &amp; x = 0 \ -1 &amp; si &amp; x&lt;0 \ \end{array}\right.$</td></tr><tr><td>sqrt(x)</td><td>$\sqrt{x} $</td></tr></tbody></table>

Fonctions Mathématiques ISETL

NB : Il ne faut pas oublier qu'ISETL est utilisé habituellement sur des ensembles finis, comme pour l'exemple suivant :

![fonctions](images/isetlmath-1024x664.png)

Fonction Mathématique en ISETL

Un ensemble fini ne possède pas une notation unique :

- Sans relation d'ordre : $\{-6,-5\}=\{-5,-6\}$.
- La répétition d'éléments entre les accolades ne modifie pas non plus l'ensemble : $\{-5,-5\}=\{-5\}$.

C'est pourquoi, dans l'exemple ci-dessus, $E = \{-1,0,1\}$ et non $\{-1,-1,0,1\}$.

## Fonction Trigonométriques et Hyperboliques

Les fonctions trigonométriques et hyperboliques ISETL sont répertoriées dans un précédent article de KeskeC :

[ISETL – Fonctions trigonométriques et hyperboliques](https://keskec.fr/sciences/informatique/robin/3131/)
