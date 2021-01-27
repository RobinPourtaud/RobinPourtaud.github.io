---
title: 'Différents types d&rsquo;automates finis'
author: Robin Pourtaud
type: post
date: 2020-12-11T09:57:52+00:00
url: /sciences/informatique/robin/4870/
featured_image: /wp-content/uploads/2020/12/Images-KeskeC-3-1568x882.png
rank_math_seo_score:
  - "80"
ads-for-wp-visibility:
  - show
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - automate
categories:
  - Informatique
tags:
  - Automate
  - Graphe

---
Cet article présente un ensemble de propriétés concernant les automates finis. Pour mieux comprendre ces définitions, chaque type d&rsquo;AFN sera illustré d&rsquo;exemples générés grâce au logiciel Jflap. Les définitions formelles ne sont pas explicitées dans cet article mais sont disponibles via les liens sources. 

## Définitions : 

### Automate déterministe

Un automate est dit déterministe si il respecte trois conditions : 

  1. Il possède un unique état initial.
  2. Il ne possède pas d&rsquo;epsilon-transitions.
  3. Pour chaque état de cet automate, il existe au maximum une transition issue de cet état possédant le même symbole.

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-1-edited.png" alt="" class="wp-image-4889" width="281" height="281" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-1-edited.png 473w, https://keskec.fr/wp-content/uploads/2020/12/image-1-edited-300x300.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-1-edited-150x150.png 150w" sizes="(max-width: 281px) 100vw, 281px" /><figcaption>N&rsquo;est pas un AFD</figcaption></figure>
</div>

Attention : Un automate fini est toujours un AFN (automate fini non déterministe). Un automate fini déterministe (AFD) est un AFN particulier.

### Automate complet

Un automate fini est dit complet si : 

  1. Depuis n&rsquo;importe quel état, tous les symboles de l&rsquo;alphabet doivent appartenir au moins une fois aux transitions (sortantes). 

Par exemple pour l&rsquo;alphabet {a,b,c} : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-12.png" alt="" class="wp-image-4908" width="375" height="258" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-12.png 838w, https://keskec.fr/wp-content/uploads/2020/12/image-12-300x207.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-12-768x529.png 768w" sizes="(max-width: 375px) 100vw, 375px" /><figcaption>Automate fini non complet</figcaption></figure>
</div>

Cet automate n&rsquo;est pas complet car on ne peut pas obtenir le symbole « a » depuis q2. 

Pour obtenir un automate équivalent, complet, il suffit de créer un état « puits », ou état « poubelle ». Comme suit : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-14.png" alt="" class="wp-image-4912" width="286" height="202" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-14.png 831w, https://keskec.fr/wp-content/uploads/2020/12/image-14-300x213.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-14-768x545.png 768w" sizes="(max-width: 286px) 100vw, 286px" /><figcaption>Automate fini complet</figcaption></figure>
</div>

### Automate émondé

Un automate est dit émondé (ou utile) si tous les états de cet automate peuvent former au moins un mot du langage. 

Par exemple : Cet automate est fini émondé. q0, q1 et q3 peuvent servir tous les 3 à la création du langage.

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-6.png" alt="" class="wp-image-4895" width="408" height="199" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-6.png 754w, https://keskec.fr/wp-content/uploads/2020/12/image-6-300x146.png 300w" sizes="(max-width: 408px) 100vw, 408px" /><figcaption>Automate fini émondé</figcaption></figure>
</div>

Cependant celui là ne l&rsquo;est pas : l&rsquo;état q1 n&rsquo;est plus « utile ». 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-7.png" alt="" class="wp-image-4896" width="406" height="184" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-7.png 792w, https://keskec.fr/wp-content/uploads/2020/12/image-7-300x136.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-7-768x347.png 768w" sizes="(max-width: 406px) 100vw, 406px" /><figcaption>Automate non émondé</figcaption></figure>
</div>

