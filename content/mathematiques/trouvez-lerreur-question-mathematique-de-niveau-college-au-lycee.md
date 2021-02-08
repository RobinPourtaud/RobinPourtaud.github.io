---
title: "Trouvez l'erreur ! Mathématiques Collège-Lycée"
slug: "trouvez-lerreur-question-mathematique-de-niveau-college-au-lycee"
date: "2020-05-09"
categories: 
  - "mathematiques"
  - "sciences"
tags: 
  - "integrale"
  - "jeu"
  - "limite"
  - "lycee"
description: "Tout au long de votre scolarité, vous avez surement dû rencontrer beaucoup d'équations. Vous avez peut-être le sentiment d'être parfaitement capable de résoudre de simples équations du collège ou du lycée ? Et bien vous verrez qu'une erreur est très vite arrivée..."
---

Note : Toutes les variables appartiennent à {{< latex "\mathbb{R}" >}}.

**Solutions à la fin !**

## Niveau 1 : Un bon début !

Ici, chaque ligne correspond à la ligne précédente à laquelle on ajoute ce qui est écrit à sa droite. Surtout, prenez votre temps ! Ce n'est pas un exercice compliqué, rappelez-vous juste de toutes les règles apprises au collège :).



1. {{< latex " a = b " >}}
2. {{< latex "aa = ba " >}} En multipliant par a
3. {{< latex "a^2 - b^2 = ba - b^2" >}} En soustrayant {{< latex "b^2" >}}
4. {{< latex "(a+b)(a-b) = b(a-b)" >}} Identité remarquable : {{< latex " (a+b)(a-b) = a^2 - b^2 " >}}
5. {{< latex "a+b = b" >}} En divisant par {{< latex "(a-b)" >}}
6. {{< latex "b+b = b" >}} En remplaçant {{< latex "a" >}} par {{< latex "b" >}}
7. {{< latex "2b = b" >}}
8. {{< latex "2 = 1" >}} En divisant par b

Avez-vous trouvé l'erreur ?

## Niveau 2 : Racine carré

Selon le théorème de Pythagore, dans un triangle rectangle, le carré de l'hypothénuse est égale au carré de ses 2 autres cotés ({{< latex "a^2+b^2 = c^2" >}}). Ce n'est pas le sujet :). Pour ne pas vous faire piéger, **ne pensez pas à ce théorème !**

1. {{< latex "a^2 + b^2 = 9" >}}
2. {{< latex "\sqrt{a^2+b^2}=3" >}} Racine carré de 9
3. Si a = 0
4. {{< latex "\sqrt{0^2+b^2}=3" >}}
5. {{< latex "\sqrt{b^2}=3" >}}
6. {{< latex "b=3" >}}

Alors :) ? Il y a eu 1 erreur reproduite 2 fois. Laquelle est-ce?

## Niveau 3 : Équation du second degré

Un niveau de première **n'est pas** requis pour **résoudre** l'équation ci-dessous, voilà votre indice.

1. {{< latex "\frac{x+1}{x^2-1} = 3" >}}
2. {{< latex "x+1 = 3 \times (x^2 - 1)" >}}
3. {{< latex "3x^2-x-4 = 0" >}} <-Formule de résolution des équations de second degré
4. {{< latex "x_{1,2} = \frac{1\pm\sqrt{49}}{6}" >}}
5. {{< latex "x_{1,2}=\{-1,\frac{4}{3}\}" >}}

Un détail ne vous chagrine pas?

## Niveau 4 : Intégrale simple

Pour celle-ci, un niveau terminal est requis, mais cela reste une équation très simple !

{{< latex "\int x dx = \frac{x^2}{2}" >}}

Une ligne, une erreur... **non négligeable** !

## Niveau 5 : Limite

Si vous connaissez votre cours de math de 1ère , il ne devrait y avoir aucun soucis :)

{{< latex "\lim\limits_{\substack{n \to \infty}}(1+\frac{1}{n})^n" >}}

Comme {{< latex "\lim\limits_{\substack{n \to \infty}} (1 + \frac{1}{n}) = 1" >}}

Et : {{< latex "\lim\limits_{\substack{n \to \infty}} n = \infty" >}}

{{< latex "\lim\limits_{\substack{n \to \infty}}(1+\frac{1}{n})^n = 1^\infty = 1" >}}

Logique non :) ?

## Solution :

### Niveau 1 :

{{< latex "a=b" >}} donc {{< latex "a-b=0" >}}. Or, on ne peut pas diviser par 0 ! Erreur à la ligne 5

### Niveau 2 :

Pour rappel : {{< latex "\sqrt{9} = 3" >}} mais aussi {{< latex "\sqrt{9}=-3" >}} ! Erreur donc à la ligne 1 et la ligne 5. {{< latex "b=\{3,-3\}" >}}

### Niveau 3 :

La division par 0 ! Même problème que pour le niveau 1 mais un peu plus subtile :). -1 n'est donc pas solution de l'équation car {{< latex "(-1)^2-1=0" >}}.

De plus, l'utilisation de formules pour le second degrés n'était pas nécessaire ! Ne voyez-vous pas une identité remarquable ^^.

### Niveau 4 :

\+ C!! Evidemment. N'oubliez jamais cette constante, sinon votre résultat sera tout simplement faux. Pour rappel, la dérivé d'une constante est égale à 0. Ainsi, il n'est pas impossible que votre primitive possédait une constante :).

Pour vous remémorer de nombreuses notions sur les intégrales tel que l'intégration par partie ou le changement de variable, je vous renvois vers mon article :

[L’intégrale de x^i dx](https://keskec.fr/sciences/mathematiques/robin/220/)

En bonus, l'utilisation des nombres complexes :).

### Niveau 5 :

Trouvez manuellement le vrai résultat de cette limite est plus compliqué. Mais c'est une formule très connue, vous avez sans doute déjà dû la voir dans un livre de première :

{{< latex "\lim\limits_{\substack{n \to \infty}}(1+\frac{1}{n})^n = e" >}}

En revanche, même sans connaitre cette formule, vous auriez dû repérer la forme indéterminée : {{< latex "1^\infty" >}}. Si vous (comme moi avant) ne saviez pas pourquoi {{< latex "1^\infty\neq 1" >}} dans tout les cas, maintenant vous avez un parfait contre-exemple:).

Pour information : pour résoudre cette limite, il faut utiliser une notion appelée **le développement limité**, notion qui est étudiée après le lycée... 2 liens pour en savoir plus !

- [https://fr.wikipedia.org/wiki/D%C3%A9veloppement_limit%C3%A9](https://fr.wikipedia.org/wiki/D%C3%A9veloppement_limit%C3%A9)
- [https://math.unice.fr/~frapetti/analyse/FormulaireDL.pdf](https://math.unice.fr/~frapetti/analyse/FormulaireDL.pdf)
