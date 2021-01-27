---
title: Jupyter Lab gratuit avec Oracle Cloud
author: Robin Pourtaud
type: post
date: 2020-09-29T11:10:46+00:00
url: /sciences/informatique/robin/4461/
featured_image: /wp-content/uploads/2020/09/Capture-decran-2020-09-13-140156-1568x591.png
rank_math_seo_score:
  - "83"
rank_math_internal_links_processed:
  - "1"
ampforwp-amp-on-off:
  - default
rank_math_primary_category:
  - "8"
rank_math_focus_keyword:
  - Jupyter lab
rank_math_analytic_object_id:
  - "8"
categories:
  - Informatique
tags:
  - Jupyter Notebook
  - Linux

---
Gratuitement, de grandes entreprises (Google, IBM, Microsoft, &#8230;) proposent un accès à leur Jupyter Notebook. Jupyter Lab, cependant, ne fait pas partie de leurs offres gratuites (sans durée limitée et sans restriction conséquentes). C&rsquo;est dans cette optique que j&rsquo;ai découvert l&rsquo;accès « Always free » de Oracle, nous permettant aisément de créer notre Jupyter Lab personnel&#8230; 

## Résumé 

Oracle propose depuis bientôt un an une offre appelée « [Always Free][1]{.rank-math-link}« . Celle-ci comprend :

  * Deux bases de données Oracle Autonomous Database avec des outils puissants tels qu’Oracle Application Express (APEX) et Oracle SQL Developer
  * Deux machines virtuelles de calcul Oracle Cloud Infrastructure Compute&nbsp;; stockage de niveau bloc, objet et archive&nbsp;; équilibreur de charge et extraction de données&nbsp;; surveillance et notifications
  * Pendant les 30 premiers jours 300$ de crédit sur leur plateforme

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-7-1024x371.png" alt="" class="wp-image-4463" width="649" height="234" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-7-1024x371.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-7-300x109.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-7-768x278.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-7-1536x557.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-7-2048x742.png 2048w, https://keskec.fr/wp-content/uploads/2020/08/image-7-1568x568.png 1568w" sizes="(max-width: 649px) 100vw, 649px" /><figcaption>Source : <a class="rank-math-link" href="https://www.oracle.com/fr/cloud/free/#always-free">oracle.com</a></figcaption></figure>
</div>

La configuration des machines virtuelles est la suivante : <figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="156" src="https://keskec.fr/wp-content/uploads/2020/08/image-11-1024x156.png" alt="" class="wp-image-4467" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-11-1024x156.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-11-300x46.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-11-768x117.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-11-1536x234.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-11-1568x239.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-11.png 1872w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Machine Virtuelle AMD &#8211; Oracle Cloud</figcaption></figure> 

Si vous souhaitez une configuration plus « confortable », il sera nécessaire de passer à un plan payant après 30 jours&#8230; 

## Prérequis

Pour suivre ce tutoriel, il est nécessaire d&rsquo;avoir un accès en ssh sur son ordinateur (sous Linux, avec wsl2, avec putty&#8230;.). 

## Inscription à Oracle Cloud

Durant l&rsquo;inscription, vous aurez besoin de rentrer de nombreuses informations personnelles telles que votre adresse postale ou encore vos coordonnées de carte bleue. 

Cependant, il est important de noter que vous ne serez ni prélevé maintenant, ni au bout de 30 jours (du moins pas sans votre accord). 

Pour vous inscrire, connectez-vous ici : 

<p class="has-text-align-center">
  <a href="https://myservices.us.oraclecloud.com/mycloud/signup" class="rank-math-link">Oracle Cloud Account Signup</a>
</p>

Suivez cette inscription. Cela dure maximum 5 min. 

## Création d&rsquo;une machine virtuelle

Une fois inscrit, vous devrez vous retrouver sur cette page :

<div class="wp-block-image">
  <figure class="aligncenter size-large"><img loading="lazy" width="1024" height="397" src="https://keskec.fr/wp-content/uploads/2020/08/image-8-1024x397.png" alt="" class="wp-image-4464" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-8-1024x397.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-8-300x116.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-8-768x298.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-8-1536x595.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-8-2048x794.png 2048w, https://keskec.fr/wp-content/uploads/2020/08/image-8-1568x608.png 1568w" sizes="(max-width: 1024px) 100vw, 1024px" /><figcaption>Oracle Cloud &#8211; Accueil</figcaption></figure>
</div>

  1. Cliquez sur « Create a VM instance »
  2. Nommez votre instance du nom de votre choix
  3. Choisissez l&rsquo;image « Always free » de votre choix (la suite du tutoriel peut varier selon l&rsquo;image choisie)  
    

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-9-1024x765.png" alt="" class="wp-image-4465" width="693" height="517" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-9-1024x765.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-9-300x224.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-9-768x574.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-9-1536x1148.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-9-1568x1172.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-9.png 1942w" sizes="(max-width: 693px) 100vw, 693px" /><figcaption>Choix du système d&rsquo;exploitation &#8211; Oracle Cloud</figcaption></figure>
</div>

<ol start="4">
  <li>
    Cliquez ensuite sur « Show Shape, Network and Storage Options »
  </li>
  <li>
    Puis « Change Shape »
  </li>
  <li>
    Ensuite « Virtual Machine »
  </li>
  <li>
    Sur « Specialty and Legacy »
  </li>
  <li>
    Et sélectionnez la ressource « Always Free Eligible » comme sur l&rsquo;image ci-dessous (si aucune n&rsquo;est disponible, essayez de modifier dans la fenêtre précédente « availability domain ») :
  </li>
</ol>

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/08/image-10-1024x742.png" alt="" class="wp-image-4466" width="566" height="410" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-10-1024x742.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-10-300x217.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-10-768x556.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-10-1536x1113.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-10-1568x1136.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-10.png 1928w" sizes="(max-width: 566px) 100vw, 566px" /><figcaption>Choix de la VM &#8211; Oracle Cloud</figcaption></figure>
</div>

<ol start="9">
  <li>
    Enfin, sauvegardez la clé privée pour accéder à votre machine via ssh :
  </li>
</ol><figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="341" src="https://keskec.fr/wp-content/uploads/2020/08/image-12-1024x341.png" alt="" class="wp-image-4469" srcset="https://keskec.fr/wp-content/uploads/2020/08/image-12-1024x341.png 1024w, https://keskec.fr/wp-content/uploads/2020/08/image-12-300x100.png 300w, https://keskec.fr/wp-content/uploads/2020/08/image-12-768x256.png 768w, https://keskec.fr/wp-content/uploads/2020/08/image-12-1536x511.png 1536w, https://keskec.fr/wp-content/uploads/2020/08/image-12-1568x522.png 1568w, https://keskec.fr/wp-content/uploads/2020/08/image-12.png 1934w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Sauvegarde des clés SSH &#8211; Oracle Cloud</figcaption></figure> 

<ol start="10">
  <li>
    Vous pouvez maintenant cliquer sur « Create » !
  </li>
</ol>

## Se connecter à la machine Virtuelle via SSH

Pour vous connecter avec putty, je vous renvoie vers [ce lien][2]{.rank-math-link}.

Pour vous connecter « traditionnellement » avec un terminal, **restez ici** ! 

Rendez-vous dans la liste des instances située dans : 

<p class="has-text-align-center">
  « Menu de navigation en haut à gauche » > Compute > Instances
</p>

<div class="wp-block-image">
  <figure class="aligncenter size-large is-resized"><img loading="lazy" src="https://keskec.fr/wp-content/uploads/2020/09/image-1024x288.png" alt="" class="wp-image-4473" width="592" height="166" srcset="https://keskec.fr/wp-content/uploads/2020/09/image-1024x288.png 1024w, https://keskec.fr/wp-content/uploads/2020/09/image-300x84.png 300w, https://keskec.fr/wp-content/uploads/2020/09/image-768x216.png 768w, https://keskec.fr/wp-content/uploads/2020/09/image-1536x432.png 1536w, https://keskec.fr/wp-content/uploads/2020/09/image-2048x577.png 2048w, https://keskec.fr/wp-content/uploads/2020/09/image-1568x441.png 1568w" sizes="(max-width: 592px) 100vw, 592px" /><figcaption>Liste des Instances &#8211; Oracle Cloud</figcaption></figure>
</div>

Cliquez sur l&rsquo;instance puis copiez l&rsquo;IP public ainsi que le nom d&rsquo;utilisateur.

Vous pouvez maintenant ouvrir un terminal et vous connecter à l&rsquo;instance via SSH : 

  1. Ouvrez un terminal et allez dans le même dossier que votre « clé ».
  2. Entrez les 2 commandes suivantes : 

<pre class="wp-block-code" aria-describedby="shcb-language-122" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">chmod 500 &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">Votre&lt;/span> &lt;span class="hljs-attr">cl&lt;/span>é&gt;&lt;/span>
  ssh -i &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">Votre&lt;/span> &lt;span class="hljs-attr">cl&lt;/span>é&gt;&lt;/span> &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">nom&lt;/span> &lt;span class="hljs-attr">utilisateur&lt;/span>&gt;&lt;/span>@&lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">IP&lt;/span> &lt;span class="hljs-attr">publique&lt;/span>&gt;&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-122"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

Résultat : <figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="603" src="https://keskec.fr/wp-content/uploads/2020/09/image-2-1024x603.png" alt="" class="wp-image-4475" srcset="https://keskec.fr/wp-content/uploads/2020/09/image-2-1024x603.png 1024w, https://keskec.fr/wp-content/uploads/2020/09/image-2-300x177.png 300w, https://keskec.fr/wp-content/uploads/2020/09/image-2-768x452.png 768w, https://keskec.fr/wp-content/uploads/2020/09/image-2-1536x905.png 1536w, https://keskec.fr/wp-content/uploads/2020/09/image-2-2048x1207.png 2048w, https://keskec.fr/wp-content/uploads/2020/09/image-2-1568x924.png 1568w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Connexion via SSH &#8211; Oracle Cloud</figcaption></figure> 

## Installation de Jupyter lab

Pour installer Jupyter Lab, nous aurons besoin de pip3. Pour l&rsquo;installer : 

<pre class="wp-block-code"><div>
  <code class="hljs">sudo apt install python3-pip</code>
</div></pre>

Installons Jupyter Lab maintenant : 

<pre class="wp-block-code"><div>
  <code class="hljs">pip3 install jupyterlab </code>
</div></pre>

Après son installation, terminez votre connexion ssh puis relancez là. Vous pouvez maintenant exécuter Jupyter Lab.

## Accès à Jupyter lab 

Je vous propose de vous connecter à Jupyter Lab via un tunnel SSH, mais il est tout à fait possible de s&rsquo;y connecter via l&rsquo;IP public! Pour cela, je vous renvoie vers [la partie 2 d&rsquo;un tutoriel de Oracle][3]{.rank-math-link}. 

Dans votre terminal, commencez par taper « jupyter lab » : 

<pre class="wp-block-code"><div>
  <code class="hljs">jupyter lab</code>
</div></pre>

Comme ceci : <figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="569" src="https://keskec.fr/wp-content/uploads/2020/09/image-3-1024x569.png" alt="" class="wp-image-4521" srcset="https://keskec.fr/wp-content/uploads/2020/09/image-3-1024x569.png 1024w, https://keskec.fr/wp-content/uploads/2020/09/image-3-300x167.png 300w, https://keskec.fr/wp-content/uploads/2020/09/image-3-768x427.png 768w, https://keskec.fr/wp-content/uploads/2020/09/image-3-1536x854.png 1536w, https://keskec.fr/wp-content/uploads/2020/09/image-3-2048x1138.png 2048w, https://keskec.fr/wp-content/uploads/2020/09/image-3-1568x871.png 1568w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Lancement de Jupyter Lab &#8211; Oracle Cloud</figcaption></figure> 

Laissez ce terminal ouvert en ayant bien en tête le port sur lequel est déployé Jupyter Lab. 

Ouvrez un nouveau terminal et tapez la commande : 

<pre class="wp-block-code" aria-describedby="shcb-language-123" data-shcb-language-name="HTML, XML" data-shcb-language-slug="xml"><div>
  <code class="hljs language-xml">sudo ssh -i &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">Votre&lt;/span> &lt;span class="hljs-attr">cl&lt;/span>é&gt;&lt;/span> -L 80:localhost:&lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">Port&lt;/span> &lt;span class="hljs-attr">Jupyter&lt;/span>&gt;&lt;/span>  &lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">nom&lt;/span> &lt;span class="hljs-attr">utilisateur&lt;/span>&gt;&lt;/span>@&lt;span class="hljs-tag">&lt;&lt;span class="hljs-name">IP&lt;/span> &lt;span class="hljs-attr">publique&lt;/span>&gt;&lt;/span></code>
</div>

<small class="shcb-language" id="shcb-language-123"><span class="shcb-language__label">Code language:</span> <span class="shcb-language__name">HTML, XML</span> <span class="shcb-language__paren">(</span><span class="shcb-language__slug">xml</span><span class="shcb-language__paren">)</span></small></pre>

Cette commande permet de rediriger le port 80 de votre ordinateur vers le port jupyter de votre instance. Ainsi, ouvrez un navigateur et tapez « localhost », vous devriez être en mesure de vous connecter à Jupyter Lab ! <figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="703" src="https://keskec.fr/wp-content/uploads/2020/09/image-4-1024x703.png" alt="" class="wp-image-4522" srcset="https://keskec.fr/wp-content/uploads/2020/09/image-4-1024x703.png 1024w, https://keskec.fr/wp-content/uploads/2020/09/image-4-300x206.png 300w, https://keskec.fr/wp-content/uploads/2020/09/image-4-768x527.png 768w, https://keskec.fr/wp-content/uploads/2020/09/image-4-1536x1054.png 1536w, https://keskec.fr/wp-content/uploads/2020/09/image-4-2048x1405.png 2048w, https://keskec.fr/wp-content/uploads/2020/09/image-4-1568x1076.png 1568w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Connexion à Jupyter Lab &#8211; Oracle Cloud</figcaption></figure> 

Pour finir, récupérez sur votre premier terminal le « token » et collez-le.<figure class="wp-block-image size-large">

<img loading="lazy" width="1024" height="727" src="https://keskec.fr/wp-content/uploads/2020/09/image-5-1024x727.png" alt="" class="wp-image-4523" srcset="https://keskec.fr/wp-content/uploads/2020/09/image-5-1024x727.png 1024w, https://keskec.fr/wp-content/uploads/2020/09/image-5-300x213.png 300w, https://keskec.fr/wp-content/uploads/2020/09/image-5-768x545.png 768w, https://keskec.fr/wp-content/uploads/2020/09/image-5-1536x1090.png 1536w, https://keskec.fr/wp-content/uploads/2020/09/image-5-2048x1454.png 2048w, https://keskec.fr/wp-content/uploads/2020/09/image-5-1568x1113.png 1568w" sizes="(max-width: 1024px) 100vw, 1024px" /> <figcaption>Jupyter Lab &#8211; Oracle Cloud</figcaption></figure> 

Enjoy :). 

## Sources

  1. [The Oracle Cloud Free Tier &#8211; medium.com][4]{.rank-math-link}
  2. [Oracle Cloud Free Tier &#8211; oracle.com][5]{.rank-math-link}
  3. [Installation Jupyter lab &#8211; readthedocs.io][6]{.rank-math-link}
  4. [Comprendre la redirection de port (Port Forwarding) &#8211; linux-france.org][7]{.rank-math-link}

 [1]: https://www.oracle.com/fr/cloud/free/#always-free
 [2]: https://devops.ionos.com/tutorials/use-ssh-keys-with-putty-on-windows/
 [3]: https://docs.cloud.oracle.com/en-us/iaas/developer-tutorials/tutorials/apache-on-ubuntu/01oci-ubuntu-apache-summary.htm
 [4]: https://medium.com/@FranckPachot/the-oracle-cloud-free-tier-37c27f3b1e19
 [5]: https://www.oracle.com/fr/cloud/free/
 [6]: https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html
 [7]: http://www.linux-france.org/prj/edu/archinet/systeme/ch13s04.html