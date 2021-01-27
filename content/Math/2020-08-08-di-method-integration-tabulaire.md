---
title: DI Method / Intégration tabulaire
author: Robin Pourtaud
type: post
date: 2020-08-08T18:29:42+00:00
url: /sciences/mathematiques/robin/4119/
featured_image: /wp-content/uploads/2020/08/K-1568x1029.png
rank_math_seo_score:
  - "81"
rank_math_primary_category:
  - "9"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - DI Method
rank_math_analytic_object_id:
  - "23"
categories:
  - Mathématiques
tags:
  - Intégrale

---
L&rsquo; intégration par partie est une étape essentielle à la recherche de primitive. Il est facile de mal interpréter la formule, c&rsquo;est pourquoi il existe une méthode appelée Intégration tabulaire (ou DI method) permettant d&rsquo;éviter ce procédé classique et donc de s&rsquo;épargner de nombreuses erreurs potentielles&#8230; Elle aurait été introduite dans le film « Stand and Deliver » [1]. 

## Exemple d&rsquo;utilisation : 

Pour introduire la DI Method, nous nous servirons de 2 exemples : 

### Exemple 1 



On souhaite résoudre l&rsquo;intégrale : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-2f07f2be721656af25beb7827ee90476_l3.svg" class="ql-img-inline-formula " alt="&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#40;&#120;&#41;&#32;&#120;&#94;&#50;&#32;&#100;&#120;" title="Rendered by QuickLaTeX.com" height="27" width="130" style="vertical-align: -7px;" />
</p>

#### Création du tableau

Comme pour l&rsquo;intégration par partie, nous choisissons quel facteur de l&rsquo;intégrale nous souhaitons intégrer et quel facteur nous souhaitons dériver. Dans notre cas, nous dériverons<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-96691d3e59207b63443dbf279cbcc6fa_l3.svg" class="ql-img-inline-formula " alt="&#120;&#94;&#50;" title="Rendered by QuickLaTeX.com" height="17" width="18" style="vertical-align: 0px;" /> et intégrerons<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-24a861da40b764b1b3481832707118cd_l3.svg" class="ql-img-inline-formula " alt="&#99;&#111;&#115;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="53" style="vertical-align: -5px;" /> .<figure class="wp-block-table">

<table>
  <tr>
    <td>
      <strong>Ligne</strong>
    </td>
    
    <td>
      <strong>Signe</strong>
    </td>
    
    <td>
      <strong>D</strong>
    </td>
    
    <td>
      <strong>I</strong>
    </td>
  </tr>
  
  <tr>
    <td>
      1
    </td>
    
    <td>
      +
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-96691d3e59207b63443dbf279cbcc6fa_l3.svg" class="ql-img-inline-formula " alt="&#120;&#94;&#50;" title="Rendered by QuickLaTeX.com" height="17" width="18" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-24a861da40b764b1b3481832707118cd_l3.svg" class="ql-img-inline-formula " alt="&#99;&#111;&#115;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="53" style="vertical-align: -5px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      &#8211;
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-3c43d047c48e90e89cdf92ce0bf7a024_l3.svg" class="ql-img-inline-formula " alt="&#50;&#120;" title="Rendered by QuickLaTeX.com" height="14" width="21" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-bf0da28de19f36974e97fe24d0f4b1b3_l3.svg" class="ql-img-inline-formula " alt="&#115;&#105;&#110;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="52" style="vertical-align: -5px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      +
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-de8b68b4acfa64b639b429b17db8bcf7_l3.svg" class="ql-img-inline-formula " alt="&#50;" title="Rendered by QuickLaTeX.com" height="14" width="9" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d7aa3dcd2fb671d303ff5f192ec7fd16_l3.svg" class="ql-img-inline-formula " alt="&#45;&#99;&#111;&#115;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="68" style="vertical-align: -5px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      4
    </td>
    
    <td>
      &#8211;
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-fbe56718f69dc5553362893e4bac33e7_l3.svg" class="ql-img-inline-formula " alt="&#48;" title="Rendered by QuickLaTeX.com" height="14" width="10" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-baed0994e77dda80cec1aa51de002a82_l3.svg" class="ql-img-inline-formula " alt="&#45;&#115;&#105;&#110;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="68" style="vertical-align: -5px;" />
    </td>
  </tr>
</table><figcaption>Tableau de la méthode d&rsquo;intégration tabulaire</figcaption></figure> 

Dans la colonne signe, nous alternons le signe positif et négatif.

Dans la colonne D, nous dérivons ligne par ligne tant que le facteur reste différente de 0.

Dans la colonne I, nous intégrons l&rsquo;expression ligne par ligne.

_**Note** : Il faut savoir qu&rsquo;on peut continuer ou arrêter le tableau à la ligne que l&rsquo;on souhaite. Cependant, dans notre cas, l&rsquo;arrêter avant la fin laisserait une intégrale à évaluer, et continuer rajouterait des produits égaux à 0._ 

