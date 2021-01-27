---
title: Opération sur les matrices avec numpy en Python
author: Robin Pourtaud
type: post
date: 2020-05-18T10:00:00+00:00
url: /sciences/informatique/robin/2057/
featured_image: /wp-content/uploads/2020/05/numpy-1568x711.png
rank_math_seo_score:
  - "78"
itemlist_item_1877:
  - 'a:0:{}'
music_composer_1877:
  - 'a:0:{}'
movie_actor_1877:
  - 'a:0:{}'
article_items_1877:
  - 'a:0:{}'
image_object_exif_data_1877:
  - 'a:0:{}'
blogposting_items_1877:
  - 'a:0:{}'
newsarticle_items_1877:
  - 'a:0:{}'
tech_article_items_1877:
  - 'a:0:{}'
product_reviews_1877:
  - 'a:0:{}'
feed_element_1877:
  - 'a:0:{}'
faq_question_1877:
  - 'a:0:{}'
performer_1877:
  - 'a:0:{}'
accepted_answer_1877:
  - 'a:0:{}'
suggested_answer_1877:
  - 'a:0:{}'
howto_supply_1877:
  - 'a:0:{}'
howto_tool_1877:
  - 'a:0:{}'
howto_step_1877:
  - 'a:0:{}'
announcement_location_1877:
  - 'a:0:{}'
music_playlist_track_1877:
  - 'a:0:{}'
music_album_track_1877:
  - 'a:0:{}'
apartment_amenities_1877:
  - 'a:0:{}'
additional_property_1877:
  - 'a:0:{}'
mc_cause_1877:
  - 'a:0:{}'
mc_symptom_1877:
  - 'a:0:{}'
mc_risk_factor_1877:
  - 'a:0:{}'
tvseries_actor_1877:
  - 'a:0:{}'
tvseries_season_1877:
  - 'a:0:{}'
trip_itinerary_1877:
  - 'a:0:{}'
itemlist_item_1494:
  - 'a:0:{}'
music_composer_1494:
  - 'a:0:{}'
movie_actor_1494:
  - 'a:0:{}'
article_items_1494:
  - 'a:0:{}'
image_object_exif_data_1494:
  - 'a:0:{}'
blogposting_items_1494:
  - 'a:0:{}'
newsarticle_items_1494:
  - 'a:0:{}'
tech_article_items_1494:
  - 'a:0:{}'
product_reviews_1494:
  - 'a:0:{}'
feed_element_1494:
  - 'a:0:{}'
faq_question_1494:
  - 'a:0:{}'
performer_1494:
  - 'a:0:{}'
accepted_answer_1494:
  - 'a:0:{}'
suggested_answer_1494:
  - 'a:0:{}'
howto_supply_1494:
  - 'a:0:{}'
howto_tool_1494:
  - 'a:0:{}'
howto_step_1494:
  - 'a:0:{}'
announcement_location_1494:
  - 'a:0:{}'
music_playlist_track_1494:
  - 'a:0:{}'
music_album_track_1494:
  - 'a:0:{}'
apartment_amenities_1494:
  - 'a:0:{}'
additional_property_1494:
  - 'a:0:{}'
mc_cause_1494:
  - 'a:0:{}'
mc_symptom_1494:
  - 'a:0:{}'
mc_risk_factor_1494:
  - 'a:0:{}'
tvseries_actor_1494:
  - 'a:0:{}'
tvseries_season_1494:
  - 'a:0:{}'
trip_itinerary_1494:
  - 'a:0:{}'
itemlist_item_1493:
  - 'a:0:{}'
music_composer_1493:
  - 'a:0:{}'
movie_actor_1493:
  - 'a:0:{}'
article_items_1493:
  - 'a:0:{}'
image_object_exif_data_1493:
  - 'a:0:{}'
blogposting_items_1493:
  - 'a:0:{}'
newsarticle_items_1493:
  - 'a:0:{}'
tech_article_items_1493:
  - 'a:0:{}'
product_reviews_1493:
  - 'a:0:{}'
feed_element_1493:
  - 'a:0:{}'
faq_question_1493:
  - 'a:0:{}'
performer_1493:
  - 'a:0:{}'
accepted_answer_1493:
  - 'a:0:{}'
suggested_answer_1493:
  - 'a:0:{}'
howto_supply_1493:
  - 'a:0:{}'
howto_tool_1493:
  - 'a:0:{}'
howto_step_1493:
  - 'a:0:{}'
announcement_location_1493:
  - 'a:0:{}'
music_playlist_track_1493:
  - 'a:0:{}'
