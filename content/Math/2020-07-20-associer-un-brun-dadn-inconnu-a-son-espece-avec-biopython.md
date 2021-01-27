---
title: 'Associer un brun d&rsquo;ADN inconnu à son éspèce avec BioPython'
author: Robin Pourtaud
type: post
date: 2020-07-20T16:33:30+00:00
draft: true
private: true
url: /sciences/informatique/robin/3777/
rank_math_primary_category:
  - "8"
rank_math_seo_score:
  - "68"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_focus_keyword:
  - BioPython
categories:
  - Biologie
  - Informatique
tags:
  - Data-Science
  - Jupyter Notebook
  - Numpy
  - Python

---
blablabla

## Prérequis : 

Pour pouvoir suivre ce tutoriel, il est nécessaire d&rsquo;avoir installer Python3 sur son ordinateur et d&rsquo;avoir accès à pip ou pip3. 

Pour ma part, j&rsquo;utiliserais [un jupyter notebook depuis Visual Studio Code][1]{.rank-math-link}. 

## Installer BioPython : 

Il existe deux moyen d&rsquo;installer biopython, l&rsquo;un de façon classique, depuis un terminal, l&rsquo;autre depuis Jupyter Notebook : 

### Depuis un terminal : 

Depuis le terminal, rien de plus simple, il suffit de rentrer la commande suivante : 

<pre class="wp-block-code"><div>
  <code class="hljs">pip install biopython</code>
</div></pre>

En fonction de votre version de pip, il se peut qu&rsquo;il faille utiliser pip3. 

<pre class="wp-block-code"><div>
  <code class="hljs">pip3 install biopython</code>
</div></pre><figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="214" src="https://keskec.fr/wp-content/uploads/2020/07/image-1-1024x214.png" alt="" class="wp-image-3778" srcset="https://keskec.fr/wp-content/uploads/2020/07/image-1-1024x214.png 1024w, https://keskec.fr/wp-content/uploads/2020/07/image-1-300x63.png 300w, https://keskec.fr/wp-content/uploads/2020/07/image-1-768x160.png 768w, https://keskec.fr/wp-content/uploads/2020/07/image-1-1536x321.png 1536w, https://keskec.fr/wp-content/uploads/2020/07/image-1-2048x427.png 2048w, https://keskec.fr/wp-content/uploads/2020/07/image-1-1568x327.png 1568w, https://keskec.fr/wp-content/uploads/2020/07/image-1-150x31.png 150w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Installation de BioPython</figcaption></figure> 

### Depuis Jupyter Notebook : 

De facon analogue à l&rsquo;installation dans un terminal, pour éxecuter une commande bash sur un jupyter notebook, il suffit de rentrer : 

<pre class="wp-block-code"><div>
  <code class="hljs">!pip install biopython</code>
</div></pre>

ou : 

<pre class="wp-block-code"><div>
  <code class="hljs">!pip3 install biopython</code>
</div></pre>

##

 [1]: https://code.visualstudio.com/docs/python/jupyter-supp