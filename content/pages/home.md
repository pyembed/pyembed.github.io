Title: Simple content embedding for Python
URL:
save_as: index.html

[TOC]

PyEmbed is a Python library that allows you to easily embed content on your website from a wide variety of sources (including [Flickr](http://flickr.com/), [Twitter](http://twitter.com/) and [YouTube](http://youtube.com/)).  It uses the [oEmbed](http://www.oembed.com/) standard to discover how to represent the resource on your website.

## Key features ##

- Zero configuration - just supply the URL that you want to embed content from.
- Support for [Markdown](http://daringfireball.net/projects/markdown/) and [reStructuredText](http://docutils.sourceforge.net/rst.html).
- Works with static site generators, including [Pelican](http://docs.getpelican.com).
- Fully customizable embeddings, with support for [Jinja2](http://jinja.pocoo.org/)
 and [Mustache](http://mustache.github.io/).

## Getting started ##

PyEmbed comes with out-of-the-box support for Markdown and reStructuredText, or you can embed it in your own applications.  See the Usage section on the navigation bar for more information.

## Compatibility ##

PyEmbed has been tested with Python 2.7, 3.3 and 3.4.

## Contributing ##

To report an issue, request an enhancement, or contribute a patch, go to the [PyEmbed GitHub page](https://github.com/pyembed/).

## Release history ##

### v1.2.2 ###

*Released 2015-08-15*

Fix another Beautiful Soup warning.

### v1.2.1 ###

*Released 2015-08-15*

Fix Beautiful Soup warning.

### v1.2.0 ###

*Released 2015-08-12*

Use [official list of providers](http://oembed.com/providers.json).

### v1.1.2 ###

*Released 2015-01-03*

Allow overriding the templates in the default renderer.

### v1.1.1 ###

*Released 2014-09-02*

Fixed bug with embedding from SoundCloud.

### v1.1.0 ###

*Released 2014-08-02*

This release adds support for more providers.  These are statically configured based on the list in the [oEmbed spec](http://oembed.com).

### v1.0.0 ###

*Released 2014-02-05*

Initial stable release.