#### Utilisation du tableau 

Nous pouvons dès maintenant évaluer cette intégrale avec ce tableau. 

Nous commençons par additionner pour toutes les lignes de 1 à 3 le produit de D avec le I de la ligne suivante, en multipliant chaque produit par le signe qui lui est associé. 

Pour la dernière ligne, nous ajoutons l&rsquo;intégrale du produit D &#8211; I multipliée par le signe.

_Autrement dit, nous dérivons en diagonale jusqu&rsquo;à l&rsquo;avant dernière ligne, puis on intègre la dernière ligne._ 

Cela nous donne directement la solution : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-9216cafefe6d67b799d0c5ca9a4945df_l3.svg" class="ql-img-inline-formula " alt="&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#40;&#120;&#41;&#32;&#120;&#94;&#50;&#32;&#100;&#120;&#32;&#61;&#32;&#43;&#32;&#40;&#120;&#94;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#115;&#105;&#110;&#40;&#120;&#41;&#41;&#32;&#45;&#32;&#40;&#50;&#120;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#99;&#111;&#115;&#40;&#120;&#41;&#41;&#32;&#43;&#32;&#40;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#115;&#105;&#110;&#40;&#120;&#41;&#41;&#32;&#45;&#32;&#40;&#92;&#105;&#110;&#116;&#32;&#32;&#48;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#115;&#105;&#110;&#40;&#120;&#41;&#32;&#100;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="55" width="758" style="vertical-align: -6px;" />
</p>

Ce qui nous donne bien : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-c12c10a167679e3da79771bf065366ef_l3.svg" class="ql-img-inline-formula " alt="&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#40;&#120;&#41;&#32;&#120;&#94;&#50;&#32;&#100;&#120;&#32;&#61;&#32;&#50;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#99;&#111;&#115;&#40;&#120;&#41;&#32;&#43;&#32;&#40;&#45;&#50;&#32;&#43;&#32;&#120;&#94;&#50;&#41;&#32;&#115;&#105;&#110;&#40;&#120;&#41;" title="Rendered by QuickLaTeX.com" height="27" width="454" style="vertical-align: -7px;" />
</p>

Vous pouvez retrouver la même chose sur [Wolfram Alpha][1]{.rank-math-link}.

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-1024x366.png" alt="" class="wp-image-4124" width="581" height="208" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-1024x366.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-300x107.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-768x275.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-1536x549.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-1568x561.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-150x54.png 150w, https://keskec.fr/wp-content/uploads/2020/08/image.png 1616w" sizes="(max-width: 581px) 100vw, 581px" /><figcaption>Intégrale x^2 cosx dx &#8211; Wolfram Alpha</figcaption></figure>
</div>

### Exemple 2 : 

Dans un autre article, pour résoudre [l&rsquo;intégrale de x à la puissance i][2]{.rank-math-link}, j&rsquo;ai dû effectuer une intégration par partie pour l&rsquo;intégrale : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a79bec0a9346c85ccc527485d05b051d_l3.svg" class="ql-img-inline-formula " alt="&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#40;&#117;&#41;&#32;&#101;&#94;&#117;&#32;&#100;&#117;" title="Rendered by QuickLaTeX.com" height="26" width="129" style="vertical-align: -7px;" />.
</p>

#### Création du tableau<figure class="wp-block-table">

<table>
  <tr>
    <td>
      Ligne
    </td>
    
    <td>
      Signe
    </td>
    
    <td>
      D
    </td>
    
    <td>
      I
    </td>
  </tr>
  
  <tr>
    <td>
      1
    </td>
    
    <td>
      +
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0c2baa0ad522ad93028683eb3d83ee12_l3.svg" class="ql-img-inline-formula " alt="&#101;&#94;&#117;" title="Rendered by QuickLaTeX.com" height="14" width="18" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-92ce4ef3a574972a67d7a8c9956277be_l3.svg" class="ql-img-inline-formula " alt="&#99;&#111;&#115;&#40;&#117;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="53" style="vertical-align: -5px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      2
    </td>
    
    <td>
      &#8211;
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0c2baa0ad522ad93028683eb3d83ee12_l3.svg" class="ql-img-inline-formula " alt="&#101;&#94;&#117;" title="Rendered by QuickLaTeX.com" height="14" width="18" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-ed940e127a8a6da6cb0acbb103274de7_l3.svg" class="ql-img-inline-formula " alt="&#115;&#105;&#110;&#40;&#117;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="52" style="vertical-align: -5px;" />
    </td>
  </tr>
  
  <tr>
    <td>
      3
    </td>
    
    <td>
      +
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-0c2baa0ad522ad93028683eb3d83ee12_l3.svg" class="ql-img-inline-formula " alt="&#101;&#94;&#117;" title="Rendered by QuickLaTeX.com" height="14" width="18" style="vertical-align: 0px;" />
    </td>
    
    <td>
      <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-e28b412887faf008abc0efbe0881419f_l3.svg" class="ql-img-inline-formula " alt="&#45;&#99;&#111;&#115;&#40;&#117;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="68" style="vertical-align: -5px;" />
    </td>
  </tr>
