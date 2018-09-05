from flask import render_template, redirect
from blueprints.example import blueprint, name
from jumpscale import j


@blueprint.route('/')
def route_default():
    return redirect('%s/index.html' % name)


@blueprint.route('/<template>.html')
def route_template(template):
    ds = j.tools.docsites.docsite_get("example")
    doc = ds.doc_get(template)
    return render_template(template + '.html', doc=doc)
