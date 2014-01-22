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

## Available parameters ##

The table below shows which parameters are available for each response type.  For more information, see section 2.3.4 of the [OEmbed spec](http://oembed.com).

The exception is the first parameter, `content_url`, which contains the URL that was requested to be embedded.

<div class="table-responsive">
    <table class="table table-bordered">
        <thead>
            <tr>
                <th>Parameter</th>
                <th>Link</th>
                <th>Photo</th>
                <th>Rich</th>
                <th>Video</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>content_url</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
            <tr>
                <td>type</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
            <tr>
                <td>version</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
            <tr>
                <td>title</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>author_name</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>author_url</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>provider_name</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>provider_url</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>cache_age</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>thumbnail_url</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>thumbnail_width</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>thumbnail_height</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
                <td class="warning">Optional</td>
            </tr>
            <tr>
                <td>url</td>
                <td class="danger">Not present</td>
                <td class="success">Required</td>
                <td class="danger">Not present</td>
                <td class="danger">Not present</td>
            </tr>
            <tr>
                <td>width</td>
                <td class="danger">Not present</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
            <tr>
                <td>height</td>
                <td class="danger">Not present</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
            <tr>
                <td>html</td>
                <td class="danger">Not present</td>
                <td class="danger">Not present</td>
                <td class="success">Required</td>
                <td class="success">Required</td>
            </tr>
        </tbody>
    </table>
</div>