</table><figcaption>Tableau DI Method e^u cos(u)</figcaption></figure> 

Comme nous pouvons le voir, la dérivé ne sera jamais égale à 0 contrairement à l&rsquo;exemple 1. Dans ce cas là, nous pouvons nous arrêter si on arrive à une répétition :  
Nous avons<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-92ce4ef3a574972a67d7a8c9956277be_l3.svg" class="ql-img-inline-formula " alt="&#99;&#111;&#115;&#40;&#117;&#41;" title="Rendered by QuickLaTeX.com" height="20" width="53" style="vertical-align: -5px;" /> en ligne 1 et 3. 

#### Utilisation du tableau

De façon analogue à l&rsquo;exemple 1, nous avons : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b4140d3d8746b4f718a78c15276a1a04_l3.svg" class="ql-img-inline-formula " alt="&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#32;&#40;&#117;&#41;&#32;&#101;&#94;&#117;&#32;&#32;&#61;&#32;&#43;&#32;&#40;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#115;&#105;&#110;&#40;&#117;&#41;&#41;&#32;&#45;&#32;&#40;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#99;&#111;&#115;&#40;&#117;&#41;&#41;&#32;&#43;&#32;&#40;&#92;&#105;&#110;&#116;&#32;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#99;&#111;&#115;&#40;&#117;&#41;&#41;" title="Rendered by QuickLaTeX.com" height="26" width="659" style="vertical-align: -7px;" />
</p>

En reformulant, nous avons : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-6ffd4354418ff434f1c10ca432774880_l3.svg" class="ql-img-inline-formula " alt="&#50;&#32;&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#32;&#117;&#32;&#101;&#94;&#117;&#32;&#61;&#32;&#43;&#32;&#40;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#115;&#105;&#110;&#40;&#117;&#41;&#41;&#32;&#45;&#32;&#40;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#45;&#99;&#111;&#115;&#40;&#117;&#41;&#41;" title="Rendered by QuickLaTeX.com" height="26" width="459" style="vertical-align: -7px;" />
</p>

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-632ecdd6aed5205ad2f9b478fe25ce87_l3.svg" class="ql-img-inline-formula " alt="&#32;&#92;&#105;&#110;&#116;&#32;&#99;&#111;&#115;&#32;&#117;&#32;&#101;&#94;&#117;&#32;&#61;&#32;&#92;&#102;&#114;&#97;&#99;&#123;&#49;&#125;&#123;&#50;&#125;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#101;&#94;&#117;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#40;&#115;&#105;&#110;&#40;&#117;&#41;&#45;&#99;&#111;&#115;&#40;&#117;&#41;&#41;" title="Rendered by QuickLaTeX.com" height="29" width="381" style="vertical-align: -8px;" />
</p>

Encore une fois, vous pouvez trouver le même résultat sur Wolfram Alpha.

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-1-1024x354.png" alt="" class="wp-image-4135" width="549" height="189" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-1-1024x354.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-1-300x104.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-1-768x265.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-1-1536x531.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-1-1568x542.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-1-150x52.png 150w, https://keskec.fr/wp-content/uploads/2020/08/image-1.png 1647w" sizes="(max-width: 549px) 100vw, 549px" /><figcaption>Intégrale cos u sin^u du &#8211; Wolfram Alpha</figcaption></figure>
</div>

## En vidéo 

Si vous êtes à l&rsquo;aise avec l&rsquo;**anglais**, je ne peux que vous recommander la chaine de blackpenredpen. Il présente de manière concise et claire la méthode tabulaire. <figure class="wp-block-embed-youtube wp-block-embed is-type-video is-provider-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio">

<div class="wp-block-embed__wrapper">
</div><figcaption>Intégration par partie &#8211; DI method en Anglais</figcaption></figure> 

## Sources : 

  1. [Intégration par parties &#8211;&nbsp;Integration by parts][3]{.rank-math-link}
  2. [Tabular Integration Method sin(ln(x)) DI ou présentation tabulaire.][4]{.rank-math-link}
  3. [integration by parts, DI method, VERY EASY &#8211; blackpenredpen &#8211; Youtube][5]{.rank-math-link}

 [1]: https://www.wolframalpha.com/input/?i=int+x%5E2+cosx+dx
 [2]: https://keskec.fr/sciences/mathematiques/robin/220/
 [3]: https://fr.qwe.wiki/wiki/Integration_by_parts#Tabular_integration_by_parts
 [4]: https://maths1024.blogspot.com/2017/12/tabular-integration-method-sinlnx-di-ou.html
 [5]: https://www.youtube.com/watch?v=2I-_SV8cwsw