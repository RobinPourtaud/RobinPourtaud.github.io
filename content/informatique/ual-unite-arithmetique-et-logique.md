---
title: "UAL - Unité arithmétique et logique"
slug: "ual-unite-arithmetique-et-logique"
date: "2020-12-27"
categories: 
  - "informatique"
tags: 
  - "bit"
  - "logique"
  - "processeur"
no: ""
---

Une unité arithmétique et logique (UAL) ou ALU en anglais est un composant essentiel au fonctionnement de nos ordinateurs actuels. Souvent intégrée au processeur pour effectuer de nombreuses opérations arithmétiques, cet article en présente un exemple simple, conçu avec le logiciel Logisim.

## Caractéristiques de l'UAL :

Notre UAL nous permet d'effectuer 7 opérations sur des entiers signés de 8 bits.

### Entrées :

Notre UAL prend 3 entrées :

1. Un nombre sur 8 bits "A" utilisé en entrée des opérations.
2. Un nombre sur 8 bits "B" utilisé en entrée des opérations.
3. Un nombre sur 3 bits "ctr" utilisé pour sélectionner l'opération désirée.

### Sorties :

Notre UAL possède 2 sorties :

1. Un nombre sur 8 bits étant le résultat de l'opération choisie.
2. Un nombre sur 4 bits présentant chaque flag.

### Opérations :

Notre UAL peut nous autoriser à effectuer 8 opérations. Nous nous servirons uniquement de 7 d'entre elles :

0. ctr = 000 : Addition
1. ctr = 001 : Soustraction
2. ctr = 010 : OU bit à bit
3. ctr = 011 : Et bit à bit
4. ctr = 100 : Non bit à bit
5. ctr = 101 : Décalage à gauche logique
6. ctr = 110 : Décalage à droite logique

![](images/image-30-1024x667.png)

Opérations - UAL

Les opérations "non" et les 2 décalages se servent uniquement du premier nombre "A". C+ et C- sont les carrys de l'addition et de la soustraction.

## Flags :

![](images/image-23.png)

4 bits Flags

Notre sortie flags est représentée par un 4 bit correspondant respectivement à CF, ZF, SF et OF.

### Carry Flag (CF) :

**Commentaire :** Dans le cadre d'additions et de soustractions sur des nombres signés, le carry flag ne pourra **jamais** être égal à 1. Vous pouvez donc relier le bit CF à "0".  
Cependant, dans le cadre de ce tutoriel, le circuit restera explicité :

- c+ est le carry de l'opération 000 (addition)
- c- est le carry de l'opération 001 (soustraction)

![](images/image-24.png)

Carry Flag

- Si ctr = 000, alors CF = c+
- Si ctr = 001, alors CF = c-
- Sinon CF = 0

### Zéro Flag (ZF) :

Le zéro flag est égal à 1 si et seulement si tous les bits de S sont égaux à 0 :

![](images/image-25.png)

Zero Flag



Autrement dit : {{< latex "ZF = \overline{S_0+S_1+S_2+S_3+S_4+S_5+S_6+S_7}" >}}

### Sign Flag (SF) :

SF correspond au signe de S. Si S négatif, alors S = 1, sinon S=0.

Autrement dit : {{< latex "SF = S_7" >}}

![](images/image-26.png)

Sign Flag

### Overflow Flag (OF) :

L'overflow flag est égal à 1 dans 4 cas différent:

1. Pour une addition : Si un positif + un positif = un négatif
2. Pour une addition : Si un négatif + un négatif = un positif
3. Pour une soustraction : Si un négatif - un positif = un positif
4. Pour une soustraction : Si un positif - un négatif = un négatif

Dans les autres cas : OF = 0.

- S A est le signe de A
- S B est le signe de B
- SF est le signe de S

![](images/image-28.png)

Overflow Flag

Autrement dit :

- {{< latex "OF+ = SA.SB.\overline{SF}+\overline{SA}.\overline{SB}.SF" >}}
- {{< latex "OF- = SA.\overline{SB}.\overline{SF}+\overline{SA}.SB.SF" >}}
- OF = OF+ si ctr = 000, OF- si ctr = 001, 0 sinon.

## Mention :

Cette unité arithmétique et logique a été conçu dans le cadre d'un projet d'informatique en collaboration avec [Mr Lucas Lelièvre](https://www.linkedin.com/in/lucas-leli%C3%A8vre-b30990151/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_top%3BQjKA%2FeL3SlC434krJot2NQ%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_search_srp_top-search_srp_result&lici=R3L0SBS2RwyBRO8CpE9SBA%3D%3D) que je remercie.
