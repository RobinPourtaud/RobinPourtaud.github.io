---
title: "Coloration Syntaxique pour Wordpress AMP"
slug: "mettre-de-la-couleurs-a-vos-codes-pour-les-wordpress-amp"
date: "2020-05-25"
categories: 
  - "informatique"
tags: 
  - "amp"
  - "css"
  
  - "wordpress"
description: "AMP est une technologie développée par Google depuis 2015. Open Source, c'est une méthode de création de page Web statique permettant un rendu plus rapide. Applicable sur Wordpress, elle peut permettre des gains importants, de part son utilisation de cache et sa désactivation par défaut de code personnalisé JavaScript. Cette désactivation est, en terme de vitesse, bénéfique. Elle pose malgré tout de nombreux problèmes. Un problème parmi ceux-ci est celui de la coloration syntaxique."
---
Il existe de nombreuses extensions Wordpress permettant la coloration syntaxique. Cependant, la (très grande) majorité d'entre elles utilise le JavaScript... Ce tutoriel est là pour vous aider à rétablir vos magnifiques codes sur votre site Wordpress AMP :) .

## Nécessaire

- Avoir accès aux droits d'administration de votre Wordpress mis à jour (mai 2020).
- Avoir **de préférence** installé [ce plugin pour AMP](https://wordpress.org/plugins/accelerated-mobile-pages/).
- Savoir installer une extension. Sinon : [Support](https://wordpress.com/fr/support/extensions/)

## Installer l’extension : Syntax-highlighting Code Block

Je vous propose d'installer l'extension :

[Syntax-highlighting Code Block (with Server-side Rendering)](https://wordpress.org/plugins/syntax-highlighting-code-block/)

Contrairement à de nombreuses extensions de coloration syntaxique, celle-ci ne repose pas sur le JavaScript mais sur le PHP. Ainsi il n'y aura plus besoin de fichiers JS personnalisés, qui posent problème avec la technologie AMP.

## Trouvez un thème qui vous convient

Il existe de nombreux thèmes compatibles Highlight.js. Vous pouvez tous les tester à l'adresse :

[https://highlightjs.org/static/demo/](https://highlightjs.org/static/demo/)

Une fois votre thème favori trouvé, rendez-vous sur Github à l'adresse suivante :

[https://github.com/highlightjs/highlight.js/tree/master/src/styles](https://github.com/highlightjs/highlight.js/tree/master/src/styles)

et copiez le contenu du fichier CSS choisi.

Mon préféré étant celui-ci :

```css
/*
Monokai style - ported by Luigi Maselli - http://grigio.org
*/

.hljs {
  display: block;
  overflow-x: auto;
  padding: 0.5em;
  background: #272822;
  color: #ddd;
}

.hljs-tag,
.hljs-keyword,
.hljs-selector-tag,
.hljs-literal,
.hljs-strong,
.hljs-name {
  color: #f92672;
}

.hljs-code {
  color: #66d9ef;
}

.hljs-class .hljs-title {
  color: white;
}

.hljs-attribute,
.hljs-symbol,
.hljs-regexp,
.hljs-link {
  color: #bf79db;
}

.hljs-number{
    color: #ae81ff;
}

.hljs-string,
.hljs-bullet,
.hljs-subst,
.hljs-title,
.hljs-section,
.hljs-emphasis,
.hljs-type,
.hljs-built_in,
.hljs-builtin-name,
.hljs-selector-attr,
.hljs-selector-pseudo,
.hljs-addition,
.hljs-variable,
.hljs-template-tag,
.hljs-template-variable {
  color: #a6e22e;
}

.hljs-comment,
.hljs-quote,
.hljs-deletion,
.hljs-meta {
  color: #75715e;
}

.hljs-keyword,
.hljs-selector-tag,
.hljs-literal,
.hljs-doctag,
.hljs-title,
.hljs-section,
.hljs-type,
.hljs-selector-id {
  font-weight: bold;
}
```

## Ajoutez le code CSS à votre site AMP

Une fois le code CSS trouvé, il faut l'ajouter à toutes vos page AMP. Pour cela, rendez-vous sur les paramètres de votre extension AMP. (Si vous avez une autre extension, trouvez l'endroit où ajouter du code CSS personnalisé).

Depuis votre interface d'administration Wordpress :

1. Accédez à vos extensions et cliquez sur "Settings".
2. Cliquez sur "Design" puis "Global".
3. Dans "Custom CSS", ajoutez votre code CSS précédemment copié.

## Utilisation

Tous vos codes sont maintenant, normalement, de la bonne couleur :).

Si ce n'est pas le cas, il se peut que vous utilisiez un plugin de cache, n'affichant ainsi pas ces nouvelles modifications. Videz le cache et regardez si cela a fonctionné !

Si vos couleurs ne s'affichent pas où il faut pour certains blocs de code, il faudra sélectionner manuellement le bon langage de programmation associé. Pour cela, rendez-vous sur votre article. Cliquez sur le bloc de code posant problème.

![Bloc code](image-2-533x1024.png#t3)



Sélectionnez le langage adéquat !

## Sources :

- [https://developers.google.com/amp?hl=fr](https://developers.google.com/amp?hl=fr)
- [https://fr.wikipedia.org/wiki/Accelerated_Mobile_Pages](https://fr.wikipedia.org/wiki/Accelerated_Mobile_Pages)
- [https://github.com/highlightjs/highlight.js](https://github.com/highlightjs/highlight.js)
