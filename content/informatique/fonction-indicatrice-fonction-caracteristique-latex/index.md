---
title: "Fonction Indicatrice / Fonction caractéristique - Latex"
slug: "fonction-indicatrice-fonction-caracteristique-latex"
date: "2021-01-05"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "latex"
description: "Cet article présente un moyen de générer le symbole usuel de la fonction indicatrice (ou fonction caractéristique). Ce symbole peut aussi désigner la fonction identité."
---
## Package requis

Il existe plusieurs paquets permettant de générer un "1 ajouré". On peut y trouver dsfont notamment. Pour cet article, nous utiliserons le package bbold.

```tex
²usepackage{bbold}
```

_Le package amsfonts ne permet pas de générer un 1 ajouré, vous obtiendrez ce symbole :_

![](image-1.png#t1)

## Code Latex

Pour afficher le symbole de la fonction caractéristique, il faut utiliser la commande mathbb :

```tex
²mathbb{1}
```

## Résultat

Nous obtenons ainsi :

![](image.png#t1)


## Sources :

1. [Fonction caractéristique (théorie des ensembles) - Wikipédia](https://fr.wikipedia.org/wiki/Fonction_caract%C3%A9ristique_(th%C3%A9orie_des_ensembles))
2. [Bbold - Latex](https://mirrors.chevalier.io/CTAN/fonts/bbold/bbold.pdf)
