---
title: ISETL – Boucle While et boucle For
author: Robin Pourtaud
type: post
date: 2020-07-27T09:06:45+00:00
url: /sciences/informatique/robin/3869/
featured_image: /wp-content/uploads/2020/07/boucle-1568x611.png
rank_math_seo_score:
  - "70"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - ISETL
rank_math_analytic_object_id:
  - "29"
categories:
  - Informatique
tags:
  - ISETL
  - Tutoriel

---
_Interactive SET Language (ISETL) est un langage de programmation basé sur SETL. Développé par Garry Levin en 1988, il avait pour finalité&nbsp;_**l’enseignement des mathématiques discrètes à l’université**_.&nbsp;Cet article est à destination des étudiants voulant apprendre à rédiger des boucles While et For en ISETL._

## Boucle While

### Définition : 

Une boucle « While », ou boucle « Tant Que » permet de répéter l&rsquo;exécution d&rsquo;une portion de code tant qu&rsquo;une condition est « Vrai ».

En ISETL, une boucle « While » se rédige de cette façon : 

### Exemple : 

On veut se compliquer la vie et afficher 3 fois « true » avec une boucle « While » : 

<pre class="wp-block-code" aria-describedby="shcb-language-114" data-shcb-language-name="PHP" data-shcb-language-slug="php"><div>
  <code class="hljs language-php">x := &lt;span class="hljs-keyword">true&lt;/span>;
  i := &lt;span class="hljs-number">0&lt;/span>;
  &lt;span class="hljs-keyword">while&lt;/span> x &lt;span class="hljs-keyword">do&lt;/span> 
    i:=i+&lt;span class="hljs-number">1&lt;/span>;
    &lt;span class="hljs-keyword">print&lt;/span>(x);
    &lt;span class="hljs-keyword">if&lt;/span> i &gt; &lt;span class="hljs-number">2&lt;/span> then 
      x:=&lt;span class="hljs-keyword">false&lt;/span>;
    end &lt;span class="hljs-keyword">if&lt;/span>
  end &lt;span class="hljs-keyword">while&lt;/span>;</code>
</div>

<small class="shcb-language" id="shcb-language-114"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PHP</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">php</span><span class="shcb-language__paren">)</span></small></pre><figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="456" src="https://keskec.fr/wp-content/uploads/2020/07/image-15-1024x456.png" alt="" class="wp-image-3873" srcset="https://keskec.fr/wp-content/uploads/2020/07/image-15-1024x456.png 1024w, https://keskec.fr/wp-content/uploads/2020/07/image-15-300x134.png 300w, https://keskec.fr/wp-content/uploads/2020/07/image-15-768x342.png 768w, https://keskec.fr/wp-content/uploads/2020/07/image-15-1536x684.png 1536w, https://keskec.fr/wp-content/uploads/2020/07/image-15-2048x912.png 2048w, https://keskec.fr/wp-content/uploads/2020/07/image-15-1568x698.png 1568w, https://keskec.fr/wp-content/uploads/2020/07/image-15-150x67.png 150w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Boucle While ISETL</figcaption></figure> 

## Boucle For

### Définition : 

Une boucle « For » est un type de boucle While se servant **d&rsquo;un compteur et d&rsquo;une condition** tel que ce compteur ne doit pas rendre cette **condition fausse.** 

En ISETL, une boucle For se rédige de cette façon :

<pre class="wp-block-code" aria-describedby="shcb-language-115" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">for &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">variable&lt;/span>&gt;&lt;/span> in &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">tuple&lt;/span>&gt;&lt;/span> do
  &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">code&lt;/span>&gt;&lt;/span>
  end for;
  </code>
</div>

<small class="shcb-language" id="shcb-language-115"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

### Exemple : 

On veut afficher tous les carrés des éléments de 0 à 9 d&rsquo;un tuple : 

<pre class="wp-block-code" aria-describedby="shcb-language-116" data-shcb-language-name="PHP" data-shcb-language-slug="php"><div>
  <code class="hljs language-php">E:=[&lt;span class="hljs-number">0.&lt;/span>&lt;span class="hljs-number">.9&lt;/span>];
  &lt;span class="hljs-keyword">for&lt;/span> i in E &lt;span class="hljs-keyword">do&lt;/span> &lt;span class="hljs-keyword">print&lt;/span>(i**&lt;span class="hljs-number">2&lt;/span>);
  end &lt;span class="hljs-keyword">for&lt;/span>;</code>
</div>

<small class="shcb-language" id="shcb-language-116"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">PHP</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">php</span><span class="shcb-language__paren">)</span></small></pre><figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="473" src="https://keskec.fr/wp-content/uploads/2020/07/image-14-1024x473.png" alt="" class="wp-image-3872" srcset="https://keskec.fr/wp-content/uploads/2020/07/image-14-1024x473.png 1024w, https://keskec.fr/wp-content/uploads/2020/07/image-14-300x139.png 300w, https://keskec.fr/wp-content/uploads/2020/07/image-14-768x355.png 768w, https://keskec.fr/wp-content/uploads/2020/07/image-14-1536x709.png 1536w, https://keskec.fr/wp-content/uploads/2020/07/image-14-2048x946.png 2048w, https://keskec.fr/wp-content/uploads/2020/07/image-14-1568x724.png 1568w, https://keskec.fr/wp-content/uploads/2020/07/image-14-150x69.png 150w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Carrés des valeurs d&rsquo;un tuple</figcaption></figure> 

## Plus d&rsquo;ISETL ? 

<p class="has-text-align-center">
  <a href="https://keskec.fr/tag/isetl/" class="rank-math-link">KeskeC &#8211; ISETL</a>
</p>