music_album_track_1493:
  - 'a:0:{}'
apartment_amenities_1493:
  - 'a:0:{}'
additional_property_1493:
  - 'a:0:{}'
mc_cause_1493:
  - 'a:0:{}'
mc_symptom_1493:
  - 'a:0:{}'
mc_risk_factor_1493:
  - 'a:0:{}'
tvseries_actor_1493:
  - 'a:0:{}'
tvseries_season_1493:
  - 'a:0:{}'
trip_itinerary_1493:
  - 'a:0:{}'
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - Matrice
rank_math_analytic_object_id:
  - "71"
categories:
  - Informatique
  - Mathématiques
tags:
  - Algèbre Linéaire
  - Matrice
  - Numpy
  - Python
  - Tutoriel

---
Effectuer des calculs sur les matrices est, souvent, une opération fastidieuse et source de nombreuses erreurs. L&rsquo;algorithme naïf de multiplication de matrice possède, par exemple, une complexité cubique, rendant le calcul manuel de grandes matrices vite impossible. Utiliser un ordinateur pour effectuer ce genre de calculs me semble donc une bonne chose à faire. Pour aujourd&rsquo;hui, je vais vous présenter quelques fonctions en python, permettant d&rsquo;effectuer des opérations sur les matrices en juste quelques lignes de codes.

## Importer numpy

Avant toute chose, pour effectuer des calculs scientifiques, vous devez importer la bibliothèque numpy.

<pre class="wp-block-code" aria-describedby="shcb-language-61" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">&lt;span class="hljs-keyword">import&lt;/span> numpy &lt;span class="hljs-keyword">as&lt;/span> np </code>
</div>

<small class="shcb-language" id="shcb-language-61"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Addition et Multiplication de Matrices

<pre class="wp-block-code" aria-describedby="shcb-language-62" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  M2 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">2.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  MResultAdd = np.add(M1,M2)
  MResultSous = np.subtract(M1,M2)
  MResultMulti = M1.dot(M2)</code>
</div>

<small class="shcb-language" id="shcb-language-62"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Trace de Matrices

La trace d&rsquo;une matrice est la somme des valeurs de la diagonale de la matrice.

<pre class="wp-block-code" aria-describedby="shcb-language-63" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])</code>
</div>

<small class="shcb-language" id="shcb-language-63"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Déterminant de Matrices

Le calcul du déterminant d&rsquo;une matrice est un outil nécessaire en algèbre linéaire afin de vérifier une inversibilité ou pour calculer l&rsquo;inverse d&rsquo;une matrice. (Wikipédia)

<pre class="wp-block-code" aria-describedby="shcb-language-64" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  Determinant = np.linalg.det(M1)</code>
</div>

<small class="shcb-language" id="shcb-language-64"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Transposée de Matrices

La transposée d&rsquo;une matrice A est une matrice B telle que les colonnes et lignes de la matrice A deviennent respectivement les lignes et colonnes de la matrice B. 

<pre class="wp-block-code" aria-describedby="shcb-language-65" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">2.&lt;/span>],
                  [&lt;span class="hljs-number">6.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  Transpose = M1.transpose()</code>
</div>

<small class="shcb-language" id="shcb-language-65"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Inverse de Matrices



L&rsquo;inverse de matrice prend toute son utilité dans le calcul de systèmes linéaires. Si<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-99432eb5e1aa2dcc98e99a34b336a4fb_l3.svg" class="ql-img-inline-formula " alt="&#65;&#120;&#61;&#66;" title="Rendered by QuickLaTeX.com" height="15" width="69" style="vertical-align: 0px;" /> , alors<img loading="lazy" src="https://keskec.fr/wp-content/ql-cache/quicklatex.com-7539f758f72e16959d45acbcbde31cce_l3.svg" class="ql-img-inline-formula " alt="&#120;&#61;&#65;&#94;&#123;&#45;&#49;&#125;&#66;" title="Rendered by QuickLaTeX.com" height="17" width="90" style="vertical-align: 0px;" /> .

Une matrice A admet une inverse si et seulement si son déterminant est différent de 0. Il est donc important de le tester au préalable :). 

<pre class="wp-block-code" aria-describedby="shcb-language-66" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">2.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">5.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  Inverse = np.linalg.inv(M1)</code>
</div>

<small class="shcb-language" id="shcb-language-66"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

## Valeurs propres et Vecteurs propres de Matrices

