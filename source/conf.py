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

html_title = 'Pumping Python: how to solve problems with Test Driven Development'
html_short_title = 'Pumping Python'
html_logo = "_static/dry_favicon_16x16.png"
html_favicon = '_static/dry_favicon_16x16.png'
html_theme = 'press'
html_static_path = ['_static']
html_theme_options = {
    "external_links": [
        ("videos", "https://www.youtube.com/@JacobItegboje"),
        ("jacobitegboje", "https://jacobitegboje.com"),
    ]
}

# html_logo = "_static/DRY_html_logo.png"
# html_theme = 'alabaster'
# html_sidebars = {
#     "**": [
#         # "util/searchbox.html",
#         # "globaltoc.html",
#     ]
# }

extensions = ['sphinx.ext.autosectionlabel']
# autosectionlabel_prefix_document = True

epub_theme = 'epub'
epub_description = 'Pumping Python: how to solve problems with Test Driven Development'
epub_cover = ('_static/DRY.png', '')

latex_logo = '_static/DRY.png'
latex_show_pagerefs = True
latex_show_urls = 'inline'
latex_them = 'howto' # 'manual'

text_sectionchars = '#*=-~"+`'
