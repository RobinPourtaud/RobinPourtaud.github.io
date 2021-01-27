---
title: 'Démonstration : Toutes les puissances de 6 finissent par un 6'
author: Robin Pourtaud
type: post
date: 2020-08-30T14:00:24+00:00
url: /sciences/mathematiques/robin/4448/
featured_image: /wp-content/uploads/2020/08/puissance-de-6-1568x543.png
rank_math_seo_score:
  - "55"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "9"
rank_math_focus_keyword:
  - Puissances de 6
rank_math_analytic_object_id:
  - "15"
categories:
  - Mathématiques
tags:
  - Démonstration

---
 

Par une démonstration par récurrence, cet article montrera que toutes les puissances strictement positives de 6 finissent toujours par un 6. 

## Intuition : 

6 puissance 1 est 6, 6 puissance 2 36, 6 puissance 3 216. Pour aller plus vite je vous propose ce code python : 

<pre class="wp-block-code" aria-describedby="shcb-language-121" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">&lt;span class="hljs-keyword">for&lt;/span> i &lt;span class="hljs-keyword">in&lt;/span> range(&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">20&lt;/span>) : print(&lt;span class="hljs-string">"6 puissance "&lt;/span> + str(i) + &lt;span class="hljs-string">" est égale à "&lt;/span> + str(&lt;span class="hljs-number">6&lt;/span>**i))</code>
</div>

<small class="shcb-language" id="shcb-language-121"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

A l&rsquo;exécution, nous avons : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-6-1024x530.png" alt="" class="wp-image-4449" width="613" height="317" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-6-1024x530.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-6-300x155.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-6-768x398.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-6-1536x795.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-6-1568x812.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-6.png 1665w" sizes="(max-width: 613px) 100vw, 613px" /><figcaption>Puissance de 6 de 1 à 19</figcaption></figure>
</div>

Bien que très persuasif, ce n&rsquo;est pas suffisant pour considérer cette propriété comme vraie&#8230; 

On souhaite que cette propriété soit vraie pour toutes les puissances, une démonstration par récurrence semble donc être un choix judicieux&#8230; 

## Démonstration 

### Énoncé 



Soit<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-f72758fdfe50e6e9e6463e8d76ed918e_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#111;&#114;&#97;&#108;&#108;&#32;&#110;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;&#42;" title="Rendered by QuickLaTeX.com" height="15" width="71" style="vertical-align: -1px;" /> , nous allons prouver par récurrence la propriété<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-1e7d21ac9e344537d7044cd4dd87a7a3_l3.svg" class="ql-img-inline-formula " alt="&#80;&#95;&#110;" title="Rendered by QuickLaTeX.com" height="17" width="22" style="vertical-align: -3px;" /> :<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-76e4b7bd2e64844b576ba6e1e9e6d389_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="14" width="19" style="vertical-align: 0px;" /> se termine par un 6.

### Initialisation {.has-text-align-left}

On vérifie que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-20b80ddb400f45b250760d140baa30b2_l3.svg" class="ql-img-inline-formula " alt="&#80;&#95;&#49;" title="Rendered by QuickLaTeX.com" height="17" width="20" style="vertical-align: -3px;" /> est vrai : 

<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-9347d0e9832b774fff490caa17626477_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#49;&#32;&#61;&#32;&#54;" title="Rendered by QuickLaTeX.com" height="17" width="55" style="vertical-align: 0px;" /> se termine par un 6.

La propriété est vraie au rang 1. 

### Hérédité

Soit<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d74297808032749ccd33a9f8c6d59821_l3.svg" class="ql-img-inline-formula " alt="&#110;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;&#94;&#42;" title="Rendered by QuickLaTeX.com" height="15" width="57" style="vertical-align: -1px;" /> , nous supposons que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-76e4b7bd2e64844b576ba6e1e9e6d389_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#110;" title="Rendered by QuickLaTeX.com" height="14" width="19" style="vertical-align: 0px;" /> se termine par un 6. 