### Automate unitaire

Un automate est dit unitaire si il possède un unique état initial.

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image.png" alt="" class="wp-image-4886" width="469" height="272" srcset="https://keskec.fr/wp-content/uploads/2020/12/image.png 942w, https://keskec.fr/wp-content/uploads/2020/12/image-300x174.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-768x446.png 768w" sizes="(max-width: 469px) 100vw, 469px" /><figcaption>Automate unitaire</figcaption></figure>
</div>

### Automate standard

Un automate est dit standard si : 

  1. Il est unitaire (un seul état initial)
  2. Il n&rsquo;existe pas de transitions allant sur cet état initial

Par exemple, ceci n&rsquo;est pas un automate standard : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-8-1024x317.png" alt="" class="wp-image-4899" width="447" height="138" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-8-1024x317.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-8-300x93.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-8-768x238.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-8.png 1284w" sizes="(max-width: 447px) 100vw, 447px" /><figcaption>Automate non standard</figcaption></figure>
</div>

Mais celui là l&rsquo;est : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-9-1024x282.png" alt="" class="wp-image-4900" width="387" height="106" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-9-1024x282.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-9-300x83.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-9-768x212.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-9.png 1233w" sizes="(max-width: 387px) 100vw, 387px" /><figcaption>Automate standard</figcaption></figure>
</div>

### Automate normalisé

Un automate est dit normalisé si : 

  1. Il est standard (aucune transition vers l&rsquo;unique état initial).
  2. Il possède un unique état final 
  3. Aucune transition n&rsquo;a pour origine l&rsquo;état final (on ne peut pas en sortir). 

Par exemple cet automate n&rsquo;est pas normalisé : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-10-1024x676.png" alt="" class="wp-image-4901" width="307" height="203" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-10-1024x676.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-10-300x198.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-10-768x507.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-10.png 1226w" sizes="(max-width: 307px) 100vw, 307px" /><figcaption>Automate non-normalisé</figcaption></figure>
</div>

Cet automate est normalisé : 

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/12/image-11-1024x654.png" alt="" class="wp-image-4902" width="305" height="195" srcset="https://keskec.fr/wp-content/uploads/2020/12/image-11-1024x654.png 1024w, https://keskec.fr/wp-content/uploads/2020/12/image-11-300x191.png 300w, https://keskec.fr/wp-content/uploads/2020/12/image-11-768x490.png 768w, https://keskec.fr/wp-content/uploads/2020/12/image-11.png 1487w" sizes="(max-width: 305px) 100vw, 305px" /><figcaption>Automate normalisé</figcaption></figure>
</div>

## Sources : 

  1. [Deterministic finite automaton &#8211; Wikipédia][1]{.rank-math-link}
  2. [Nondeterministic finite automaton &#8211; Wikipédia][2]{.rank-math-link}
  3. [automate normalisé &#8211; math.cheredeprince.net][3]{.rank-math-link}
  4. [séquence 209\_5\_7 &#8211; desmontils.net][4]
  5. [Automate déterministe &#8211; momirandum.com][5]{.rank-math-link}
  6. [Automate standard &#8211; momirandum.com][6]{.rank-math-link}
  7. [Complétion &#8211; Etat poubelle][7]{.rank-math-link}

 [1]: https://en.wikipedia.org/wiki/Deterministic_finite_automaton
 [2]: https://en.wikipedia.org/wiki/Nondeterministic_finite_automaton
 [3]: https://math.cheredeprince.net/elt/automate_normalise#!aside=opened&elts=set:automate_normalise,1
 [4]: http://www.desmontils.net/emiage/Module209EMiage/c5/Ch5_7.htm
 [5]: http://www.momirandum.com/automates-finis/Automatedeterministe.html
 [6]: http://www.momirandum.com/automates-finis/Automatestandard.html
 [7]: http://www.momirandum.com/automates-finis/CompletionEtatpoubelle.html