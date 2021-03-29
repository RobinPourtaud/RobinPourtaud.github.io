---
title: "ISETL 3.0 sur Windows 10"
slug: "installer-isetl"
date: "2020-06-03"
categories: 
  - "informatique"
tags: 
  - "isetl"
  - "ms-dos"
  - "windows-10"
description: "Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, elle avait pour finalité l'enseignement des mathématiques discrètes à l'université."
---
En 1985, SETL était devenu un projet très lourd, lent et nécessitait une compilation, ce qui le rendait difficilement utilisable. C'est dans ce contexte que Gary Levin décida de créer une version de SETL interactive à direction des universités.  
Et c'est ainsi qu'en 1988 sortit la version 1.0 d'ISETL : **plus rapide**, **plus léger** (<250K), et ayant une **syntaxe très proche de celle de SETL**. (source 1)

Il est extrêmement complexe de se procurer des informations utiles sur ISETL en 2020. **Désuet** et complexe à appréhender, il est malgré tout encore enseigné dans certaines universités dans le cadre d'une introduction à la théorie des ensembles.

Dans cet article, je vais vous montrer comment installer ISETL sur Windows 10. Vous verrez par la suite comment utiliser ISETL sur d'autres systèmes d’exploitation en utilisant un émulateur MS-DOS !

## Installation :

Dans le cas où les fichiers ne seraient plus disponibles, vous pouvez les retrouver sur [Github](https://github.com/KeskeC/ISETL).

### Compatible ?

Au moment où je rédige cet article, je suis sur Windows 10 version 2004, il se peut que de futures mises à jour de Windows rendent ce "vieux programme" inutilisable.

![Windows 10 version 2004](image.png#t4)



_Info : pour connaitre rapidement votre version de Windows : Win + R et tapez "winver"._

Dans le pire cas, je peux vous proposer d'utiliser une ancienne version de Windows grâce à une machine virtuelle (HyperV, vmWare, VirtualBox...).

## Téléchargement :

Malencontreusement, le site web officiel d'ISETL n'est plus accessible en ligne et n'est absolument plus mis à jour. En revanche, il est tout à fait possible de le retrouver archivé sur [Wayback Machine](https://web.archive.org/web/20070411084445/http://csis03.muc.edu/isetlw/isetlw.htm).

Il n'est pas nécessaire de cliquer, je vous propose de télécharger le fichier juste ici : [Télécharger IsetlW](https://keskec.fr/wp-content/uploads/2020/06/ISETLW.zip)

À l'intérieur de l'archive, vous trouverez un fichier exécutable. Extrayez-le et exécutez-le. Vous pourrez maintenant interpréter du ISETL sur Windows 10 !

![ISETLW 3.0](image-1-1024x573.png#t4)



## La version MS-DOS :

Si vous voulez utiliser ISETL avec un terminal, sachez que vous pouvez utiliser la version MS-DOS d’ISETL. En effet, avant de posséder une interface graphique, ce programme était uniquement utilisé via un terminal.

Seulement, en 2020, exécuter un logiciel MS-DOS en 16-bit peut poser problème. Avec un ordinateur Windows en 32-bit, il était possible d'exécuter des programmes MS-DOS 16-bit en natif. Ce n'est "malheureusement" plus cas depuis Windows 10 en 64-bit.

### Emulateur MS-DOS

Il va donc falloir installer un émulateur MS-DOS pour pouvoir faire tourner ce programme. Je vous propose 4 alternatives mais il y en a évidement bien d'autres :

- [vDos](https://www.vdos.info/index.html) pour Windows 10
- [MS-DOS](https://copy.sh/v86/?profile=msdos) sur le web
- [DOSBox](https://la-vache-libre.org/dosbox-tatez-du-ms-dos-sous-gnulinux/) pour Linux
- [DOSBox](https://play.google.com/store/apps/details?id=bruenor.magicbox.free&hl=fr) pour Android

Je vais continuer les explications avec vDos pour Windows 10. Vous pouvez d'ailleurs le télécharger ici : [vDos.zip](https://www.vdos.info/download.html)

Je vous laisse l'installer en gardant bien en tête l'endroit où il sera stocké (le garder à la racine est conseillé).

### Télécharger ISETL3.0 pour MS-DOS

Vous pouvez télécharger la version MS-DOS juste ici : [ISETL3.0 MS-DOS](https://github.com/KeskeC/ISETL/tree/master/ISETL-DOS)

Je vous laisse extraire le fichier dans le dossier d'installation de vDos pour pouvoir l'exécuter sans se soucier de sa possession dans votre ordinateur.

Par défaut : C:\vDos

### Exectuter ISETL grâce à vDos

Ouvre et modifier le fichier "autoexec.txt" comme ceci :

```batch
rem This is essentially the DOS autoexec.bat.
rem =========================================

rem At startup, C: is the only drive letter known by vDos.
rem But this vDos C: is NOT Windows C: !!!

rem vDos drive letters don't have to match those of Windows.
rem It's even adviced they don't, to limit access to the Windows file system.

rem The USE command assigns vDos drive letters to Windows drives, folders,
rem or network shares. The command syntax is:
rem USE <vDos drive letter:> <Windows drive:|folder|network share>\
rem Examples: USE C: D:\dosprog\, USE F: \server\share\dosprog\.

rem By default C: is assigned to the folder vDos.exe is started from.
rem Execute the batch file that launches the DataPerfect demo program:
CALL ISETL.EXE

@ECHO OFF
rem The demo program was closed, and we return here.
rem Eventually add EXIT to close the vDos window.
```

Sauvegardez le fichier.

Vous pouvez enfin exécuter "vDos.exe". Constatez que tout fonctionne comme prévu !

![ISETL 3.0 MS-DOS](image-2-1024x658.png#t4)


## Sources :

1. [Isetl for Mathematics](http://www.math.bas.bg/softeng/bantchev/place/setl/isetl-for-mathematics.pdf)
2. [ISETL - Site Officiel - Web.archive.org](https://web.archive.org/web/20070411084445/http://csis03.muc.edu/isetlw/isetlw.htm)
3. [Learning Discrete Mathematics with ISETL - Google Book](https://books.google.fr/books?id=DBzSBwAAQBAJ&lpg=PA4&ots=Mzph34QZDQ&dq=isetl&hl=fr&pg=PR1#v=onepage&q&f=false)
