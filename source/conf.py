project = 'pumping python'
copyright = '2023, JadeCobra LLC'
author = 'Jacob Itegboje'

templates_path = ['_templates']
exclude_patterns = [
    'build',
    'notes',
    '.venv',
    'code/code_tree.rst'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_title = 'pumping python: how I solve problems with Test Driven Development'
html_short_title = 'pumping python'
html_baseurl = 'https://www.pumpingpython.com/'
html_logo = "_static/dry_favicon_16x16.png"
html_favicon = '_static/dry_favicon_16x16.png'
html_theme = 'press'
html_static_path = ['_static']
html_theme_options = {
    "external_links": [
        ("videos", "https://www.youtube.com/@JacobItegboje"),
    ]
}
# html_sidebars = {
#     "**": [
#         # "util/searchbox.html",
#         # "globaltoc.html",
#     ]
# }

extensions = ['sphinx.ext.autosectionlabel', 'sphinx_sitemap']

# -- Options for ePub output -------------------------------------------------
epub_theme = 'epub'
epub_description = 'pumping python: how I solve problems with Test Driven Development'
epub_cover = ('_static/DRY.png', '')

# -- Options for LaTeX output -------------------------------------------------
latex_logo = '_static/DRY.png'
latex_show_pagerefs = True
latex_show_urls = 'inline'
latex_theme = 'howto' # 'manual'

text_sectionchars = '#*=-~"+`'

# -- MISC

# autosectionlabel_prefix_document = True