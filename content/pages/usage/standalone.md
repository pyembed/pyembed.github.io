Title: Standalone usage
URL: usage/standalone/
save_as: usage/standalone/index.html

[TOC]

PyEmbed can easily be embedded into your own projects.  Embedding content is just a single call:

    >>> from pyembed.core import PyEmbed
    >>> html = PyEmbed().embed(url)

## Installation ##

PyEmbed can be installed using [pip](http://www.pip-installer.org/).

    pip install pyembed

## Usage ##

### Basics ###

As shown above, passing a URL to the `embed` method will return the HTML to embed.

For example, this call:

    >>> PyEmbed().embed('http://www.youtube.com/watch?v=9bZkp7q19f0')

will result in the following HTML output:

    <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>

### Parameters ###

You can control the maximum size of the embedded content with the `max_height` and / or `max_width` parameters.  For example:

    >>> pyembed = PyEmbed()
    >>> url = 'http://www.youtube.com/watch?v=9bZkp7q19f0'
    >>> pyembed.embed(url, max_width = 300)
    >>> pyembed.embed(url, max_width = 300, max_height = 200)
