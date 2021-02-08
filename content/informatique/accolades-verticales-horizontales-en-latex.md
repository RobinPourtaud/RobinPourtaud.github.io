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
no: ""
---

Une des plus grandes forces de LaTeX est certainement **son rendu d'équations**. Très pratique et très rapide, le LaTeX vous permettra, dans le domaine des mathématiques, d'écrire des intégrales, des sommes, des limites, mais aussi **des systèmes linéaires**, le tout dans la plus grande simplicité.  
Faut-il encore savoir le faire... 

\[latexpage\]

## Accolades horizontales

### Accolades sur du texte

Pour afficher une accolade sur du texte, il suffit d'utiliser \\overbrace comme ceci :

**Code LaTex :**

```
5+5 = \overbrace{10_{10}}^{1010_2}
```

**Rendu :**

$5+5 = \\overbrace{10\_{10}}^{1010\_2}$

### Accolades sous du texte

La commande analogue à \\overbrace est \\underbrace.

**Code LaTeX :**

```
5+5 = \underbrace{10_{10}}_{1010_2}
```

**Rendu :**

$5+5 = \\underbrace{10\_{10}}\_{1010\_2}$

## Accolades verticales

Pour afficher une accolade verticale sur le coté gauche d'un texte, il suffit d'utiliser la commande suivante :

**Code LaTeX :**

```
\left\{ 1+1=2
```

**Rendu :**

$\\left\\{ 1+1=2$

Pour une accolade à droite, il existe la commande \\right.

**Mais \\left et \\right prennent toute leur utilité dans l'écriture de systèmes ou de fonctions. Voici 2 exemples :**

### Un exemple de système :

**Code LaTeX :**

```
\left\{
\begin{array}{rcr}
4x + 8y & = & 54 \\
2x + 7y & = & 39 \\
\end{array}
\right.
```

**Rendu :**

$\\left\\{  
\\begin{array}{rcr}  
4x + 8y & = & 54 \\\\  
2x + 7y & = & 39 \\\\  
\\end{array}  
\\right.  
$

### Un exemple de fonction :

**Code LaTeX :**

```
g(i,j) = \left\{
\begin{array}{ll}
\ 255 & \mbox{si } f(i,j) \leq s \
\ 0 & \mbox{sinon} 
\end{array}
\right.
```

**Rendu :**

$  
g(i,j) = \\left\\{  
\\begin{array}{ll}  
\\255 & \\mbox{si } f(i,j) \\leq s \\  
\\0 & \\mbox{sinon.}  
\\end{array}  
\\right.  
$

## Sources :

1. [https://tex.stackexchange.com/questions/297/how-can-i-get-an-underbrace-and-an-overbrace-to-partially-overlap-in-an-equation](https://tex.stackexchange.com/questions/297/how-can-i-get-an-underbrace-and-an-overbrace-to-partially-overlap-in-an-equation)
2. [https://fr.wikibooks.org/wiki/LaTeX/Math%C3%A9matiques](https://fr.wikibooks.org/wiki/LaTeX/Math%C3%A9matiques)
3. [https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire\_des\_math%C3%A9matiques](https://fr.wikibooks.org/wiki/LaTeX/%C3%89crire_des_math%C3%A9matiques)
