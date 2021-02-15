---
title: "Partie entière supérieure et inférieure en Latex"
slug: "partie-entiere-superieur-et-inferieur-en-latex"
date: "2020-06-23"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "latex"
description: "Cet article présentera l'utilisation de la partie entière, aussi bien supérieure qu'inférieure en Latex. Deux macros seront explicitées pour faciliter leur utilisation."
---

## Partie entière supérieure en LaTex :



Pour prendre la partie entière supérieure d'un entier $x$ en Latex, il suffit de taper ceci :

```
\lceil x \rceil 
```

Voici le résultat :

$\lceil x \rceil$

## Partie entière inférieure en LaTex :

La partie entière inférieure en Latex d'un entier $x$ se fait de façon analogue à celle supérieure :

```
\lfloor x \rfloor 
```

Voilà son rendu :

$\lfloor x \rfloor$

## Raccourcir son utilisation avec une macro?

Il est possible de faire une macro de la partie entière afin de simplifier son utilisation :

```
\newcommand{\floor}[1]{\lfloor #1 \rfloor}
\newcommand{\ceil}[1]{\lceil #1 \rceil}
```

Il est ainsi possible d'utiliser :

```
\floor{x}
\ceil{x}
```

  
\newcommand{\floor}\[1\]{\lfloor #1 \rfloor}  
\newcommand{\ceil}\[1\]{\lceil #1 \rceil}  
\floor{x} \ceil{x}

Pour raccourcir votre code Latex.

## Intéressé par la création d'accolades en LaTeX ?

Je vous propose mon article sur le sujet :

[Accolades Verticales/Horizontales en LaTeX](https://keskec.fr/sciences/informatique/robin/2530/)
