---
title: "Modifier la Bitmap d'une image avec Python 3"
slug: "modifier-la-bitmap-dune-image-avec-python-et-numpy"
date: "2020-05-21"
categories: 
  - "informatique"
tags: 
  - "bitmap"
  - "matrice"
  - "numpy"
  - "python"
  - "tuto"
no: ""
---

Une image matricielle, ou « carte de points » (de l'anglais bitmap), est une image constituée d'une matrice de points colorés. Cela signifie qu'elle est constituée d'un tableau, d'une grille, où chaque case possède une couleur qui lui est propre et est considérée comme un point. (Wikipédia). Saviez-vous qu'il était possible de modifier cette bitmap très facilement en Python ? :)

## Télécharger une image

Je vous propose de modifier l'image que j'ai utilisé pour [mon article sur l'idée reçu des 5 sens](https://keskec.fr/sciences/biologie/robin/1101/) : [Celle-ci](https://keskec.fr/wp-content/uploads/2020/05/pexels-photo-2194261-1384x752.jpeg).

![](images/pexels-photo-2194261-1024x683.jpeg)

Chat Surpris

Il n'est pas nécessaire de la télécharger, je vais vous montrer comment le faire avec Python directement.

Tout d'abord, ouvrez un nouveau fichier python dans votre IDE préféré. Jupyter Notebook est probablement la meilleure alternative :).

Entrez ce code.

```
from PIL import Image
import requests
from io import BytesIO

Url = 'https://keskec.fr/wp-content/uploads/2020/05/pexels-photo-2194261-1384x752.jpeg'

response = requests.get(Url)
ImgDL = Image.open(BytesIO(response.content))
ImgDL.save("chat.jpeg")
```

Dans vos fichiers, vous pouvez maintenant trouver "chat.jpeg".

Je vous propose de faire une copie de ImgDL pour pouvoir réutiliser ImgDL plus tard si besoin.

```
import numpy as np
newImg = np.copy(ImgDL)
```

## Afficher les valeurs de la Bitmap

Pour afficher le tableau associé à l'image, rien de compliqué :

```
newImg
```

On peut remarquer que newImg contient un array (l'image) d'array (de lignes) d'array (pixel). Chaque pixel étant un triplet, Rouge, Vert, Bleu. Les lignes sont représentées de haut en bas.

## Modifier la Bitmap

### Créer une ligne noire

Il suffit de rendre tous les pixels de la première ligne égaux à \[0,0,0\].

Pour cela, rien de très compliqué :

#### Code :

```
newImg[0, 0:] = [0, 0, 0]

imgF = Image.fromarray(newImg, 'RGB')
imgF.save('LigneNoire.png')
newImg
```

#### Comparaison :

![](images/pexels-photo-2194261-1024x683.jpeg)

Chat Surpris

![](images/ligne-1024x683.png)

Chat Surpris avec la première ligne en noir

A peine visible, il y a bien une première ligne noir sur la photo de droite :).

### Rendre l'image rouge

Pour rendre une image "rouge", il faut que la première valeur de chaque pixel soit égale à sa valeur maximal. Autrement dit, il faut que le rouge soit égal à 255 pour chaque pixel.

#### Code :

```
newImg[0, 0:] = [0,0,0]
imgF = Image.fromarray(newImg, 'RGB')
imgF.save('Rouge.png')
imgF
```

#### Comparaison :

![](images/pexels-photo-2194261-1024x683.jpeg)

Chat Surpris

![](images/téléchargement-1024x683.png)

Chat Surpris Rouge

### Faire un négatif de l'image

Pour obtenir le négatif d’une image, il faut que chaque valeur soit remplacée par 255 moins sa valeur. Par exemple si pour le vert du pixel, sa valeur est 250, son négatif sera 255-250 = 5. Ainsi, il faut faire :

#### Code :

```
newImg[0:, 0:, 0:] = 255 - newImg[0:, 0:, 0:]
imgF = Image.fromarray(newImg, 'RGB')
imgF.save('Rouge.png')
imgF
```

#### Comparaison :

![](images/pexels-photo-2194261-1024x683.jpeg)

Image Originale

![](images/Chat-Surpris-Neg-1024x683.png)

Image Négative

## Le fichier sur GitHub :

[https://gist.github.com/RobinPourtaud/5036f9a5dfcff7fa43be1ec6ccae1484](https://gist.github.com/RobinPourtaud/5036f9a5dfcff7fa43be1ec6ccae1484)

## Plus de filtres ?

[Seuillage en Python 3](https://keskec.fr/sciences/informatique/robin/2524/)

## Sources :

- [https://stackoverflow.com/questions/3493092/convert-image-to-a-matrix-in-python](https://stackoverflow.com/questions/3493092/convert-image-to-a-matrix-in-python)
- [https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image](https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image)
- [https://www.pexels.com/photo/photo-of-gray-and-white-tabby-kitten-sitting-on-sofa-2194261/](https://www.pexels.com/photo/photo-of-gray-and-white-tabby-kitten-sitting-on-sofa-2194261/)
