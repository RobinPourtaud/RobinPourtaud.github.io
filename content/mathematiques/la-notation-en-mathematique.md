---
title: "La notation \"?\" en mathématique : Termial"
slug: "la-notation-en-mathematique"
date: "2020-07-20"
categories: 
  - "mathematiques"
tags: 
  - "notation"
no: ""
---

Dans son livre "The Art of Computer Science", l'informaticien Donald Knuth introduisit la notation "?". Appelé Termial en anglais, la notation point d'interrogation n? représente la somme de tous les entiers naturels inférieurs ou égales à n.

## Nota Bene :

1. Il faut savoir que cette notation **n'est pas couramment employée** et se doit donc d'être utilisée dans le bon contexte.
2. La notation point d'interrogation est distincte de la [fonction de Minkowski](https://fr.wikipedia.org/wiki/Fonction_point_d%27interrogation).
3. Je n'ai pas trouvé de traduction pour "Termial" en français.

## Définition :

Le Termial est présenté par Knuth comme une fonction analogue à la fonction factorielle "!".

\[latexpage\]

La fonction factorielle étant définie $\\forall n \\in \\mathbb{N}$ par :

$\\quicklatex{size=25}n!=\\prod^n\_{i=1}i= 1 \\times 2 \\times \\ldots \\times (n-1) \\times n$

La fonction "termial" se définie par :

$\\quicklatex{size=25}n?=\\sum^n\_{i=1}i = 1 + 2 + \\ldots + (n-1) + n$

Cette série est grossièrement divergente.

## Extension pour n non entier :

Comme pour la fonction factorielle avec la fonction gamma, il est possible d'étendre la fonction "Termial" à des valeurs non entières en prenant :

$\\quicklatex{size=25}n?=\\sum^n\_{i=1}i = \\frac{n(n+1)}{2}$

Ainsi :

$\\quicklatex{size=25}0.5? = \\frac{0.5(0.5+1)}{2} = \\frac{3}{8}$

## Sources :

1. [DONALD ("DON") ERVIN KNUTH](https://amturing.acm.org/award_winners/knuth_1013846.cfm)
2. Donald E. Knuth (1997). _The Art of Computer Programming: Volume 1: Fundamental Algorithms_. 3rd Ed. Addison Wesley Longman, U.S.A. p. 48.
3. [en.wikipedia.org - Termial](https://en.wikipedia.org/wiki/Termial)
