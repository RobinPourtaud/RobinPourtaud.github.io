---
title: "ISETL - Conditions If, ElseIf, Else"
slug: "isetl-conditions-if-elseif-else"
date: "2020-07-26"
categories: 
  - "informatique"
tags: 
  - "isetl"
  - "tuto"
description: "Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité **l’enseignement des mathématiques discrètes à l’université**_._ Cet article est à destination des étudiants voulant apprendre à rédiger des conditions en ISETL."
---
## If, ElseIf et Else

En informatique, un "Si" permet d'exécuter une partie de code conditionnellement.  
**Par exemple**, prenons une variable x.

```
Si x > 5, alors on souhaite afficher "nombre > 5", 
Sinon Si x = 5, alors afficher "nombre = 5", 
Sinon, "nombre < 5". 
```

**En ISETL**, une structure conditionnelle se rédige de la façon suivante :

```
if (condition) then .... 
elseif (condition) then .....
else .....
end if; 
```

Comme vous pouvez le voir, **le "else" ne requiert pas de "then".**

En reprenant notre exemple, nous avons donc

```
x:=10;
if (x<5) then 
        print("Nombre < 5");
elseif (x = 5) then 
	print("Nombre = 5");
else
	print("Nombre > 5");
end if;
```

ISETL ne prenant pas en compte l'indentation, il est aussi possible de rédiger ce code de cette façon :

```
x:=10;
if (x<5) then print("Nombre < 5");
elseif (x = 5) then print("Nombre = 5");
else print("Nombre > 5");
end if;
```

## Rédaction de conditions

Je vous propose un tableau récapitulatif présentant tous les opérateurs nécessaires à la rédaction de conditions en ISETL :

x et y étant des nombres, A ou B étant des propositions.

<table><tbody><tr><td class="has-text-align-center" data-align="center"><strong>Opérateur ISETL</strong></td><td class="has-text-align-center" data-align="center"><strong>Description</strong></td></tr><tr><td class="has-text-align-center" data-align="center">x=y</td><td class="has-text-align-center" data-align="center">x est égal à y</td></tr><tr><td class="has-text-align-center" data-align="center">x\=y</td><td class="has-text-align-center" data-align="center">x n'est pas égal à y</td></tr><tr><td class="has-text-align-center" data-align="center">x&lt;y</td><td class="has-text-align-center" data-align="center">x est inférieur à y</td></tr><tr><td class="has-text-align-center" data-align="center">x&lt;=y</td><td class="has-text-align-center" data-align="center">x est inférieur ou égal à y</td></tr><tr><td class="has-text-align-center" data-align="center">x&gt;y</td><td class="has-text-align-center" data-align="center">x est supérieur à y</td></tr><tr><td class="has-text-align-center" data-align="center">x&gt;=y</td><td class="has-text-align-center" data-align="center">x est supérieur ou égal à y</td></tr><tr><td class="has-text-align-center" data-align="center">A or B</td><td class="has-text-align-center" data-align="center">Disjonction logique : A ou B</td></tr><tr><td class="has-text-align-center" data-align="center">A and B</td><td class="has-text-align-center" data-align="center">Conjonction logique : A et B</td></tr><tr><td class="has-text-align-center" data-align="center">A impl B</td><td class="has-text-align-center" data-align="center">Implication logique : A implique B</td></tr><tr><td class="has-text-align-center" data-align="center">not A</td><td class="has-text-align-center" data-align="center">Négation logique : Non A</td></tr></tbody></table>

Tableau Récapitulatif Opérateurs Logiques ISETL

### Nota Bene

Il faut bien prendre en compte que la condition d'égalité en ISETL **s'écrit avec un seul "égal"** contrairement au python, c++, java.... L'affectation en ISETL étant ":=".

## Plus de tutoriels en ISETL

[ISETL - KeskeC](https://keskec.fr/tag/isetl/)
