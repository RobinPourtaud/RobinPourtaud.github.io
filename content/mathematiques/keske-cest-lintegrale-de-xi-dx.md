---
title: "L'intégrale de x^i dx"
slug: "keske-cest-lintegrale-de-xi-dx"
date: "2020-04-12"
categories: 
  - "mathematiques"
tags: 
  - "analyse"
  - "analyse-complexe"
  - "integrale"
  - "nombre-complexe"
no: ""
---

"i" est un nombre. Il est complexe certes, mais reste un nombre. Il est égale à la racine de "-1" Ainsi, les règles des intégrales qu'on connait et qu'on utilise avec les nombres réels sont tout aussi applicables.

## Méthode 1 : Traditionnelle et Rapide

\[latexpage\]

_Précision pour le reste de l'article :_  
_"C" est une constante polymorphe quelconque. J'utiliserais plusieurs fois "+ C", mais les différents C ne sont pas forcément identiques._

$x^i$ est de la forme $x^b$, $\\forall b \\in \\mathbb{C}$. Or, on sait que :

$\\quicklatex{size=22} \\int x^b dx = \\frac{x^{b+1}}{b+1}$

Nous obtenons donc la solution :

$\\quicklatex{size=22}\\int x^i dx = \\frac{x^{i+1}}{i+1} + C$.

## Méthode 2 : Pour le fun

Cette méthode n'est absolument pas nécessaire, ni pratique à utiliser. Cependant, elle sera utile pour réviser les formules d'Euler, l'intégration par partie, le changement de variable, et bien sûr les nombres complexes. C'est donc un très bon exercice pour réviser ses mathématiques de Licence 1-2.

### Réécriture de la formule :

$\\quicklatex{size=22}\\int x^i dx = \\int e^{i \\ln{x}} dx$

De plus, d'après les formules d'Euler :

$\\quicklatex{size=22} e^{i\\theta}=\\cos{\\theta}+ i \\times \\sin{\\theta}$

Ainsi :

$\\quicklatex{size=22} \\int e^{i \\ln{x}} = \\int \\cos{\\ln{x}}+ i \\times \\sin{\\ln{x}} dx = \\int \\cos{\\ln{x}} dx+ i \\times \\int\\sin{\\ln{x}} dx$

### Changement de Variable

Soit $u = ln(x)$, alors $du = \\frac{1}{x} dx$ et donc $dx = x du$, $dx=e^u du$.

#### Intégrale 1 :

$\\quicklatex{size=22}\\int \\cos{\\ln{x}} dx = \\int \\cos{u}e^u du$

#### Intégrale 2 :

$\\quicklatex{size=22}\\int \\sin{\\ln{x}} dx = \\int \\sin{u}e^u du$

### Intégration par Partie

Par la formule d'intégration par partie ou par la méthode tabulaire nous obtenons

#### Intégrale 1 :

$\\quicklatex{size=22}\\int \\cos{u}e^u du = e^u \\cos{u} + e^u \\sin{u} - \\int \\cos{u}e^u du + C$

$\\quicklatex{size=22}2\\int \\cos{u}e^u du = e^u \\cos{u} + e^u \\sin{u} + C$

$\\quicklatex{size=22}\\int \\cos{u}e^u du = \\frac{1}{2} \\times (e^u \\cos{u} + e^u \\sin{u}) + C$

$\\quicklatex{size=22}\\int \\cos{u}e^u du = \\frac{e^u}{2} \\times ( \\cos{u}+ \\sin{u}) + C$

#### Intégrale 2 :

$\\quicklatex{size=22}\\int \\sin{u}e^u du = e^u \\sin{u} - e^u \\cos{u} - \\int \\sin{u}e^u du + C$

$\\quicklatex{size=22}2\\int \\sin{u}e^u du = e^u \\sin{u} - e^u \\cos{u} + C$

$\\quicklatex{size=22}\\int \\sin{u}e^u du = \\frac{1}{2} \\times (e^u \\sin{u} - e^u \\cos{u}) + C$

$\\quicklatex{size=22}\\int \\sin{u}e^u du = \\frac{e^u}{2} \\times (\\sin{u} - \\cos{u}) + C$

#### Regroupement :

$\\quicklatex{size=22}\\int \\cos{u}e^u du + i \\times \\int \\sin{u}e^u du = \\frac{e^u}{2}(\\cos{u}+\\sin{u}+i\\sin{u}-i\\cos{u}) + C$

$\\quicklatex{size=22}=\\frac{x}{2} \\times (\\cos{ln{x}}+\\sin{ln{x}}+i\\sin{ln{x}}-i\\cos{ln{x}})+C$

Ceci est une solution de l'intégrale, on pourrait donc s’arrêter là si on le souhaite...

### Application des formules d'Euler et simplification

D'après les formules d'Euler, on sait que :

$\\quicklatex{size=22}\\cos{x} = \\frac{e^{i\\theta}+e^{-i\\theta}}{2}$

Ainsi que :

$\\quicklatex{size=22}\\sin{x} = \\frac{e^{i\\theta}-e^{-i\\theta}}{2i}$

Donc :

$\\quicklatex{size=22}=\\frac{x}{2} \\times (\\cos{ln{x}}+\\sin{ln{x}}+i\\sin{ln{x}}-i\\cos{ln{x}})+C$

$\\quicklatex{size=22}=\\frac{x}{2} \\times(\\frac{e^{i ln{x}}+e^{-i ln{x}}}{2} - i \\times \\frac{e^{i ln{x}}+e^{-i ln{x}}}{2} + \\frac{e^{i ln{x}}-e^{-i ln{x}}}{2i} + i \\times \\frac{e^{i ln{x}}-e^{-i ln{x}}}{2i})$

D'abord :

$\\quicklatex{size=22}=\\frac{x}{4} \\times(x^i + x^{-i} -ix^i -ix^-i+x^i-x^{-i}+\\frac{x^i-x^{-i}}{i})$

Donne :

$\\quicklatex{size=22}=\\frac{x}{4} \\times(2x^i -ix^i - ix^{-i}-ix^i+ix^{-i})$

Ensuite :

$\\quicklatex{size=22}=\\frac{x}{4} \\times(2x^i-2ix^{i})$

$\\quicklatex{size=22}=\\frac{x(x^i-ix^{i})}{2}$

$\\quicklatex{size=22}=\\frac{x^{i+1}-ix^{1+i}}{2}$

$\\quicklatex{size=22}=\\frac{x^{i+1}(1-i)}{2}$

Donc, en multipliant par "i+1" :

$\\quicklatex{size=22} \\int x^i dx = \\frac{x^{i+1}}{i+1} + C$.

Voilà donc 2 méthodes de longueurs très différentes :).
