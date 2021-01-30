+++
date = ""
description = "Cet article présente la notion de coefficient binomial, illustrée d'exemples et d'exercices corrigés. Un niveau de 1ère/Terminale est préférable pour pouvoir suivre cet article. Un rappel sur la notion de factoriel y sera explicité. "
draft = true
tags = "Dénombrement "
title = "Coefficient Binomial"

+++
## Prérequis :

La notion de factoriel est nécessaire pour pouvoir suivre cet article. Noté "!", le factoriel de n est le produit (usuellement) des entiers naturels de 1 à n. Autrement dit :

{{ latex "n! = \\Pi_{k=1}^{n}k = 1 \\times 2 \\times \\ldots \\times (n-1) \\times (n)" }}

n! = \\Pi_{k=1}^{n}k = 1 \\times 2 \\times \\ldots \\times (n-1) \\times (n)

* {{ latex "2! = 1 \\times 2" }}
* {{ latex "5! = 1 \\times 2 \\times 3 \\times 4 \\times 5 = 120" }}

Pour finir, prenez en compte que 0! = 1. Vous pouvez en savoir plus ici si vous êtes curieux :

[Pourquoi 0 factoriel est égale à 1 ? - KeskeC](https://keskec.fr/sciences/mathematiques/robin/4272/)

## Définition

En dénombrement, on définit le coefficient binomial comme le nombre de parties à "k" éléments dans un ensemble à "n" éléments, "k" et "n" étant des entiers naturels avec k inférieur ou égal à n.

On note le coefficient binomial par la formule :

{{ latex "\\binom{n}{k} = C^k_n = \\frac{n!}{k!(n-k)!}"}}