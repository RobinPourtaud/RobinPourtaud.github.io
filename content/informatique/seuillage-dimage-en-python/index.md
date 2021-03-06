---
title: "Seuillage d'image en Python3"
slug: "seuillage-dimage-en-python"
date: "2020-06-17"
categories: 
  - "informatique"
tags: 
  - "numpy"
  - "python"
  
description: "Le seuillage est une technique de traitement d'image permettant l'attribution de chaque pixel soit à une couleur, soit à une autre, selon un seuil. Plus explicitement :"
---


## Définition

Soit $f$, une image composée de $n$ lignes et $m$ colonnes, $\forall i \in \[0,n\]$ et $\forall j \in \[0,m\]$.

Soit $f(i,j)$ l'intensité d'un pixel. C'est à dire la valeur maximale du triplet $\[R,G,B\]$ associée au pixel.

Soit un seuil $s \in \[0,255\]$.

Alors le seuillage de l'image f serait équivalent à une fonction $g$ tel que :

$$g(i,j) = \begin{cases} 255 & \text{si} \; f(i,j) \leq s \\ 0 & \text{sinon.}  \end{cases}$$


## Nécessaire

### Python 3 :

Pour suivre ce tutoriel, vous devez avoir installé Python 3 ainsi que le package numpy.

J'utiliserai personnellement le "Jupyter notebook" de Google : [Google Colab](https://colab.research.google.com/).

### Article précédent sur les bitmaps en python :

[Modifier la Bitmap d’une image avec Python 3](https://keskec.fr/sciences/informatique/robin/2137/)

## Fonction de seuillage

Tout d'abord, il nous faut une image. Pour cela, je vous suggère de télécharger celle-ci comme ceci :

```python
import numpy as np
from PIL import Image
import requests
from io import BytesIO

Url = 'https://keskec.fr/wp-content/uploads/2020/05/autumn-autumn-leaves-beautiful-color-206648-1024x771.jpg'

response = requests.get(Url)
ImgDL = Image.open(BytesIO(response.content))
```

### La fonction :

Il existe plein de façon d'effectuer un seuillage en python, je vous propose celle-ci :

```python
def Seuillage(Img:Image, s:int)->Image:
  newImg = np.copy(Img)
  for i in range(len(newImg)):
    for j in range(len(newImg[0])):
      x = newImg[i,j,0]
      y = newImg[i,j,1]
      z = newImg[i,j,2]

      if x < s or y < s or z < s : 
        newImg[i,j,0:] = 0

      else : 
        newImg[i,j,0:] = 255

  return Image.fromarray(newImg, 'RGB')
```

Un exemple d'utilisation de cette fonction serait :

```python
Seuillage(ImgDL,90)
```

### Le résultat :

![Image originale](autumn-autumn-leaves-beautiful-color-206648-1024x771.jpg#t3)



![Seuillage d image (seuil = 110)](téléchargement-1024x771.png#t3)



Faire varier le seuil entre 0 et 255 peut permettre d'obtenir de nombreuses images très intéressantes :



<amp-carousel height="300" layout="fixed-height" type="carousel" role="region">
    <amp-img src="image-4.png" width="400" height="300" alt="Seuille = 20"></amp-img>
    <amp-img src="image-5.png" width="400" height="300" alt="Seuille = 70"></amp-img>
    <amp-img src="image-6.png" width="400" height="300" alt="Seuille = 140"></amp-img>
</amp-carousel>

## Le code source sur Github

[seuillage-keskec.ipynb](https://gist.github.com/RobinPourtaud/274589130004ef89eb83569019bfeca6#file-seuillage-keskec-ipynb)

## Sources

1. [Seuillage d'image - Wikipédia](https://fr.wikipedia.org/wiki/Seuillage_d%27image)
2. [Forum Développez.net](https://www.developpez.net/forums/d1424637/autres-langages/python/calcul-scientifique/seuillage-d-image-rgb/)
