Title: Customization
URL: customization/
save_as: customization/index.html

[TOC]

PyEmbed allows you to control exactly how content is renderer by supplying a custom renderer.  There are supported renderers that allow you to write templates for your embeddings using [Mustache](mustache/) or [Jinja2](jinja2/), or you can write your own renderer.

## Using a renderer ##

### Standalone ###

If you're using PyEmbed directly, you can specify a custom renderer as follows:

    >>> html = PyEmbed(renderer).embed(url)

### Markdown ###

You can pass a custom renderer directly to the [Markdown extension](/usage/markdown/):

    >>> html = markdown.markdown(text, extensions=[PyEmbedMarkdown(renderer)])

## Creating a custom renderer ##

If you want to create your own renderer, you should extend the [PyEmbedRenderer](https://github.com/pyembed/pyembed/blob/master/pyembed/core/render.py) class, overriding the `render` method.
