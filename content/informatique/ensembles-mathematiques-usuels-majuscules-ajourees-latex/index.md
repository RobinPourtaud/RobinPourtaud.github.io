---
title: "Ensembles mathématiques usuels (majuscules ajourées) - Latex"
slug: "ensembles-mathematiques-usuels-majuscules-ajourees-latex"
date: "2021-01-05"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "latex"
description: "Cet article présente la façon usuelle d'afficher les symboles utilisés pour désigner certains ensembles mathématiques. Ces symboles, appelés **majuscule ajourées** serons explicités dans un tableau récapitulatif."
---
## Ajourer une majuscule :

Pour ajourer une majuscule (mettre une majuscule sous forme usuelle des ensembles) en Latex, il suffit d'importer amsfonts :

```tex
\usepackage{amsfonts}
```

Vous pouvez ainsi via "mathbb" afficher les majuscules que vous souhaitez :

```tex
\mathbb{R}
```

Ce qui nous donne :



$$\mathbb{R}$$

## Tableau récapitulatif

Ce tableau liste quelques utilisation commune des majuscules ajourés en mathématique :

|Ensemble|Code Latex|Affichage|
|--- |--- |--- |
|Biquaternion|²mathbb{B}|$\mathbb{B}$|
|Ensemble des nombres complexes|²mathbb{C}|$\mathbb{C}$|
|Ensemble des nombres décimaux|²mathbb{D}|$\mathbb{D}$|
|Espérance mathématique|²mathbb{E}|$\mathbb{E}$|
|Quaternion|²mathbb{H}|$\mathbb{H}$|
|Corps|²mathbb{K}|$\mathbb{K}$|
|Quaternion Hyperbolique|²mathbb{M}|$\mathbb{M}$|
|Ensemble des entiers naturels|²mathbb{N}|$\mathbb{N}$|
|Octonion|²mathbb{O}|$\mathbb{O}$|
|Ensemble des nombres premiers / Probabilité|²mathbb{P}|$\mathbb{P}$|
|Ensemble des nombres rationnels|²mathbb{Q}|$\mathbb{Q}$|
|Ensemble des nombres réels|²mathbb{R}|$\mathbb{R}$|
|Sédénion|²mathbb{S}|$\mathbb{S}$|
|Ensembles des entiers relatifs|²mathbb{Z}|$\mathbb{Z}$|

Toutes les lettres de l'alphabet (latin ou grec) peuvent être prises en argument.

_Commentaire : La fonction indicatrice ne peut pas être affichée avec amsfonts, il faut utiliser un autre package. Vous pouvez retrouver un article sur le sujet ici (fonction indicatrice - KeskeC)._

## Sources :

1. [Nombre Hypercomplexe - Wikipédia](https://fr.wikipedia.org/wiki/Nombre_hypercomplexe)
2. [amsmath - Latex](https://ctan.tetaneutral.net/macros/latex/required/amsmath/amsldoc.pdf)


