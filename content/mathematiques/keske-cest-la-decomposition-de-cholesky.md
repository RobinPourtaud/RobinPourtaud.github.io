---
title: "La Factorisation de Cholesky"
slug: "keske-cest-la-decomposition-de-cholesky"
date: "2020-04-18"
categories: 
  - "mathematiques"
tags: 
  - "cholesky"
  - "decomposition"
  - "matrice"
description: "Toute matrice symétrique définie positive A admet une décomposition de Cholesky. A étant égal à la multiplication d'une matrice triangulaire inférieure L par la matrice transposée de L."
---

## Définition :



Si A est une matrice symétrique définie positive, alors il existe une matrice triangulaire inférieure L telle que $A = L^tL$. On dit alors que A admet une factorisation de Cholesky (ou décomposition de Cholesky).

## Vérification :

Pour calculer la décomposition de A, nous devons vérifier que A est bien symétrique définie positive:

### Symétrique :

Une matrice $A$ est dite symétrique si $L = ^tL$. C'est à dire que $\forall i,j \in \dim{A}, A_{i,j} = A_{j,i}$.

Par exemple : $\begin{bmatrix} -4 & -2 \\ -2 & 13 \end{bmatrix}$

### Définie positive :

Une matrice A est dite définie positive si et seulement si ses valeurs propres sont positives. Je vous renvoie vers mon article sur les valeurs propres et vecteurs propres pour en savoir plus :

[Valeurs et Vecteurs propres - KeskeC.fr](https://keskec.fr/sciences/mathematiques/robin/684/)

## Résolution :

Une fois la vérification faite, en dimension 3, on cherche une matrice L telle que $A = L^tL$.

L = \begin{bmatrix} L_{1,1} & 0 & 0 \\  
L_{2,1} & L_{2,2} & 0 \\  
L_{3,1} & L_{3,2} & L_{3,3}\\  
\end{bmatrix}

$A = \begin{bmatrix} L_{1,1} & 0 & 0 \\ L_{2,1} & L_{2,2} & 0 \\ L_{3,1} & L_{3,2} & L_{3,3} \end{bmatrix}\begin{bmatrix} L_{1,1} & L_{2,1} & L_{3,1} \\ 0 & L_{2,2} & L_{3,2} \\ 0 & 0 & L_{3,3} \end{bmatrix}$

$A = \begin{bmatrix} L_{1,1}^2 & \* & \* \\ L_{2,1}L_{1,1} & L_{2,1}^2 + L_{2,2}^2& \* \\ L_{3,1}L_{1,1} & L_{3,1}L_{2,1}+L_{3,2}L_{2,2} & L_{3,1}^2 + L_{3,2}^2+L_{3,3}^2 \end{bmatrix}$

Il suffit maintenant de résoudre équation par équation le système $ A = L^tL$.

## Exemple :

Prenons $A = \begin{bmatrix} 1 & 2 \\ 2 & 7 \end{bmatrix}$.

A étant de taille 2x2, alors : $A = L^tL= \begin{bmatrix} L_{1,1}^2 & L_{1,1}L_{2,1} \\ L_{2,1}L_{1,1} & L_{2,1}^2 + L_{2,2}^2 \end{bmatrix}$.

Ce qui nous donne 4 équations:

- $1 = L_{1,1}^2$
- $2 = L_{1,1}L_{2,1}$
- $2 = L_{1,1}L_{2,1}$
- $7 = L_{2,1}^2 + L_{2,2}^2$

Donc:

- $L_{1,1}=1$
- $L_{2,1}=2$
- $L_{2,2}=\sqrt{3}$

$A=L^tL=\begin{bmatrix}1 & 2\\ 2 & 7 \end{bmatrix} = \begin{bmatrix}1 & 0\\ 2 & \sqrt{3}\end{bmatrix}\begin{bmatrix}1 & 2\\ 0 & \sqrt{3} \end{bmatrix}$

## Utile pour le calcul de déterminant !

La décomposition de Cholesky offre un avantage pour le calcul de déterminant.

En effet, L étant triangulaire :

 $\det{A}=\det{L^tL}=\det{L}\times\det{^tL}=\det{L}^2=(\prod_{i=1}^{dim L}L_{i,i})^2$

## En python :

Il est possible d'effectuer une factorisation de Cholesky rapidement en Python grâce à numpy !

```
import numpy as np

A = np.array([[1,2], [2,7]])
B = np.linalg.cholesky(A)
print(B)
```

Pour en savoir plus : [numpy.linalg.cholesky](https://numpy.org/doc/stable/reference/generated/numpy.linalg.cholesky.html).

### Sources:

1. [https://en.wikipedia.org/wiki/Cholesky_decomposition](https://en.wikipedia.org/wiki/Cholesky_decomposition)
2. [https://fr.wikipedia.org/wiki/Factorisation_de_Cholesky](https://fr.wikipedia.org/wiki/Factorisation_de_Cholesky)
3. [http://perso.eleves.ens-rennes.fr/~ariffaut/Agregation/Cholesky.pdf](http://perso.eleves.ens-rennes.fr/~ariffaut/Agregation/Cholesky.pdf)