Veuillez bien prendre en compte le fait que les vecteurs propres ne sont pas uniques, l&rsquo;échelle (la longueur), le signe, ou l&rsquo;ordre peuvent être [différents][1]{.rank-math-link}.

<pre class="wp-block-code" aria-describedby="shcb-language-67" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">2.&lt;/span>],
                  [&lt;span class="hljs-number">6.&lt;/span>,&lt;span class="hljs-number">3.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>],
                  [&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>,&lt;span class="hljs-number">1.&lt;/span>]])
  Eig = np.linalg.eig(M1)</code>
</div>

<small class="shcb-language" id="shcb-language-67"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Pour en savoir plus sur le sujet, je vous renvoie vers mon article sur [les valeurs et vecteurs propres][2]{.rank-math-link}.

## Décomposition de Cholesky de Matrices

La décomposition de Cholesky permet de décomposer une matrice symétrique définie positive en un produit d&rsquo;une matrice L par sa transposée.

<pre class="wp-block-code" aria-describedby="shcb-language-68" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">2&lt;/span>],
                  [&lt;span class="hljs-number">2&lt;/span>,&lt;span class="hljs-number">7&lt;/span>] ])
  np.linalg.cholesky(M1)</code>
</div>

<small class="shcb-language" id="shcb-language-68"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Le résultat de np.linalg.cholesky(M1) sera cette matrice L.

Pour en savoir plus sur l&rsquo;utilité et le calcul de la matrice de Cholesky, [c&rsquo;est ici][3]{.rank-math-link}. 

## Conditionnement de Matrice

Pour définir correctement le conditionnement d&rsquo;une matrice, je vous suggère [mon article sur ce sujet][4]{.rank-math-link}. 

<pre class="wp-block-code" aria-describedby="shcb-language-69" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">2&lt;/span>,&lt;span class="hljs-number">1&lt;/span>],
                  [&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">5&lt;/span>,&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">5&lt;/span>],
                  [&lt;span class="hljs-number">8&lt;/span>,&lt;span class="hljs-number">6&lt;/span>,&lt;span class="hljs-number">10&lt;/span>,&lt;span class="hljs-number">9&lt;/span>],
                  [&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">5&lt;/span>,&lt;span class="hljs-number">9&lt;/span>,&lt;span class="hljs-number">1&lt;/span>] ])
  Cond = np.linalg.cond(M1)</code>
</div>

<small class="shcb-language" id="shcb-language-69"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Par défaut, np.linalg.cond **n&rsquo;utilise pas la norme infinie.** Si vous souhaitez l&rsquo;utiliser, je vous propose de rajouter cette option : 

<pre class="wp-block-code" aria-describedby="shcb-language-70" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">M1 = np.array([ [&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">2&lt;/span>,&lt;span class="hljs-number">1&lt;/span>],
                  [&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">5&lt;/span>,&lt;span class="hljs-number">1&lt;/span>,&lt;span class="hljs-number">5&lt;/span>],
                  [&lt;span class="hljs-number">8&lt;/span>,&lt;span class="hljs-number">6&lt;/span>,&lt;span class="hljs-number">10&lt;/span>,&lt;span class="hljs-number">9&lt;/span>],
                  [&lt;span class="hljs-number">7&lt;/span>,&lt;span class="hljs-number">5&lt;/span>,&lt;span class="hljs-number">9&lt;/span>,&lt;span class="hljs-number">1&lt;/span>] ])
  Cond = np.linalg.cond(M1,np.inf)</code>
</div>

<small class="shcb-language" id="shcb-language-70"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Pour plus de paramètres, c&rsquo;est [ici.][5]{.rank-math-link}

## Pour aller plus loin&#8230;.

Numpy propose encore un nombre très important de fonctions relatives aux matrices&#8230;. 

Ici se trouvent par exemple un certain nombre d&rsquo;entre-elles : <https://docs.scipy.org/doc/numpy/reference/routines.linalg.html>{.rank-math-link}

## Sources : 

  * <https://docs.scipy.org/doc/numpy/reference/routines.linalg.html?highlight=determinant>
  * [https://www.researchgate.net/post/Why\_eigenvectors\_seem\_incorrect\_in_python][1]

 [1]: https://www.researchgate.net/post/Why_eigenvectors_seem_incorrect_in_python
 [2]: https://keskec.fr/sciences/mathematiques/robin/684/
 [3]: https://keskec.fr/sciences/mathematiques/robin/622/
 [4]: https://keskec.fr/sciences/informatique/robin/57/
 [5]: https://docs.scipy.org/doc/numpy/reference/generated/numpy.linalg.cond.html#numpy.linalg.cond