import sphinxawesome_theme

project = 'pumping python'
copyright = '%Y, JadeCobra LLC'
author = 'Jacob Itegboje'
version = '0.1.0'
release = version

rst_prolog = """
.. role:: red
   :class: custom-red
.. role:: green
   :class: custom-green
.. role:: yellow
   :class: custom-yellow
"""
root_doc = 'index'

templates_path = ['_templates']
exclude_patterns = [
    'build',
    'notes',
    '.venv',
    'code/code_tree.rst',
]

extensions = [
    'sphinx_sitemap',
    'sphinx_design',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'notfound.extension',
]

# -- Section Header Options ----------------------------------------------------
text_sectionchars = '#*=-~"+`'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
html_permalinks_icon = sphinxawesome_theme.postprocess.Icons.permalinks_icon
html_theme_options = {
    "logo_light": "_static/dry_favicon_16x16.png",
    "logo_dark": "_static/dry_favicon_16x16.png",
    "show_prev_next": True,
}
html_sidebars = {
    "**": ["sidebar_main_nav_links.html", "sidebar_toc.html", "localtoc.html"],
}

pygments_style = "default"
pygments_style_dark = "monokai"

html_extra_path = ['robots.txt', 'llms.txt']
html_baseurl = 'https://www.pumpingpython.com/'
html_favicon = '_static/dry_favicon_16x16.png'
html_title = 'pumping python: how I solve problems with Test Driven Development'
html_short_title = 'pumping python'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_js_files = [
    'https://widget.trustpilot.com/bootstrap/v5/tp.widget.bootstrap.min.js',
]

sitemap_url_scheme = '{link}'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# -- Options for ePub output -------------------------------------------------
epub_theme = 'epub'
epub_description = 'pumping python: how I solve problems with Test Driven Development'
epub_cover = ('_static/DRY.png', '')

# -- Options for LaTeX output -------------------------------------------------
latex_logo = '_static/DRY.png'
latex_show_pagerefs = True
latex_show_urls = 'inline'
latex_theme = 'manual'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'classoptions': ',openany,oneside',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'tableofcontents': r'\setcounter{tocdepth}{2}\tableofcontents',
}

latex_documents = [(
    root_doc, 'pumpingpython.tex', 'pumping python Documentation',
    'Jacob Itegboje', 'manual',
)]

suppress_warnings = [
    'ref.label',
    'autosectionlabel.*',
    'toc.not_readable',
    'toc.not_included',
]