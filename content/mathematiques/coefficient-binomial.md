+++
date = ""
description = "Cet article présente la notion de coefficient binomial, illustrée d'exemples et d'exercices corrigés. Un niveau de 1ère/Terminale est préférable pour pouvoir suivre cet article. Un rappel sur la notion de factoriel y sera explicité. "
draft = true
image_src = ""
tags = []
title = "Coefficient Binomial"
[image]
src = "static/images/UAL.png"
[[source]]
src = ["https://google.fr"]
title = ["Google"]

+++
## Prérequis :

La notion de factoriel est nécessaire pour pouvoir suivre cet article. Noté "!", le factoriel de n est le produit (usuellement) des entiers naturels de 1 à n. Autrement dit :

{{< latex "n! = ²Pi_{k=1}^{n}k = 1 ²times 2 ²times ²ldots ²times (n-1) ²times (n)">}}

Pour prendre plusieurs exemples :

* {{< latex "2! = 1 ²times 2" >}}
* {{< latex "5! = 1 ²times 2 ²times 3 ²times 4 ²times 5 = 120" >}}

Pour finir, prenez en compte que 0! = 1. Vous pouvez en savoir plus ici si vous êtes curieux :

[Pourquoi 0 factoriel est égale à 1 ? - KeskeC](https://keskec.fr/sciences/mathematiques/robin/4272/)

## Définition

En dénombrement, on définit le coefficient binomial comme le nombre de parties à "k" éléments dans un ensemble à "n" éléments, "k" et "n" étant des entiers naturels avec k inférieur ou égal à n.

On note le coefficient binomial par la formule :

{{< latex "²binom{n}{k} = C^k_n = ²frac{n!}{k!(n-k)!}">}}

Un ensemble de propriétés faisant intervenir les coefficients binomiaux est trouvable sur [Wikipédia](https://fr.wikipedia.org/wiki/Coefficient_binomial#Formules%20faisant%20intervenir%20les%20coefficients%20binomiaux).

## Exemple

### Graphiquement

On retrouve ce coefficient un peu partout en dénombrement, probabilité ou statistique. Pour prendre un exemple, dans le cadre d'une succession d'épreuves de Bernoulli, le coefficient binomial est utilisé pour calculer le nombre de k succès parmi n épreuves.

![](https://keskec.fr/wp-content/uploads/2021/01/image-5.png "Succession de n épreuves de Bernouilli")

Visiblement, selon cette arborescence, il y a :

* 1 façon d'obtenir 2 succès (2 parmi 2 = 1)
* 2 façons d'obtenir 1 succès (1 parmi 2 = 2)
* 1 façon d'obtenir 0 succès (0 parmi 2 = 1)

Cette symétrie dans les résultats se retrouvera bien sûr des arborescences plus grandes.

## Avec un ensemble

Soit un ensemble E = {a,b,c}

Calculons l'ensemble des parties de E :

Il y a :

* 1 élément à 0 élément (0 parmi 3 = 1)
* 3 éléments à 1 élément (0 parmi 3 = 3)
* 3 éléments à 2 éléments (0 parmi 3 = 3)
* 1 élément à 3 éléments (0 parmi 3 = 1)

Commentaire : L'ensemble des parties d'un ensemble E a pour cardinal 2^#E, ce qui correspond à la somme des cardinaux des parties à k éléments. Par exemple, nous avons bien pour cet exemple 1+3+3+1=2^3. Pour en savoir plus, [c'est ici](https://keskec.fr/sciences/mathematiques/robin/4073/).

## Exercice corrigé

Afin de voir si vous avez bien compris cette notion, je vous propose un petit exercice d'introduction :

### Enoncé

Un ami me propose de prendre 3 cartes dans un paquet de 52 cartes.   
Si j'obtiens le 5,6 et 7 de cœur (sans prendre en compte l'ordre), il m'a dit qu'il me donnerait 100€.

1. Combien y a-t-il de tirages possibles ?
2. Quelle est la probabilité d'obtenir ces 100€ ?

On veut obtenir 3 cartes spécifiques parmi un paquet de 52 cartes.

Si vous essayez de calculer ce chiffre "à la main", vous allez vite vous rendre compte que cette tâche va vite devenir compliquée. Utilisons donc notre formule !