Title: Usage with reStructuredText
URL: usage/rst/
save_as: usage/rst/index.html

[TOC]

PyEmbed is available as a [reStructuredText](http://docutils.sourceforge.net/rst.html) directive, for use with [Docutils](http://docutils.sourceforge.net/) Embedding content is then a simple matter of using the special `.. embed::` tag.  For example:

    .. embed:: http://www.youtube.com/watch?v=9bZkp7q19f0

More examples can be seen on the [examples page](/examples/rst/).

## Installation ##

PyEmbed-Rst can be installed using [pip](http://www.pip-installer.org/).

    pip install pyembed-rst

## Usage ##

### Standalone ###

PyEmbed-Rst can be registered as a standard reStructuredText directive:

    >>> from pyembed.rst import PyEmbedRst
    >>> PyEmbedRst().register()
    >>> html = publish_string(text)

### Pelican ###

If you're using [Pelican](http://docs.getpelican.com/), simply add these lines to your pelicanconf.py file:

    from pyembed.rst import PyEmbedRst
    PyEmbedRst().register()

## Syntax ##

### Basics ###

The default syntax for embedding is to use the `embed` directive, including the URL of the content to embed.

For example, this source:

    .. embed:: http://www.youtube.com/watch?v=9bZkp7q19f0

will result in the following HTML output:

    <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>

### Parameters ###

You can control the maximum size of the embedded content with the `max_height` and / or `max_width` parameters.  For example:

    .. embed:: http://www.youtube.com/watch?v=9bZkp7q19f0
       :max_width: 300

<!-- break -->

    .. embed:: http://www.youtube.com/watch?v=9bZkp7q19f0
       :max_width: 300
       :max_height: 200