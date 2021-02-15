---
title: "Octet, Giga-bits, Kibioctets, Byte ?"
slug: "kilo-octets-kilo-bits-kibioctets-byte-quelles-differences-pour-quelle-utilitee"
date: "2020-06-01"
categories: 
  - "informatique"
tags: 
  - "bit"
  - "conversion"
description: "Durant votre vie numérique, vous avez sans doute rencontré de nombreux acronymes. Des Kbit ? Des To? Voir même de Gio ?  "
---
Savoir combien de films votre clé USB peut stocker, ce n'est pas inné, ça s'apprend, et c'est ce que je vais vous expliquer à travers cet article :).

## Le système international d'unité (SI)



Au lycée, vous avez certainement entendu parler du **système international d'unité**.  
Il s'agit d'un système décimal, permettant de conformer les unités avec précision pour tous les pays du monde (sauf exceptions). Le changement d’échelle se fait par puissance de 10.

Par exemple : 1 km = 1 kilomètre ou 10 hectomètre ou 100 décamètres, mais encore 1000 mètre. Le mètre étant l'unité utilisé pour mesurer des distances. De la même façon, on peut se servir du gramme pour mesurer la masse, le Watt pour la puissance, le joule pour l'énergie, alors pourquoi ne pas faire la même chose pour les données :).

  
Pour une vision plus globale de la chose, je vous propose un tableau présentant quelques préfixes utilisés pour respecter les standards du système internationales :

| Préfixe | Symbole | Valeur |
|--- |--- |--- |
| (aucun) | unité | $10^0$ |
| déca- | da | $10^1$ |
| hecto- | h | $10^2$ |
| kilo- | k | $10^3$ |
| méga- | M | $10^6$ |
| giga- | G | $10^9$ |
| téra- | T | $10^{11}$ |

Quelques préfixes SI couramment utilisés

Voyons maintenant les unités employées pour **la quantification de données.**

## Le bit

