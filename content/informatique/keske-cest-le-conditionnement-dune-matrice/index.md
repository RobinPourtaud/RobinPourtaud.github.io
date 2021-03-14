---
title: "Conditionnement d'une Matrice"
slug: "keske-cest-le-conditionnement-dune-matrice"
date: "2020-04-11"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "algebre"
  - "analyse"
  - "optimisation-informatique"
  - "systeme-lineaire"
description: "Cet article présente ce qu'est le conditionnement d'une matrice inversible et sa norme infinie, illustré par deux exemples."
---


## Définition

Un système linéaire peut s'écrire sous forme de matrice par une équation du type AX=B. On dit de la matrice A qu'elle est mal conditionnée si une petite variation de B entraîne une grande variation de X.

Pour une matrice inversible A, sa fonction de conditionnement est :

$\kappa(A)=\Vert A \Vert \Vert A^{-1} \Vert $

Note : Plus $\kappa$ est élevé, plus la matrice A est mal conditionnée.

## Exemple 1

Pour comprendre ce qu'est le conditionnement, prenons un exemple de système linéaire $AX=Y$ :

### Matrice A et sa solution

Soit une matrice A :

$A=\begin{bmatrix} 10 & 7 & 8 & 7 \\ 7 & 5 & 6 & 5 \\8 & 6 & 10 & 9 \\ 7 & 5 & 9 & 10 \end{bmatrix}, Y=\begin{bmatrix}32 \\ 23 \\ 33 \\ 31\end{bmatrix}$

La solution de ce système sera donc :

$X = \begin{bmatrix}1\\1\\1\\1\end{bmatrix}$

### Exemple de variation

Il est intéressant de remarquer que si on varie faiblement $Y$ :

$\Delta_Y=\begin{bmatrix}0.1\\-0.1\\0.1\\-0.1\end{bmatrix}$

Nous obtenons :

$X=\begin{bmatrix}9.2\\-12.6\\4.5\\-11\end{bmatrix}$

Une petite variation $\Delta_Y$ sur $Y$ implique une grande variation de $X$.  
On dira de la matrice $A$ qu'elle est "**mal conditionnée**".

### Calcul du conditionnement

La fonction de conditionnement d’une matrice $A$ est $\kappa(A)=\Vert A \Vert \Vert A^{-1} \Vert $, $A$ ayant un déterminant différent de 0 et donc étant inversible. Prenons la norme infini :

$\kappa(A)=\Vert A \Vert _\infty \Vert A^{-1} \Vert _\infty = \max_{\\{1\le i \le n\\}} \sum^n_{j=1}|A_{i,j}| \times \max_{\\{1\le i \le n\\}} \sum^n_{j=1}|A_{i,j}^{-1}|$ avec $n = \dim A$.

Dans cet exemple: $\kappa(A)=33 \times 136 = 4488$.

### En python

Pour calculer le conditionnement rapidement en python, je vous propose de faire :

```
import numpy as np 
A = np.array([[10,7,8,7],[7,5,6,5],[8,6,10,9],[7,5,9,10]])
print(np.linalg.cond(A,np.inf))
```

Vous devriez obtenir le même résultat !

Pour en savoir plus sur le conditionnement : [Python avec Numpy](https://keskec.fr/sciences/informatique/robin/2057/#Conditionnement_de_Matrice).

## Exemple 2

Pour prendre un autre exemple: La "matrice B" est bien conditionnée:

Soit la matrice inversible B :

$B=\begin{bmatrix}1&7&2&1\\7&5&1&5\\8&6&10&9\\7&5&9&1\end{bmatrix}$.

Nous avons : $\kappa(B)=33\times 0.4496=14.8368$

Cette matrice est relativement bien conditionnée en comparaison avec la matrice $A$.

Nous pouvons donc affirmer que pour un système linéaire $BX=Y$, une petite variation de $Y$ n’engendra pas une grosse variation $X$.

## Sources

1. [Conditionnement d'une matrice - bibmath.net](http://www.bibmath.net/dico/index.php?action=affiche&quoi=./c/conditionnement.html)
2. [NORMES ET CONDITIONNEMENT D’UNE MATRICE](https://www.i2m.univ-amu.fr/perso/thierry.gallouet/licence.d/anum.d/anum-tg2.pdf)
3. [Conditionnement d'une matrice](http://wiki.inra.fr/wiki/cascisdi/Production/Conditionnement+d%27une+matrice)
