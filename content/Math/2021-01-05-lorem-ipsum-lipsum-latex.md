---
title: Lorem Ipsum (lipsum) – Latex
author: Robin Pourtaud
type: post
date: 2021-01-05T20:17:24+00:00
url: /sciences/informatique/robin/5030/
featured_image: /wp-content/uploads/2020/12/Lorem-Ipsum-1568x768.png
rank_math_seo_score:
  - "86"
rank_math_primary_category:
  - "8"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - Lorem Ipsum
categories:
  - Informatique
tags:
  - LaTeX

---
Cet article présente la façon la plus courante de générer un Lorem Ipsum (ou faux-texte) en Latex. 

## Utilisation 

### Importation de lipsum

Afin de générer ce faux-texte, vous devez avoir importé le package « lipsum » : 

<pre class="wp-block-code" aria-describedby="shcb-language-125" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">usepackage&lt;/span>&lt;span class="hljs-string">{lipsum}&lt;/span>&lt;/span> </code>
</div>

<small class="shcb-language" id="shcb-language-125"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

### Exemple d&rsquo;utilisation 

La syntaxe de la commande utilisateur est la suivante : 

<pre class="wp-block-code" aria-describedby="shcb-language-126" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">lipsum&lt;/span>&lt;span class="hljs-string">[&lt;paragraph range&gt;]&lt;/span>&lt;span class="hljs-string">[&lt;sentence range&gt;]&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-126"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

  * « Paragraph range » fait référence aux paragraphes du Lipsum souhaité (150 étant la valeur maximum).
  * « Sentence range » fait référence aux phrases du Lipsum correspondant au paragraphe voulu. Ce paramètre nécessite une valeur non nulle du premier paramètre. 

Les 2 paramètres sont optionnels.

#### Exemple 1

La commande « \lipsum » génère par défaut les paragraphes 1 à 7 du Lipsum : 

<pre class="wp-block-code" aria-describedby="shcb-language-127" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">lipsum&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-127"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

#### Exemple 2

Pour générer un Lipsum contenant les 2 premiers paragraphes, vous pouvez utiliser la commande : 

<pre class="wp-block-code" aria-describedby="shcb-language-128" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">lipsum&lt;/span>&lt;span class="hljs-string">[1-2]&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-128"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-20-1024x686.png" alt="" class="wp-image-5032" width="437" height="292" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-20-1024x686.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-20-300x201.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-20-768x515.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-20.png 1103w" sizes="(max-width: 437px) 100vw, 437px" /><figcaption>2 premiers paragraphes lipsum</figcaption></figure>
</div>

#### Exemple 3

Pour afficher la première phrase du premier paragraphe, vous pouvez utiliser la commande suivante : 

<pre class="wp-block-code" aria-describedby="shcb-language-129" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">lipsum&lt;/span>&lt;span class="hljs-string">[1]&lt;/span>&lt;span class="hljs-string">[1]&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-129"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

Le résultat étant le suivant : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-22.png" alt="" class="wp-image-5037" width="459" height="59" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-22.png 826w, https://keskec.fr/wp-content/uploads/2020/12/image-22-300x38.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-22-768x99.png 768w" sizes="(max-width: 459px) 100vw, 459px" /><figcaption>Lorem Ipsum première phrase</figcaption></figure>
</div>

## Alternative : 

Le paquet blindtext propose un résultat similaire : 

<pre class="wp-block-code" aria-describedby="shcb-language-130" data-shcb-language-name="TeX" data-shcb-language-slug="tex"><div>
  <code class="hljs language-tex">&lt;span class="hljs-tag">\&lt;span class="hljs-name">usepackage&lt;/span>&lt;span class="hljs-string">{blindtext}&lt;/span>&lt;/span>
  ...
  &lt;span class="hljs-tag">\&lt;span class="hljs-name">blindtext&lt;/span>&lt;span class="hljs-string">[1]&lt;/span>&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-130"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">TeX</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">tex</span><span class="shcb-language__paren">)</span></small></pre>

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-21-1024x414.png" alt="" class="wp-image-5036" width="405" height="164" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-21-1024x414.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-21-300x121.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-21-768x311.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-21.png 1050w" sizes="(max-width: 405px) 100vw, 405px" /><figcaption>blindtext[1]</figcaption></figure>
</div>

Pour en savoir plus : [Blindtext][1]{.rank-math-link}

## Sources : 

  * [Access to 150 paragraphs of Lorem Ipsum dummy text][2]{.rank-math-link}
  * [Lorem Ipsum &#8211; Wikipédia][3]{.rank-math-link}

<p class="has-text-align-center">
  <a class="rank-math-link" href="https://keskec.fr/tag/latex/">D&rsquo;autres tutoriel sur LaTeX ici</a>
</p>

 [1]: https://www.ctan.org/pkg/blindtext
 [2]: https://distrib-coffee.ipsl.jussieu.fr/pub/mirrors/ctan/macros/latex/contrib/lipsum/lipsum.pdf
 [3]: https://fr.wikipedia.org/wiki/Lorem_ipsum