On peut réécrire notre hypothèse de récurrence comme ceci<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-5764af24388daddf9ad37adee32443a1_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#111;&#114;&#97;&#108;&#108;&#32;&#107;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;" title="Rendered by QuickLaTeX.com" height="15" width="61" style="vertical-align: -1px;" /> : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-f0ce20a9f8d4d80eb81d01175933c754_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#110;&#32;&#61;&#32;&#49;&#48;&#107;&#32;&#43;&#32;&#54;" title="Rendered by QuickLaTeX.com" height="16" width="112" style="vertical-align: -2px;" />
</p>

Nous avons donc : 

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-d0e855d842f5dcd846ce0a8853560ddd_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;&#32;&#61;&#32;&#54;&#32;&#92;&#116;&#105;&#109;&#101;&#115;&#32;&#40;&#49;&#48;&#107;&#32;&#43;&#32;&#54;&#41;" title="Rendered by QuickLaTeX.com" height="22" width="181" style="vertical-align: -5px;" />
</p>

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-45042ec1c58c75ea5fc77cbcfd2be62f_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;&#32;&#61;&#32;&#54;&#48;&#107;&#32;&#43;&#32;&#51;&#54;" title="Rendered by QuickLaTeX.com" height="19" width="142" style="vertical-align: -2px;" />
</p>

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-c9770eabe8c39c20c206351d7213f9c9_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;&#32;&#61;&#32;&#54;&#48;&#107;&#32;&#43;&#32;&#51;&#48;&#32;&#43;&#32;&#54;" title="Rendered by QuickLaTeX.com" height="19" width="177" style="vertical-align: -2px;" />
</p>

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-de57c47830145f6b7d03f12c2eb3a5ef_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;&#32;&#61;&#32;&#49;&#48;&#40;&#54;&#107;&#32;&#43;&#32;&#51;&#41;&#32;&#43;&#32;&#54;" title="Rendered by QuickLaTeX.com" height="22" width="192" style="vertical-align: -5px;" />
</p>

En prenant<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-7fe500292c372aabed717381f5ff3791_l3.svg" class="ql-img-inline-formula " alt="&#107;&#39;&#32;&#61;&#32;&#54;&#107;&#43;&#51;" title="Rendered by QuickLaTeX.com" height="18" width="97" style="vertical-align: -2px;" /> ,<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-79bd05e8e54afbd53ec548e5a6a1d412_l3.svg" class="ql-img-inline-formula " alt="&#107;&#39;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="54" style="vertical-align: -1px;" /> :

<p class="has-text-align-center">
  <img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-23ebbbf388b618885f0f060032efd1be_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;&#32;&#61;&#32;&#49;&#48;&#107;&#39;&#32;&#43;&#32;&#54;" title="Rendered by QuickLaTeX.com" height="19" width="137" style="vertical-align: -2px;" />
</p>

Ce qui implique donc que<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-8c77d4ba08f884ee538aa3f4783290b0_l3.svg" class="ql-img-inline-formula " alt="&#54;&#94;&#123;&#110;&#43;&#49;&#125;" title="Rendered by QuickLaTeX.com" height="17" width="38" style="vertical-align: 0px;" /> se termine par un 6.

### Conclusion

D’après le principe de récurrence, la propriété<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-1e7d21ac9e344537d7044cd4dd87a7a3_l3.svg" class="ql-img-inline-formula " alt="&#80;&#95;&#110;" title="Rendered by QuickLaTeX.com" height="17" width="22" style="vertical-align: -3px;" /> est vraie<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-c99669e518eb53983f6ae7e6da0e074a_l3.svg" class="ql-img-inline-formula " alt="&#92;&#102;&#111;&#114;&#97;&#108;&#108;&#32;&#110;&#32;&#92;&#105;&#110;&#32;&#92;&#109;&#97;&#116;&#104;&#98;&#98;&#123;&#78;&#125;&#94;&#42;" title="Rendered by QuickLaTeX.com" height="15" width="69" style="vertical-align: -1px;" /> .

## Aller plus loin 

De façon analogue à cette démonstration, vous pouvez prouver cette identité pour les puissances de 5 &#8230;