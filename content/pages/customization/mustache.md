Title: Customization with Mustache
URL: customization/mustache/
save_as: customization/mustache/index.html

[TOC]

PyEmbed allows you to control how embeddings are rendered using Mustache templates.  For example, if you want to include the thumbnail image when embedding a link, you could use a template like this:

    <a href="{{content_url}}"><img src="{{thumbnail_url}}" /></a>

## Usage ##

In order to use the Mustache renderer, you must create a directory containing template files for each type of OEmbed resource.  These files must be named:

- link.mustache
- photo.mustache
- rich.mustache
- video.mustache

You can then create the renderer as follows:

    >>> from pyembed.mustache import MustacheRenderer
    >>> renderer = MustacheRenderer(path_to_template_dir)

For more information on how to use the renderer, see the [introduction to customization](../).
