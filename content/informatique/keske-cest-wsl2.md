---
title: "Wsl2"
slug: "keske-cest-wsl2"
date: "2020-04-11"
categories: 
  - "informatique"
tags: 
  - "linux"
  - "tuto"
  - "windows-10"
  - "wsl2"
description: "Vous souhaitez savoir comment installer Windows Subsystem for Linux 2 ? Et utiliser Debian ou Ubuntu comme distribution ? Voici un article pour vous guider."
---

> **Windows Subsystem for Linux (WSL)** est une couche de compatibilité permettant d'exécuter des [exécutables binaires](https://fr.wikipedia.org/wiki/Fichier_ex%C3%A9cutable) [Linux](https://fr.wikipedia.org/wiki/Linux) (au format [ELF](https://fr.wikipedia.org/wiki/Executable_and_Linkable_Format)) de manière native sur [Windows 10](https://fr.wikipedia.org/wiki/Windows_10) et [Windows Server 2019](https://fr.wikipedia.org/wiki/Windows_Server_2019).
> 
> [fr.wikipedia.org](https://fr.wikipedia.org/wiki/Windows_Subsystem_for_Linux)

En mai 2019, Microsoft lance WSL2, une mise à jours de WSL proposant de nombreuses nouveautés.

Parmi celles-ci, on retrouve:

- La présence d'un vrai noyau Linux au sein de Windows
- Un temps d'accès réduit
- Un accès et une modification des fichiers plus fluides
- Un accès à internet et des ports plus rapide et intrinsèque à Windows

## Wsl, bénéfice?

Concrètement, WSL nous offre un accès à un système Linux à l'intérieur de Windows via un terminal. Cela implique donc que toute application Linux sera maintenant exécutable depuis Windows 10.

## Nécessaire à l'installation:

- Windows 10 builds 18917 ou plus (commande "winver" pour vérifier).
- 30 min de votre temps :).

## Installation:

### Installation de WSL:

D'abord, ouvrez le terminal PowerShell en Administrateur et tapez la commande:

```
Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Windows-Subsystem-Linux
```

Ensuite, redémarrez l'ordinateur.

### Activer la Machine Virtuel Windows

Aussi avec le terminal PowerShell en Administrateur, tapez la commande suivante:

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

puis:

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

Redémarrez l'ordinateur.

### Installer la distribution Linux de votre choix

Vous pouvez maintenant installer la distribution Linux souhaitée, [Ubuntu](https://www.microsoft.com/fr-fr/p/ubuntu/9nblggh4msv6?activetab=pivot:overviewtab), [Debian](https://www.microsoft.com/fr-fr/p/debian/9msvkqc78pk6?activetab=pivot:overviewtab)....

Vous avez juste à cliquer sur "Installer".

Puis, suite au téléchargement, "ouvrez" la distribution choisie.

Patientez un peu, puis choisissez un nom d'utilisateur UNIX et un mot de passe, sachant que ceux-ci peuvent être différents de vos identifiants Windows.

Vous avez maintenant accès à un vrai terminal Linux sous Windows.... sous WSL1.

![](images/Capture-1-1024x523.png)

Windows Subsystem for Linux

### Passer de WSL1 à WSL2

Pour passer votre distribution de WSL1 à WSL2, il suffit d'abord de taper la commande suivante dans le terminal powershell:

```
wsl --set-version <Distro> 2
```

Ensuite, remplacez <Distro> par le nom de votre distribution

```
wsl --set-version 2
```

Si vous souhaitez que toutes vos futures distributions soit sous WSL2 par défaut...

La commande ci-dessous vous permet également de lister les noms des distribution Linux si besoin.

```
wsl -l
```

Vous avez enfin un système Linux opérationnel :).

### Petit + : Le nouveau Terminal Windows

Vous pouvez télécharger le nouveau terminal Windows à l'adresse suivante:

[https://www.microsoft.com/fr-fr/p/windows-terminal-preview/9n0dx20hk701?activetab=pivot:overviewtab](https://www.microsoft.com/fr-fr/p/windows-terminal-preview/9n0dx20hk701?activetab=pivot:overviewtab)

https://www.youtube.com/watch?v=8gw0rXPMMPE

## Sources:

- [https://docs.microsoft.com/en-us/windows/wsl/wsl2-install](https://docs.microsoft.com/en-us/windows/wsl/wsl2-install)
- [https://howto.lintel.in/wsl-vs-wsl-2-performance/](https://howto.lintel.in/wsl-vs-wsl-2-performance/)
- [https://devblogs.microsoft.com/commandline/wsl2-will-be-generally-available-in-windows-10-version-2004/](https://devblogs.microsoft.com/commandline/wsl2-will-be-generally-available-in-windows-10-version-2004/)
