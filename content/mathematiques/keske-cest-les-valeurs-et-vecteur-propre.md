---
title: "Les Valeurs et Vecteurs Propres"
slug: "keske-cest-les-valeurs-et-vecteur-propre"
date: "2020-04-19"
categories: 
  - "mathematiques"
tags: 
  - "algebre-2"
  - "valeurs-propres"
  - "vecteurs-propres"
no: ""
---

Un scalaire lambda est une valeur propre de f si il existe un vecteur x non nul tel que f(x) = lambda x.

\[latexpage\]

Soit E un espace vectoriel de dimension fini, sur $\\mathbb{K}$. $f$ un endomorphisme (applications linéaires d'un espace vectoriel dans lui-même) de E.

## Définition

Un scalaire $\\lambda$ est une valeur propre de $f$ s'il existe un vecteur x (le vecteur propre) non nul tel que $f(x)=\\lambda x$.

## Exemple

$A = \\begin{bmatrix} 7 & 2 \\\\ -4 & 1 \\end{bmatrix}$.

### Calcul du Polynôme Caractéristique

Le polynome caractéristique de A est défini comme: $\\chi\_A(\\lambda) = \\det(\\lambda I\_{dim A} - A)$.

Ainsi :

$\\chi\_A(\\lambda) = \\det \\begin{bmatrix} \\lambda - 7 & -2 \\\\ 4 & \\lambda -1 \\end{bmatrix} = (\\lambda - 7)(\\lambda - 1) + 8 = (\\lambda - 3)(\\lambda - 5)$.

### Calcul des Valeurs Propres

Les valeurs propres sont les racines du polynôme caractéristique. C'est à dire les solutions de $\\ker \\chi\_A(\\lambda)$.

$(\\lambda - 3)(\\lambda - 5) = 0$ Admet 2 solutions: $\\lambda\_{1,2}=\\{3,5\\}$

Le Spectre d'une matrice est l'ensembles de ses Valeurs Propres associées. Ainsi :

$Sp(A)=\\{3,5\\}$

### Calcul des Vecteurs Propres

Pour calculer les Vecteurs Propres, on cherche les solutions de $\\ker(\\lambda\_{1,2} I - A)$.

Pour $\\lambda = 3$.

$\\ker (3I - A) = \\ker \\begin{bmatrix} -4 & -2 \\\\ 4 & 2 \\end{bmatrix}$

Soit un Vecteur $x = \\begin{bmatrix} X \\\\ Y \\end{bmatrix}$.

$\\begin{bmatrix} -4 & -2 \\\\ 4 & 2 \\end{bmatrix}\\begin{bmatrix} X \\\\ Y \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\end{bmatrix} \\Rightarrow 2X+Y = 0 \\Rightarrow Y=-2X \\Rightarrow \\begin{bmatrix} X \\\\ Y \\end{bmatrix} = X \\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix}$

$\\ker(3I - A) = Vect\\{\\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix}\\}$

Un vecteur propre associé à $\\lambda = 3$ est donc $\\begin{bmatrix} 1 \\\\ -2 \\end{bmatrix}$.

De la même façon, un vecteur propre de $\\lambda=5$ est $\\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix}$.

### Sources

- [https://fr.wikipedia.org/wiki/Valeur\_propre,\_vecteur\_propre\_et\_espace\_propre](https://fr.wikipedia.org/wiki/Valeur_propre,_vecteur_propre_et_espace_propre)
- [https://www.dcode.fr/vecteurs-propres-matrice](https://www.dcode.fr/vecteurs-propres-matrice)
- [https://www-fourier.ujf-grenoble.fr/~parisse/mat249/mat249/node48.html](https://www-fourier.ujf-grenoble.fr/~parisse/mat249/mat249/node48.html)
- [http://www.unige.ch/~hairer/poly\_mathinfo/math-info.pdf](http://www.unige.ch/~hairer/poly_mathinfo/math-info.pdf)
- [http://www.bibmath.net/dico/index.php?action=affiche&quoi=./p/polynomecar.html](http://www.bibmath.net/dico/index.php?action=affiche&quoi=./p/polynomecar.html)