Le bit représente **la plus petite unité utilisée** pour quantifier une donnée. Elle peut adopter 2 valeurs, soit un 0, soit un 1. En utilisant ainsi la base 2, on peut créer différents nombres décimaux. Par exemple [en convertissant](https://keskec.fr/sciences/informatique/robin/267/) :

- 00 en binaire vaut 0 en décimal
- 01 en binaire vaut 1 en décimal
- 10 en binaire vaut 2 en décimal
- 11 en binaire vaut 3 en décimal

Avec 2 bits, on peut créer 3 valeurs. Avec 8 bits, on peut en créer $2^8$ valeurs, soit 256 valeurs.

_Pour la petite info : les pixels des écrans super VGA étaient codés sur 8 bits, ils pouvaient donc afficher 256 couleurs... Pour les écrans actuels, le triplet Rouge Vert Bleu codé est devenu la norme, chaque nuance de couleurs codé sur 8 bits chacun. Ce qui fait donc $2^{3 \times 8}=2^{24}=16777216$ couleurs différentes.  
Il existe des exceptions, comme certains écrans OLED de LG, qui ont fait le choix d'ajouter un pixel blanc : WRGB._

Je vous propose un tableau usuel récapitulatif du bit selon le système internationale d'unité :

| Unité | Notation | Valeur |
|--- |--- |--- |
| bit | bit | $10^0 $ |
| kilobit | kbit/kb | $10^3$ |
| mégabit | Mbit/Mb | $10^6$ |
| gigabit | Gbit/Gb | $10^9$ |
| térabit | Tbit | $10^{12}$ |
| pétabit | Pbit | $10^{15}$ |
| exabit | Ebit | $10^{18}$ |
| zettabit | Zbit | $10^{21}$ |
| yottabit | Ybit | $10^{24}$ |

Le bit du SI

Par exemple : 1kbit = 1000 bits

## L'octe = byte ? (non)

### L'octet

**Un octet est un "groupement" de 8 bits.** Par exemple 01101001 est un octet.

En reprenant mon paragraphe précédent, 8 bits, donc un octet peut prendre 256 valeurs distinctes (de 0 à 255).

Dans le langage courant, on entendra fréquemment l'idée qu'**un octet = un byte**, mais ce **n'est pas la même chose** !

### Le byte

**Un byte est la plus petite unité adressable logiquement par un processeur.** Autrement dit, le processeur traitera l'information par petit paquet de bits **de mêmes tailles**. Comme pour le langage humain, la phrase "Je mange des pâtes" a plus de sens que "J e m a n g e d e s p â t e s". L'humain à besoin de mots, le processeur de bytes.

### La nuance entre les deux :

Usuellement, un byte est un groupement de 8 bits. Ainsi, usuellement, 1 byte = 1 octet. La confusion se fait donc d'elle-même. Mais comme expliqué précédemment, un byte n'est pas forcément défini par une taille !  
Par exemple pour certains vieux processeurs, 1 byte = 4 bits.

Vous verrez certainement souvent cette confusion. Dans la majorité des cas, cela ne posera sans doute aucun problème. Par convention, il serait malgré tout préférable d'utiliser le mot octet par défaut, et le mot byte uniquement dans le bon contexte (en temps que "groupement" de bits).

Je vous propose un tableau usuelle récapitulatif du bit selon le système internationale d'unité :

| Unité | Notation | Valeur |
|--- |--- |--- |
| Octet | o | $10^0$ |
| Kilooctet | Ko | $10^3$ |
| Mégaoctet | Mo | $10^6$ |
| Gigaoctet | Go | $10^9$ |
| Teraoctet | To | $10^{12}$ |
| Pétaoctet | Po | $10^{15}$ |
| Exaoctet | Eo | $10^{18}$ |
| Zettaoctet | Zo | $10^{21}$ |
| Yotaoctet | Yo | $10^{24}$ |

L'octet du SI

Donc par exemple 1Ko = 1000o = 8Mb = 8000b. **Par mésusage** 1Ko=Kbytes.

Il faut savoir que par le passé le passage entre plusieurs ordres de grandeurs se faisait par puissance de 2 et non par puissance 10. Ce qui représentait une anomalie du système internationale. Ainsi, **dans le passé** : $1 Ko = 2^{10} o$

L'utilisation de puissance de 2 n'a malgré tout pas été oublié et c'est ce qu'on va voir dans la prochaine section !

[C'est ici pour en savoir plus sur la représentation de nombre en mémoire.](https://keskec.fr/sciences/informatique/robin/243/)

## Kibioctet, Kibibit ?

Dans le passé $1 Ko = 2^{10}o = 1024 o$. Depuis 1998, on dira $1Kio = 2^{10}o$. La notation $1KiB = 2^10bits$ est aussi très courante. Le B majuscule signifiant Byte.

De façon analogue : $1Kibit = 2^{10}bits = 1024bits$.

L'utilisation de Gio ou de Tio se construira par la même logique :).

## Un petit exercice récapitulatif :

### Énoncé :

Je suis sur ma console en train de télécharger un jeu vidéo :

**Vitesse de téléchargement** : 75 mbits/s  
**Taille totale du Jeu** : 75go  
**Espace restant** : 70Gio

Aurais-je besoin de supprimer d'autre jeux pour télécharger celui-ci ?

Dans combien de temps, mon jeu sera téléchargé en heure?

### Correction :

$70Gio = 1 073 741 824 \times 70 o = 75 161 927 680 o = 75.1619 Go$.

La taille totale du Jeu est inférieur à l'espace restant, le jeu va pouvoir s'installer :).

Le jeu se télécharge à 75 Mbits/s, c'est-à-dire 9,375 Mo/s, mais encore 0,009375 Go/s.

En faisant un produit en croix, $1 \times 75 / 0.009375 = 8000 $ secondes. Ce qui fait 2.22 heures de téléchargement... (à condition que la connexion soit stable évidemment).

## Sources :

- [Convertisseur octet](http://www.ecommerce-pro.com/tutoriel/convertisseur_octets.php#:~:text=Un%20kilooctet%20(ko)%20%3D%20210,1%20073%20741%20824%20octets)
- [Préfixe du système international Wikipédia](https://fr.wikipedia.org/wiki/Pr%C3%A9fixes_du_Syst%C3%A8me_international_d%27unit%C3%A9s)
- [Profondeur de couleur Wikipédia](https://fr.wikipedia.org/wiki/Profondeur_de_couleur_(informatique))
- [Pixel 4 couleurs](https://www.lcd-compare.com/definition-de-4-color-pixels.htm)
- [Octet Wikipédia](https://fr.wikipedia.org/wiki/Octet)
- [Convertisseur](https://calculis.net/conversion/memoire)
- [Forum Comment ça marche?](https://forums.commentcamarche.net/forum/affich-4577255-disque-dur-320-go-a-298-go)
- [Byte Wikipédia](https://fr.wikipedia.org/wiki/Byte)
