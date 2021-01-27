---
title: Traduire un string grâce à Google Traduction en Python (for free)
author: Robin Pourtaud
type: post
date: 2020-05-12T19:48:34+00:00
url: /sciences/informatique/robin/1933/
featured_image: /wp-content/uploads/2020/05/GoogleTrad-1568x825.png
rank_math_seo_score:
  - "68"
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
  - Traduire
rank_math_analytic_object_id:
  - "75"
categories:
  - Informatique
tags:
  - Google Traduction
  - Jupyter Notebook
  - Python
  - Tutoriel

---
Traduire du texte est quelque chose de complexe, demandant beaucoup de données et de ressources. C&rsquo;est pourquoi, il n&rsquo;est pas possible (difficile) de programmer soit même un algorithme performant de traduction. 

La méthode la plus simple est encore de se relayer sur la puissance de Google. Google, ou plutôt Google Cloud propose un API, l&rsquo;API **Google Cloud Translation**. Cet API, bien que très pratique, pose un certain problème, celui du **prix** : [20$ pour 1 million de caractères][1]{.rank-math-link.rank-math-link}. Bien que plutôt rentable pour de nombreux projets, si, comme moi, vous n&rsquo;avez pas besoin d&rsquo;utiliser autant de caractères, il serait intéressant de trouver une alternative **gratuite**. Et c&rsquo;est pour cela que je vous propose cet article ! 

Pour ce tutoriel, j&rsquo;utiliserai [Colab Research][2]{.rank-math-link}, le Jupyter Notebook de Google.

## Nécessaire : 

Pour suivre ce tutoriel vous avez 2 possibilités : 

  * Vous utilisez un Jupyter Notebook en ligne tel que celui de [Google][2]{.rank-math-link} ou de [Microsoft][3]{.rank-math-link}, qui proposent une solution rapide et pré-configurée.
  * Ou, un ordinateur avec **python** et **pip** correctement installé.

## Installation de la bibliothèque :

Pour ce projet, on va utiliser la bibliothèque (library) « googletrans ». Trouvable [ici][4]{.rank-math-link}.

(si vous utilisez votre terminal) Pour l&rsquo;installer, utilisez la formule magique habituelle : 

<pre class="wp-block-code" aria-describedby="shcb-language-58" data-shcb-language-name="Bash" data-shcb-language-slug="bash"><div>
  <code class="hljs language-bash">sudo pip install googletrans</code>
</div>

<small class="shcb-language" id="shcb-language-58"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Bash</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">bash</span><span class="shcb-language__paren">)</span></small></pre>

Si vous voulez l&rsquo;installer depuis Jupyter Notebook : 

<pre class="wp-block-code"><div>
  <code class="hljs">!pip install -q googletrans</code>
</div></pre>

## Utilisation de googletrans : 

Je vous propose un code tout simple qui traduit le mot « hello world » en « bonjour le monde » : 

<pre class="wp-block-code" aria-describedby="shcb-language-59" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">&lt;span class="hljs-keyword">from&lt;/span> googletrans &lt;span class="hljs-keyword">import&lt;/span> Translator
  
  tr = Translator()
  output = tr.translate(&lt;span class="hljs-string">'hello world'&lt;/span>,src=&lt;span class="hljs-string">'en'&lt;/span>,dest=&lt;span class="hljs-string">'fr'&lt;/span>).text
  
  print(output)</code>
</div>

<small class="shcb-language" id="shcb-language-59"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Comme on peut s&rsquo;en douter, print(output) retourne bien « bonjour le monde ».

Mais googletrans permet des choses plus folles ! Il permet de detecter automatiquement la langue ! 

<pre class="wp-block-code" aria-describedby="shcb-language-60" data-shcb-language-name="Python" data-shcb-language-slug="python"><div>
  <code class="hljs language-python">&lt;span class="hljs-keyword">from&lt;/span> googletrans &lt;span class="hljs-keyword">import&lt;/span> Translator
  
  tr = Translator()
  output = tr.translate(&lt;span class="hljs-string">'Chaton'&lt;/span>).text
  
  print(output)</code>
</div>

<small class="shcb-language" id="shcb-language-60"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">Python</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">python</span><span class="shcb-language__paren">)</span></small></pre>

Ce code affichera donc « Kitten », étant donné que &lsquo;dest&rsquo; est par défaut égal à &lsquo;eng&rsquo;.

## Sources : 

  * <https://pypi.org/project/googletrans/>
  * <https://colab.research.google.com/notebooks/snippets/importing_libraries.ipynb>
  * <https://notebooks.azure.com/help/jupyter-notebooks/package-installation>

 [1]: https://cloud.google.com/translate/pricing
 [2]: https://colab.research.google.com/
 [3]: https://notebooks.azure.com/
 [4]: https://pypi.org/project/googletrans/