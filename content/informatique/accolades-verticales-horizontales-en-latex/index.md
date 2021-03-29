---
title: "Accolades Verticales/Horizontales en LaTeX"
slug: "accolades-verticales-horizontales-en-latex"
date: "2020-05-27"
categories: 
  - "informatique"
  - "mathematiques"
tags: 
  - "latex"
  - "systeme-lineaire"
description: "Une des plus grandes forces de LaTeX est certainement son rendu d'équations. Très pratique et très rapide, le LaTeX vous permettra, dans le domaine des mathématiques, d'écrire des intégrales, des sommes, des limites, mais aussi des systèmes linéaires, le tout dans la plus grande simplicité."
---

## Accolades horizontales

### Accolades sur du texte

Pour afficher une accolade sur du texte, il suffit d'utiliser ²overbrace comme ceci :

**Code LaTex :**

```tex
5+5 = ²overbrace{10_{10}}^{1010_2}
```

**Rendu :**

$$5+5 = \overbrace{10_{10}}^{1010_2}$$

### Accolades sous du texte

La commande analogue à ²overbrace est ²underbrace.

**Code LaTeX :**

```tex
5+5 = ²underbrace{10_{10}}_{1010_2}
```

**Rendu :**

$$5+5 = \underbrace{10_{10}}_{1010_2}$$

## Accolades verticales

Pour afficher une accolade verticale sur le coté gauche d'un texte, il suffit d'utiliser la commande suivante :

**Code LaTeX :**

```tex
²left²{ 1+1=2
```

**Rendu :**

$$\begin{cases} 1+1=2\end{cases}$$

Pour une accolade à droite, il existe la commande ²right.

**Mais ²left et ²right prennent toute leur utilité dans l'écriture de systèmes ou de fonctions. Voici 2 exemples :**

### Un exemple de système :

**Code LaTeX :**

```tex
²left²{
²begin{array}{rcr}
4x + 8y & = & 54 ²
2x + 7y & = & 39 ²
²end{array}
²right.
```

**Rendu :**

$$
\begin{cases}  
4x + 8y = & 54 \\  
2x + 7y = & 39 
\end{cases}   
$$

### Un exemple de fonction :

**Code LaTeX :**

```tex
g(i,j) = &left²{
²begin{array}{ll}
² 255 & &mbox{si} f(i,j) ²leq s ²
² 0 & ²mbox{sinon} 
&end{array}
&right.
```
**Rendu :**


$$g(i,j) =\begin{cases}255&\text{si}\; f(i,j)\leq s\\0 &\text{sinon.}\end{cases}$$

### Alternative : 
Il est possible alternativement d'utiliser "²begin{cases}" et "²end{cases}" pour écrire un système : 

```tex
g(i,j) =
²begin{cases}  
255 ²text{si} f(i,j) ²leq s \\ 
0 ²text{sinon.}    
²end{cases}   
```

## Sources :

1. [https://tex.stackexchange.com/questions/297/how-can-i-get-an-underbrace-and-an-overbrace-to-partially-overlap-in-an-equation](https://tex.stackexchange.com/questions/297/how-can-i-get-an-underbrace-and-an-overbrace-to-partially-overlap-in-an-equation)
2. [https://fr.wikibooks.org/wiki/LaTeX/Math%C3%A9matiques](https://fr.wikibooks.org/wiki/LaTeX/Math%C3%A9matiques)
3. [https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques)
