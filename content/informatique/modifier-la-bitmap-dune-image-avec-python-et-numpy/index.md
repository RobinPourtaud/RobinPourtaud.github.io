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
  
description: "Une image matricielle, ou « carte de points » (de l'anglais bitmap), est une image constituée d'une matrice de points colorés. Cela signifie qu'elle est constituée d'un tableau, d'une grille, où chaque case possède une couleur qui lui est propre et est considérée comme un point. (Wikipédia). Saviez-vous qu'il était possible de modifier cette bitmap très facilement en Python ? :)"
---
## Télécharger une image

Je vous propose de modifier cette image [image](pexels-photo-2194261-1384x752.jpeg).

![Chat Surpris](pexels-photo-2194261-1024x683.jpeg#t4)



Il n'est pas nécessaire de la télécharger, je vais vous montrer comment le faire avec Python directement.

Tout d'abord, ouvrez un nouveau fichier python dans votre IDE préféré. Jupyter Notebook est probablement la meilleure alternative :).

Entrez ce code.

```python
from PIL import Image
import requests
from io import BytesIO

Url = 'https://devmath.fr/informatique/modifier-la-bitmap-dune-image-avec-python-et-numpy/pexels-photo-2194261-1384x752.jpeg'

response = requests.get(Url)
ImgDL = Image.open(BytesIO(response.content))
ImgDL.save("chat.jpeg")
```

Dans vos fichiers, vous pouvez maintenant trouver "chat.jpeg".

Je vous propose de faire une copie de ImgDL pour pouvoir réutiliser ImgDL plus tard si besoin.

```python
import numpy as np
newImg = np.copy(ImgDL)
```

## Afficher les valeurs de la Bitmap

Pour afficher le tableau associé à l'image, rien de compliqué :

```python
newImg
```

On peut remarquer que newImg contient un array (l'image) d'array (de lignes) d'array (pixel). Chaque pixel étant un triplet, Rouge, Vert, Bleu. Les lignes sont représentées de haut en bas.

## Modifier la Bitmap

### Créer une ligne noire

Il suffit de rendre tous les pixels de la première ligne égaux à \[0,0,0\].

Pour cela, rien de très compliqué :

#### Code :

```python
newImg[0, 0:] = [0, 0, 0]

imgF = Image.fromarray(newImg, 'RGB')
imgF.save('LigneNoire.png')
newImg
```

#### Comparaison :

![Chat Surpris](pexels-photo-2194261-1024x683.jpeg#t4)



![Chat Surpris avec la première ligne en noir](ligne-1024x683.png#t4)



A peine visible, il y a bien une première ligne noir sur la photo de droite :).

### Rendre l'image rouge

Pour rendre une image "rouge", il faut que la première valeur de chaque pixel soit égale à sa valeur maximal. Autrement dit, il faut que le rouge soit égal à 255 pour chaque pixel.

#### Code :

```python
newImg[0, 0:] = [0,0,0]
imgF = Image.fromarray(newImg, 'RGB')
imgF.save('Rouge.png')
imgF
```

#### Comparaison :

![Chat Surpris](pexels-photo-2194261-1024x683.jpeg#t4)



![Chat Surpris Rouge](téléchargement-1024x683.png#t4)


### Faire un négatif de l'image

Pour obtenir le négatif d’une image, il faut que chaque valeur soit remplacée par 255 moins sa valeur. Par exemple si pour le vert du pixel, sa valeur est 250, son négatif sera 255-250 = 5. Ainsi, il faut faire :

#### Code :

```python
newImg[0:, 0:, 0:] = 255 - newImg[0:, 0:, 0:]
imgF = Image.fromarray(newImg, 'RGB')
imgF.save('negatif.png')
imgF
```

#### Comparaison :

![Image Originale](pexels-photo-2194261-1024x683.jpeg#t4)



![Image Négative](Chat-Surpris-Neg-1024x683.png#t4)



## Le fichier sur GitHub :

[https://gist.github.com/RobinPourtaud/5036f9a5dfcff7fa43be1ec6ccae1484](https://gist.github.com/RobinPourtaud/5036f9a5dfcff7fa43be1ec6ccae1484)

## Plus de filtres ?

[Seuillage en Python 3](https://keskec.fr/sciences/informatique/robin/2524/)

## Sources :

- [https://stackoverflow.com/questions/3493092/convert-image-to-a-matrix-in-python](https://stackoverflow.com/questions/3493092/convert-image-to-a-matrix-in-python)
- [https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image](https://stackoverflow.com/questions/2659312/how-do-i-convert-a-numpy-array-to-and-display-an-image)
- [https://www.pexels.com/photo/photo-of-gray-and-white-tabby-kitten-sitting-on-sofa-2194261/](https://www.pexels.com/photo/photo-of-gray-and-white-tabby-kitten-sitting-on-sofa-2194261/)
