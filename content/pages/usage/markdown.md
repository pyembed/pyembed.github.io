Title: Usage with Markdown
URL: usage/markdown/
save_as: usage/markdown/index.html

[TOC]

PyEmbed is available as an extension to [Python-Markdown](http://pythonhosted.org/Markdown/).  Embedding content is then a simple matter of using the special `[!embed]` link tag.  For example:

    [!embed](http://www.youtube.com/watch?v=9bZkp7q19f0)

More examples can be seen on the [examples page](/examples/markdown/).

## Installation ##

PyEmbed-Markdown can be installed using [pip](http://www.pip-installer.org/).

    pip install pyembed-markdown

## Usage ##

### Standalone ###

PyEmbed-Markdown can be passed as a standard extension to Python-Markdown:

    >>> import markdown
    >>> from pyembed.markdown import PyEmbedMarkdown
    >>> html = markdown.markdown(text, extensions=[PyEmbedMarkdown()])

### Pelican ###

If you're using [Pelican](http://docs.getpelican.com/), simply add these lines to your pelicanconf.py file:

    from pyembed.markdown import PyEmbedMarkdown
    MD_EXTENSIONS = [PyEmbedMarkdown()]

## Syntax ##

### Basics ###

The default syntax for embedding is to create a link with text `!embed`, and the URL of the content to embed.

For example, this source:

    [!embed](http://www.youtube.com/watch?v=9bZkp7q19f0)

will result in the following HTML output:

    <iframe width="480" height="270" src="http://www.youtube.com/embed/9bZkp7q19f0?feature=oembed" frameborder="0" allowfullscreen></iframe>

### Parameters ###

You can control the maximum size of the embedded content with the `max_height` and / or `max_width` parameters.  For example:

    [!embed?max_width=300](http://www.youtube.com/watch?v=9bZkp7q19f0)
    [!embed?max_width=300&max_height=200](http://www.youtube.com/watch?v=9bZkp7q19f0)
