project = 'pumping python'
copyright = '2023, JadeCobra LLC'
author = 'Jacob Itegboje'

templates_path = ['_templates']
exclude_patterns = [
    'build',
    'notes',
    '.venv',
    'code/code_tree.rst',
]

extensions = [
    'sphinx_sitemap',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.intersphinx',
    'sphinx.ext.githubpages',
    'notfound.extension',
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_extra_path = ['robots.txt', 'llms.txt']
html_baseurl = 'https://www.pumpingpython.com/'
html_favicon = '_static/dry_favicon_16x16.png'
html_logo = "_static/dry_favicon_16x16.png"
# html_theme = 'press'
html_title = 'pumping python: how I solve problems with Test Driven Development'
html_short_title = 'pumping python'
html_static_path = ['_static']
html_theme_options = {
    'external_links': [
        ("videos", "https://www.youtube.com/@JacobItegboje"),
    ],
}

sitemap_url_scheme = '{link}'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

notfound_template = '_templates/layout.html'

# -- Options for ePub output -------------------------------------------------
epub_theme = 'epub'
epub_description = 'pumping python: how I solve problems with Test Driven Development'
epub_cover = ('_static/DRY.png', '')

# -- Options for LaTeX output -------------------------------------------------
latex_logo = '_static/DRY.png'
latex_show_pagerefs = True
latex_show_urls = 'inline'
latex_theme = 'howto' # 'manual'

# -- Section Header Options ----------------------------------------------------
text_sectionchars = '#*=-~"+`'