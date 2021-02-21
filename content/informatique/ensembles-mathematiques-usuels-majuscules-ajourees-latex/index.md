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

```
\usepackage{amsfonts}
```

Vous pouvez ainsi via "mathbb" afficher les majuscules que vous souhaitez :

```
\mathbb{R}
```

Ce qui nous donne :



$\mathbb{R}$

## Tableau récapitulatif

Ce tableau liste quelques utilisation commune des majuscules ajourés en mathématique :

<table class="has-fixed-layout"><tbody><tr><td><strong>Ensemble</strong></td><td><strong>Code Latex</strong></td><td><strong>Affichage</strong></td></tr><tr><td>Biquaternion</td><td>\mathbb{B}</td><td>$\mathbb{B}$</td></tr><tr><td>Ensemble des nombres complexes</td><td>\mathbb{C}</td><td>$\mathbb{C}$</td></tr><tr><td>Ensemble des nombres décimaux</td><td>\mathbb{D}</td><td>$\mathbb{D}$</td></tr><tr><td>Espérance mathématique</td><td>\mathbb{E}</td><td>$\mathbb{E}$</td></tr><tr><td>Quaternion</td><td>\mathbb{H}</td><td>$\mathbb{H}$</td></tr><tr><td>Corps</td><td>\mathbb{K}</td><td>$\mathbb{K}$</td></tr><tr><td>Quaternion Hyperbolique</td><td>\mathbb{M}</td><td>$\mathbb{M}$</td></tr><tr><td>Ensemble des entiers naturels</td><td>\mathbb{N}</td><td>$\mathbb{N}$</td></tr><tr><td>Octonion</td><td>\mathbb{O}</td><td>$\mathbb{O}$</td></tr><tr><td>Ensemble des nombres premiers / Probabilité</td><td>\mathbb{P}</td><td>$\mathbb{P}$</td></tr><tr><td>Ensemble des nombres rationnels</td><td>\mathbb{Q}</td><td>$\mathbb{Q}$</td></tr><tr><td>Ensemble des nombres réels</td><td>\mathbb{R}</td><td>$\mathbb{R}$</td></tr><tr><td>Sédénion</td><td>\mathbb{S}</td><td>$\mathbb{S}$</td></tr><tr><td>Ensembles des entiers relatifs</td><td>\mathbb{Z}</td><td>$\mathbb{Z}$</td></tr></tbody></table>

Majuscules ajourés

Toutes les lettres de l'alphabet (latin ou grec) peuvent être prises en argument.

_Commentaire : La fonction indicatrice ne peut pas être affichée avec amsfonts, il faut utiliser un autre package. Vous pouvez retrouver un article sur le sujet ici (fonction indicatrice - KeskeC)._

## Sources :

1. [Nombre Hypercomplexe - Wikipédia](https://fr.wikipedia.org/wiki/Nombre_hypercomplexe)
2. [amsmath - Latex](https://ctan.tetaneutral.net/macros/latex/required/amsmath/amsldoc.pdf)
