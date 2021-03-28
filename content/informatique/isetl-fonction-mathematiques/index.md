---
title: "ISETL - Fonctions Mathématiques"
slug: "isetl-fonction-mathematiques"
date: "2020-06-18"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "isetl"
  
description: "Cet article a pour finalité de lister des fonctions mathématiques implémentées par défaut dans ISETL3.0."
---
## Prérequis :

Il est bien sur nécessaire d'avoir accès à un interpréteur ISETL sur votre ordinateur. Si ce n'est pas le cas, je vous renvoie vers mon article : [ISETL 3.0 sur Windows 10](/informatique/isetl-langage-de-programmation/)

## Liste de fonctions mathématiques ISETL :



Soit $x$ et $y$, deux réels quelconques :

|Fonction ISETL|Fonction mathématiques|
|--- |--- |
|abs(x)|$\lvert x \rvert$|
|exp(x)|$e^x$|
|ceil(x)|$\lceil x \rceil$|
|floor(x)|$\lfloor x \rfloor$|
|ln(x)|$\ln x$|
|log(x)|$\log x$|
|max(x,y)|$\max (x,y)$|
|min(x,y)|$\min (x,y)$|
|sgn(x)|$\begin{cases}1\text{ si }x>0\\0\text{ si }x=0\\-1\text{ si }x<0\end{cases}$|
|sqrt(x)|$\sqrt{x}$|

NB : Il ne faut pas oublier qu'ISETL est utilisé habituellement sur des ensembles finis, comme pour l'exemple suivant :

![Fonction Mathématique en ISETL](isetlmath-1024x664.png#t5)


Un ensemble fini ne possède pas une notation unique :

- Sans relation d'ordre : $\{-6,-5\}=\{-5,-6\}$.
- La répétition d'éléments entre les accolades ne modifie pas non plus l'ensemble : $\{-5,-5\}=\{-5\}$.

C'est pourquoi, dans l'exemple ci-dessus, $E = \{-1,0,1\}$ et non $\{-1,-1,0,1\}$.