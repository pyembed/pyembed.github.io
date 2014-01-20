Title: Customization with Jinja2
URL: customization/jinja2/
save_as: customization/jinja2/index.html

[TOC]

PyEmbed allows you to control how embeddings are rendered using Jinja2 templates.  For example, if you want to include the thumbnail image when embedding a link, you could use a template like this:

    <a href="{{content_url}}"><img src="{{thumbnail_url}}" /></a>

## Usage ##

In order to use the Jinja2 renderer, you must create a directory containing template files for each type of OEmbed resource.  These files must be named:

- link.html
- photo.html
- rich.html
- video.html

You can then create the renderer as follows:

    >>> from pyembed.jinja2 import Jinja2Renderer
    >>> renderer = Jinja2Renderer(path_to_template_dir)

For more information on how to use the renderer, see the [introduction to customization](../).
