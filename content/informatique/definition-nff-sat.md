---
title: "Définition : NFF-Sat"
slug: "definition-nff-sat"
date: "2020-11-22"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "complexite-asymptotique"
no: ""
---

Un problème de satisfaction de contraintes booléennes, aussi appelé problème de satisfiabilité, consiste à déterminer, pour un ensemble de contraintes définies sur des variables booléennes, s’il existe une assignation de valeurs aux variables satisfaisant toutes les contraintes.

## Un peu de vocabulaire :

### Définition : Forme normale négative

On dit d'une formule logique, qu'elle est en forme normale négative (FNN) si :

- Les négations se trouvent uniquement sur les littéraux.
- En plus de l'opérateur de négation, seul l'opérateur de conjonction ("et") et de disjonction ("ou") est autorisé.

Pour prendre un exemple :



- {{< latex "\overline{A \wedge B}" >}} n'est pas sous forme normale négative.
- {{< latex "\overline{A}\wedge B" >}} est sous forme normale négative.

### Définition : Satisifiabilité

On dit d'une formule booléenne qu'elle est satisfiable s'il existe une assignation (ou valuation) des variables tel qu'elle rende la formule "vrai".

Par exemple :

- {{< latex "\overline{A}\wedge A" >}} n'est pas satisfiable
- {{< latex "\overline{A}\lor A" >}} est satisfiable

Fun-Fact : Dans le deuxième cas, peu importe la valeur de notre seule variable A, notre formule est satisfiable, on peut dans ce cas parler de tautologie.

## Le problème NFF-Sat :

Le problème NFF-Sat, ou NegLit-Sat peut se présenter en 2 lignes :

Soit {{< latex "\mathcal{F}" >}} une formule booléenne telle que {{< latex "\mathcal{F}" >}} est sous forme normale négative.

{{< latex "\mathcal{F}" >}} est-elle satisfiable ?

## Sources :

1. [Représentations de formules SAT pour la Résolution Séquentielle](http://www.univ-bejaia.dz/jspui/bitstream/123456789/9590/1/Representations%20de%20formules%20SAT%20pour%20la%20resolution%20sequentielle.pdf)
2. [Valuation Logic - Wikipédia](https://en.wikipedia.org/wiki/Valuation_(logic))
3. [Satisfiability - Wikipédia](https://en.wikipedia.org/wiki/Satisfiability)
4. [Negation normal form - Wikipédia](https://en.wikipedia.org/wiki/Negation_normal_form?oldid=711179836)
