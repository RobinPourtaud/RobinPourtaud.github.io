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



Soit E un espace vectoriel de dimension fini, sur {{< latex "\mathbb{K}" >}}. {{< latex "f" >}} un endomorphisme (applications linéaires d'un espace vectoriel dans lui-même) de E.

## Définition

Un scalaire {{< latex "\lambda" >}} est une valeur propre de {{< latex "f" >}} s'il existe un vecteur x (le vecteur propre) non nul tel que {{< latex "f(x)=\lambda x" >}}.

## Exemple

{{< latex "A = \begin{bmatrix} 7 & 2 \\ -4 & 1 \end{bmatrix}" >}}.

### Calcul du Polynôme Caractéristique

Le polynome caractéristique de A est défini comme: {{< latex "\chi_A(\lambda) = \det(\lambda I_{dim A} - A)" >}}.

Ainsi :

{{< latex "\chi_A(\lambda) = \det \begin{bmatrix} \lambda - 7 & -2 \\ 4 & \lambda -1 \end{bmatrix} = (\lambda - 7)(\lambda - 1) + 8 = (\lambda - 3)(\lambda - 5)" >}}.

### Calcul des Valeurs Propres

Les valeurs propres sont les racines du polynôme caractéristique. C'est à dire les solutions de {{< latex "\ker \chi_A(\lambda)" >}}.

{{< latex "(\lambda - 3)(\lambda - 5) = 0" >}} Admet 2 solutions: {{< latex "\lambda_{1,2}=\{3,5\}" >}}

Le Spectre d'une matrice est l'ensembles de ses Valeurs Propres associées. Ainsi :

{{< latex "Sp(A)=\{3,5\}" >}}

### Calcul des Vecteurs Propres

Pour calculer les Vecteurs Propres, on cherche les solutions de {{< latex "\ker(\lambda_{1,2} I - A)" >}}.

Pour {{< latex "\lambda = 3" >}}.

{{< latex "\ker (3I - A) = \ker \begin{bmatrix} -4 & -2 \\ 4 & 2 \end{bmatrix}" >}}

Soit un Vecteur {{< latex "x = \begin{bmatrix} X \\ Y \end{bmatrix}" >}}.

{{< latex "\begin{bmatrix} -4 & -2 \\ 4 & 2 \end{bmatrix}\begin{bmatrix} X \\ Y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix} \Rightarrow 2X+Y = 0 \Rightarrow Y=-2X \Rightarrow \begin{bmatrix} X \\ Y \end{bmatrix} = X \begin{bmatrix} 1 \\ -2 \end{bmatrix}" >}}

{{< latex "\ker(3I - A) = Vect\{\begin{bmatrix} 1 \\ -2 \end{bmatrix}\}" >}}

Un vecteur propre associé à {{< latex "\lambda = 3" >}} est donc {{< latex "\begin{bmatrix} 1 \\ -2 \end{bmatrix}" >}}.

De la même façon, un vecteur propre de {{< latex "\lambda=5" >}} est {{< latex "\begin{bmatrix} 1 \\ -1 \end{bmatrix}" >}}.

### Sources

- [https://fr.wikipedia.org/wiki/Valeur_propre,_vecteur_propre_et_espace_propre](https://fr.wikipedia.org/wiki/Valeur_propre,_vecteur_propre_et_espace_propre)
- [https://www.dcode.fr/vecteurs-propres-matrice](https://www.dcode.fr/vecteurs-propres-matrice)
- [https://www-fourier.ujf-grenoble.fr/~parisse/mat249/mat249/node48.html](https://www-fourier.ujf-grenoble.fr/~parisse/mat249/mat249/node48.html)
- [http://www.unige.ch/~hairer/poly_mathinfo/math-info.pdf](http://www.unige.ch/~hairer/poly_mathinfo/math-info.pdf)
- [http://www.bibmath.net/dico/index.php?action=affiche&quoi=./p/polynomecar.html](http://www.bibmath.net/dico/index.php?action=affiche&quoi=./p/polynomecar.html)
