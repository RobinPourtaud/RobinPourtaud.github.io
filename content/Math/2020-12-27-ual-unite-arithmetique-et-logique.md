---
title: UAL – Unité arithmétique et logique
author: Robin Pourtaud
type: post
date: 2020-12-27T11:55:01+00:00
url: /sciences/informatique/robin/5016/
featured_image: /wp-content/uploads/2020/12/UAL-1-1568x802.png
rank_math_seo_score:
  - "86"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - UAL
categories:
  - Informatique
tags:
  - Bit
  - Logique
  - Processeur

---
Une unité arithmétique et logique (UAL) ou ALU en anglais est un composant essentiel au fonctionnement de nos ordinateurs actuels. Souvent intégrée au processeur pour effectuer de nombreuses opérations arithmétiques, cet article en présente un exemple simple, conçu avec le logiciel Logisim. 

## Caractéristiques de l&rsquo;UAL : 

Notre UAL nous permet d&rsquo;effectuer 7 opérations sur des entiers signés de 8 bits. 

### Entrées : 

Notre UAL prend 3 entrées : 

  1. Un nombre sur 8 bits « A » utilisé en entrée des opérations.
  2. Un nombre sur 8 bits « B » utilisé en entrée des opérations.
  3. Un nombre sur 3 bits « ctr » utilisé pour sélectionner l&rsquo;opération désirée. 

### Sorties : 

Notre UAL possède 2 sorties : 

  1. Un nombre sur 8 bits étant le résultat de l&rsquo;opération choisie. 
  2. Un nombre sur 4 bits présentant chaque flag. 

### Opérations : 

Notre UAL peut nous autoriser à effectuer 8 opérations. Nous nous servirons uniquement de 7 d&rsquo;entre elles : 

<ol start="0">
  <li>
    ctr = 000 : Addition
  </li>
  <li>
    ctr = 001 : Soustraction
  </li>
  <li>
    ctr = 010 : OU bit à bit
  </li>
  <li>
    ctr = 011 : Et bit à bit
  </li>
  <li>
    ctr = 100 : Non bit à bit
  </li>
  <li>
    ctr = 101 : Décalage à gauche logique
  </li>
  <li>
    ctr = 110 : Décalage à droite logique
  </li>
</ol>

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-30-1024x667.png" alt="" class="wp-image-5059" width="451" height="293" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-30-1024x667.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-30-300x195.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-30-768x500.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-30.png 1302w" sizes="(max-width: 451px) 100vw, 451px" /><figcaption>Opérations &#8211; UAL</figcaption></figure>
</div>

Les opérations « non » et les 2 décalages se servent uniquement du premier nombre « A ». C+ et C- sont les carrys de l&rsquo;addition et de la soustraction. 

## Flags : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-23.png" alt="" class="wp-image-5049" width="250" height="148" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-23.png 448w, https://keskec.fr/wp-content/uploads/2020/12/image-23-300x177.png 300w" sizes="(max-width: 250px) 100vw, 250px" /><figcaption>4 bits Flags</figcaption></figure>
</div>

Notre sortie flags est représentée par un 4 bit correspondant respectivement à CF, ZF, SF et OF.

### Carry Flag (CF) : 

**Commentaire :** Dans le cadre d&rsquo;additions et de soustractions sur des nombres signés, le carry flag ne pourra **jamais** être égal à 1. Vous pouvez donc relier le bit CF à « 0 ».  
Cependant, dans le cadre de ce tutoriel, le circuit restera explicité : 

  * c+ est le carry de l&rsquo;opération 000 (addition)
  * c- est le carry de l&rsquo;opération 001 (soustraction)

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-24.png" alt="" class="wp-image-5050" width="152" height="136" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-24.png 317w, https://keskec.fr/wp-content/uploads/2020/12/image-24-300x269.png 300w" sizes="(max-width: 152px) 100vw, 152px" /><figcaption>Carry Flag</figcaption></figure>
</div>

  * Si ctr = 000, alors CF = c+
  * Si ctr = 001, alors CF = c-
  * Sinon CF = 0

### Zéro Flag (ZF) : 

