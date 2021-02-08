---
title: "Différents types d'automates finis"
slug: "vocabulaire-sur-les-automates-finis"
date: "2020-12-11"
categories: 
  - "informatique"
tags: 
  - "automate"
  - "graphe"
no: ""
---

Cet article présente un ensemble de propriétés concernant les automates finis. Pour mieux comprendre ces définitions, chaque type d'AFN sera illustré d'exemples générés grâce au logiciel Jflap. Les définitions formelles ne sont pas explicitées dans cet article mais sont disponibles via les liens sources.

## Définitions :

### Automate déterministe

Un automate est dit déterministe si il respecte trois conditions :

1. Il possède un unique état initial.
2. Il ne possède pas d'epsilon-transitions.
3. Pour chaque état de cet automate, il existe au maximum une transition issue de cet état possédant le même symbole.

![](images/image-1-edited.png) 

N'est pas un AFD

Attention : Un automate fini est toujours un AFN (automate fini non déterministe). Un automate fini déterministe (AFD) est un AFN particulier.

### Automate complet

Un automate fini est dit complet si :

1. Depuis n'importe quel état, tous les symboles de l'alphabet doivent appartenir au moins une fois aux transitions (sortantes).

Par exemple pour l'alphabet {a,b,c} :

![](images/image-12.png)

Automate fini non complet

Cet automate n'est pas complet car on ne peut pas obtenir le symbole "a" depuis q2.

Pour obtenir un automate équivalent, complet, il suffit de créer un état "puits", ou état "poubelle". Comme suit :

![](images/image-14.png)

Automate fini complet

### Automate émondé

Un automate est dit émondé (ou utile) si tous les états de cet automate peuvent former au moins un mot du langage.

Par exemple : Cet automate est fini émondé. q0, q1 et q3 peuvent servir tous les 3 à la création du langage.

![](images/image-6.png)

Automate fini émondé

Cependant celui là ne l'est pas : l'état q1 n'est plus "utile".

![](images/image-7.png)

Automate non émondé

### Automate unitaire

Un automate est dit unitaire si il possède un unique état initial.

![](images/image.png)

Automate unitaire

### Automate standard

Un automate est dit standard si :

1. Il est unitaire (un seul état initial)
2. Il n'existe pas de transitions allant sur cet état initial

Par exemple, ceci n'est pas un automate standard :

![](images/image-8-1024x317.png)

Automate non standard

Mais celui là l'est :

![](images/image-9-1024x282.png)

Automate standard

### Automate normalisé

Un automate est dit normalisé si :

1. Il est standard (aucune transition vers l'unique état initial).
2. Il possède un unique état final
3. Aucune transition n'a pour origine l'état final (on ne peut pas en sortir).

Par exemple cet automate n'est pas normalisé :

![](images/image-10-1024x676.png)

Automate non-normalisé

Cet automate est normalisé :

![](images/image-11-1024x654.png)

Automate normalisé

## Sources :

1. [Deterministic finite automaton - Wikipédia](https://en.wikipedia.org/wiki/Deterministic_finite_automaton)
2. [Nondeterministic finite automaton - Wikipédia](https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton)
3. [automate normalisé - math.cheredeprince.net](https://math.cheredeprince.net/elt/automate_normalise#!aside=opened&elts=set:automate_normalise,1)
4. [séquence 209_5_7 - desmontils.net](http://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_7.htm)
5. [Automate déterministe - momirandum.com](http://www.momirandum.com/automates-finis/Automatedeterministe.html)
6. [Automate standard - momirandum.com](http://www.momirandum.com/automates-finis/Automatestandard.html)
7. [Complétion - Etat poubelle](http://www.momirandum.com/automates-finis/CompletionEtatpoubelle.html)
