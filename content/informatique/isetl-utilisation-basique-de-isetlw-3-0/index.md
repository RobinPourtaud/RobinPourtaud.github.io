---
title: "ISETL - Utilisation basique de ISETLW 3.0"
slug: "isetl-utilisation-basique-de-isetlw-3-0"
date: "2020-07-22"
categories: 
  - "informatique"
tags: 
  - "isetl"
  
description: "Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, elle avait pour finalité l’enseignement des mathématiques discrètes à l’université. Cet article a pour but de vous présenter comment exécuter du code via le logiciel ISETLW 3.0 sur Windows 10."
---
## Nécessaire :

Pour pouvoir suivre ce tutoriel, il est nécessaire d'avoir accès au logiciel ISETLW 3.0 sur Windows. Pour cela, vous pouvez vous référer à mon précédent article sur son installation : [ISETL 3.0 sur Windows 10](/informatique/installer-isetl)

## Utilisation de la console :

### Utilisation habituelle :

Au démarrage de ISETLW, la console ISETL s'ouvrira par défaut :

![Console ISETLW 3.0](image-6-1024x624.png#t5)



Vous pouvez directement taper les commandes que vous souhaitez et appuyer sur "Entrer".  
Sachez que vous pouvez aussi créer des fonctions, des boucles ou des conditions sans quitter le terminal. L'indentation se fera automatiquement, comme le montre le screen ci-dessous :

![Utilisation de la console](image-7.png#t4)



### Effacer la console :

Pour effacer la console, vous pouvez cliquer sur le menu "Windows" puis "Erase this Window".

![Erase this Window](image-9.png#t4)



### Erreurs fréquentes :

Si vous oubliez un ";", sachez qu'il est toujours possible de le rentrer à la ligne suivante :

![](image-8.png#t4)

## Utilisation plus confortable :

ISETLW 3.0, n'est pas un logiciel très "User-Friendly". Cependant, il est possible d'améliorer légèrement son utilisation en 3 étapes:

### Étape 1 : Réduire "Graph Window"

Commencez par mettre en cascade ISETL, pour cela appuyez sur "Window" puis "Cascade".

Ensuite réduisez la fenêtre "Graph Windows" :

![Réduction de graph Window](image-10-1024x211.png#t5)



### Étape 2 : Ouvrir un nouveau document

Appuyez sur "File" puis "New".

### Étape 3 : Redimensionnez l'affichage

Vous pouvez maintenant cliquer sur "Window" puis "Tile Horizontally" ou "Tile Vertically" selon vos préférences :

![Affichage fragmenté ISETLW 3.0](image-11-1024x643.png#t5)


## Utilisation du "Text Window" :

Je vous propose de tester avec une petite fonction tirée d'un [précédent tutoriel](/informatique/isetl-fonction-mathematiques) sur les fonctions en ISETL :

```php
somme:=func(e);
local x;
if (#e = 1) then return arb(e);
 else
  take x from e;
  return x + somme(e);
end if;
end func;

somme({8,6,9});
```

Collez cette fonction (ou votre code) dans la fenêtre "Text Window", et selectionnez tout ce code comme sur le screenshot suivant :

![Texte Sélectionné ISETLW 3.0](image-12-1024x636.png#t5)



Une fois sélectionné, vous pouvez cliquer sur le feu vert :

![Texte éxécuté ISETLW 3.0](image-13-1024x650.png#t5)



Vous pouvez bien-sûr sauvegarder ce document grâce à la disquette !

Dans le cas où votre exécution se passerait mal, vous pouvez toujours cliquer sur le "feu rouge".

Vous pouvez maintenant utiliser ce petit logiciel normalement sans trop de problèmes :).