Le zéro flag est égal à 1 si et seulement si tous les bits de S sont égaux à 0 : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-25.png" alt="" class="wp-image-5051" width="306" height="200" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-25.png 467w, https://keskec.fr/wp-content/uploads/2020/12/image-25-300x196.png 300w" sizes="(max-width: 306px) 100vw, 306px" /><figcaption>Zero Flag</figcaption></figure>
</div>



Autrement dit :<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-dd1fef740e4711b715e8ac42f7115e4f_l3.svg" class="ql-img-inline-formula " alt="&#90;&#70;&#32;&#61;&#32;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#95;&#48;&#43;&#83;&#95;&#49;&#43;&#83;&#95;&#50;&#43;&#83;&#95;&#51;&#43;&#83;&#95;&#52;&#43;&#83;&#95;&#53;&#43;&#83;&#95;&#54;&#43;&#83;&#95;&#55;&#125;" title="Rendered by QuickLaTeX.com" height="20" width="395" style="vertical-align: -3px;" /> 

### Sign Flag (SF) : 

SF correspond au signe de S. Si S négatif, alors S = 1, sinon S=0.

Autrement dit :<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-a70ea3ea5beaba6cee2951c57fb1047a_l3.svg" class="ql-img-inline-formula " alt="&#83;&#70;&#32;&#61;&#32;&#83;&#95;&#55;" title="Rendered by QuickLaTeX.com" height="17" width="75" style="vertical-align: -3px;" /> 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-26.png" alt="" class="wp-image-5052" width="213" height="199" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-26.png 432w, https://keskec.fr/wp-content/uploads/2020/12/image-26-300x280.png 300w" sizes="(max-width: 213px) 100vw, 213px" /><figcaption>Sign Flag</figcaption></figure>
</div>

### Overflow Flag (OF) : 

L&rsquo;overflow flag est égal à 1 dans 4 cas différent: 

  1. Pour une addition : Si un positif + un positif = un négatif 
  2. Pour une addition : Si un négatif + un négatif = un positif 
  3. Pour une soustraction : Si un négatif &#8211; un positif = un positif
  4. Pour une soustraction : Si un positif &#8211; un négatif = un négatif

Dans les autres cas : OF = 0. 

  * S A est le signe de A
  * S B est le signe de B
  * SF est le signe de S

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-28.png" alt="" class="wp-image-5054" width="384" height="186" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-28.png 896w, https://keskec.fr/wp-content/uploads/2020/12/image-28-300x146.png 300w" sizes="(max-width: 384px) 100vw, 384px" /><figcaption>Overflow Flag</figcaption></figure>
</div>

Autrement dit : 

  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-c3c67e95ac7cb4e3302550279cee7507_l3.svg" class="ql-img-inline-formula " alt="&#79;&#70;&#43;&#32;&#61;&#32;&#83;&#65;&#46;&#83;&#66;&#46;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#70;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#65;&#125;&#46;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#66;&#125;&#46;&#83;&#70;" title="Rendered by QuickLaTeX.com" height="19" width="294" style="vertical-align: -2px;" /> 
  *<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-b402dda2f90c8d6ecf3e561dbbf6d390_l3.svg" class="ql-img-inline-formula " alt="&#79;&#70;&#45;&#32;&#61;&#32;&#83;&#65;&#46;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#66;&#125;&#46;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#70;&#125;&#43;&#92;&#111;&#118;&#101;&#114;&#108;&#105;&#110;&#101;&#123;&#83;&#65;&#125;&#46;&#83;&#66;&#46;&#83;&#70;" title="Rendered by QuickLaTeX.com" height="19" width="294" style="vertical-align: -2px;" /> 
  * OF = OF+ si ctr = 000, OF- si ctr = 001, 0 sinon. 

## Mention : 

Cette unité arithmétique et logique a été conçu dans le cadre d&rsquo;un projet d&rsquo;informatique en collaboration avec [Mr Lucas Lelièvre][1]{.rank-math-link} que je remercie.

 [1]: https://www.linkedin.com/in/lucas-leli%C3%A8vre-b30990151/?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_top%3BQjKA%2FeL3SlC434krJot2NQ%3D%3D&licu=urn%3Ali%3Acontrol%3Ad_flagship3_search_srp_top-search_srp_result&lici=R3L0SBS2RwyBRO8CpE9SBA%3D%3D