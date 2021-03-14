---
title: "ISETL - Syntaxe des fonctions"
slug: "isetl-syntaxe-des-fonctions"
date: "2020-07-24"
categories: 
  - "informatique"
tags: 
  - "isetl"
  - "tuto"
description: "Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité **l’enseignement des mathématiques discrètes à l’université**. Possédant une syntaxe atypique, ISETL est un langage difficile à appréhender pour un néophyte. Dans ce tutoriel, nous introduirons le concept de fonction en ISETL, partant d'une définition générale puis en prenant 3 exemples."
---
## Fonction en ISETL

### Définition :

Comme dans d'autres langages de programmation, une fonction dans ISETL est une entité informatique permettant l'encapsulation d'une partie de code. Elle peut prendre zéro, une ou plusieurs entrées et retourne une valeur (ou non, on parlera alors de procédures).

### La syntaxe :

En ISETL, la syntaxe des fonctions ne repose pas sur l'indentation, ni sur des accolades :  
Une fonction commence par **func();** et se fini par **end func();**. Ainsi :

```
VotreFonction := func(param1);
return param1;
end func; 
```

Pour exécuter cette fonction avec le paramètre 5 :

```
VotreFonction(5);
```

Vous devriez voir sur le terminal d'exécution affiché "5;".

![](image-5.png)

ISETL - Syntaxe d'une fonction

## Exemples de fonctions

### Exemple 1 :



On souhaite créer une fonction retournant **le produit cartésien de 2 ensembles**.

On appelle produit cartésien de 2 ensembles $e_1$ et $e_2$, l'ensemble des couples (i,j) tel que $i\in e_1$ et $j\in e_2$ .

Si $e_1 = \\{x,y\\}$ et $e_2 = \\{1,2\\}$, alors $e_1\times e_2 = \\{(x,1);(x,2);(y,1);(y,2)\\}$.

Nous avons donc :

```
cartesien := func(e1,e2);
return {[x,y]:x in e1, y in e2};
end func;
```

La deuxième ligne se lit comme "retourner l'ensemble de tous les couples (x,y) tel que x appartient à e1 et y à e2".

### Exemple 2 :

Pour ce deuxième exemple, nous souhaitons prendre la somme de tous les éléments d'un ensemble mais de **façon récursive**.

Par exemple pour l'ensemble {1,2,3}, nous souhaitons retourner 6.

Je vous propose une fonction (plus complexe que nécessaire) pour vous familiariser avec la syntaxe ISETL.

```
somme:=func(e);
local x;
if (#e = 1) then return arb(e);
else
  take x from e;
  return x + somme(e);
end if;
end func;
```

_Note : "#e" est le cardinal de e, "arb(e)" est un nombre arbitraire contenu dans e, "take x from e" permet de retirer une valeur de e et de la stocker dans une variable x._

Comme escompté :

```
somme({8,6,9});
```

retourne "23;".

## Plus de tutoriels sur ISETL ici :

[Article sur ISETL de KeskeC](https://keskec.fr/tag/isetl/)
