import sphinxawesome_theme


project = 'pumping python'
copyright = '%Y, JadeCobra LLC'
author = 'Jacob Itegboje'

rst_prolog = """
.. role:: red
.. role:: green
.. role:: yellow
"""
master_doc = 'index'

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


# -- Section Header Options ----------------------------------------------------
text_sectionchars = '#*=-~"+`'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'furo'
# pygments_style = "tango"
# pygments_dark_style = "monokai" # for furo
html_theme = "sphinxawesome_theme"
html_permalinks_icon = sphinxawesome_theme.postprocess.Icons.permalinks_icon
html_theme_options = {
    "logo_light": "_static/dry_favicon_16x16.png",
    "logo_dark": "_static/dry_favicon_16x16.png",
    "show_prev_next": True,
}
html_sidebars = {
  "**": ["sidebar_main_nav_links.html", "sidebar_toc.html", "localtoc.html"]
}

# syntax highlighting
pygments_style = "tango"
pygments_style_dark = "monokai"

html_extra_path = ['robots.txt', 'llms.txt']
html_baseurl = 'https://www.pumpingpython.com/'
html_favicon = '_static/dry_favicon_16x16.png'
# html_logo = "_static/dry_favicon_16x16.png"
html_title = 'pumping python: how I solve problems with Test Driven Development'
html_short_title = 'pumping python'
html_static_path = ['_static']
html_js_files = [
    '//widget.trustpilot.com/bootstrap/v5/tp.widget.bootstrap.min.js',
]
html_css_files = [
    'custom.css',
]

sitemap_url_scheme = '{link}'
intersphinx_mapping = {'python': ('https://docs.python.org/3', None)}

# notfound_template = '_templates/layout.html'

# -- Options for ePub output -------------------------------------------------
epub_theme = 'epub'
epub_description = 'pumping python: how I solve problems with Test Driven Development'
epub_cover = ('_static/DRY.png', '')

# -- Options for LaTeX output -------------------------------------------------
latex_logo = '_static/DRY.png'
latex_show_pagerefs = True
latex_show_urls = 'inline'
latex_theme = 'manual' # 'howto'

# Define custom LaTeX elements for improved aesthetics
latex_elements = {
    'geometry': '',
    # The paper size ('letterpaper' or 'a4paper').
    'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    # This is where you can load packages for custom fonts, colors, etc.
#     'preamble': r'''
# \usepackage{amsmath} % For advanced math
# \usepackage{amsfonts} % For math fonts
# \usepackage{amssymb} % For math symbols
# \usepackage{microtype} % For better typesetting (adjusts spacing, etc.)

# % Set page margins (tweak these values)
# \geometry{
#     a4paper,
#     top=2.5cm,
#     bottom=2.5cm,
#     left=3cm,
#     right=3cm,
#     headheight=14.5pt,
#     footskip=1cm
# }

# % Change the font for the entire document (e.g., use a cleaner font like Latin Modern)
# % If you want a non-default font, you'll need the proper LaTeX package installed.
# \usepackage{lmodern}
# % For a professional look, you might consider setting a serif font for body text
# % and a sans-serif for headings (if using a theme that supports it well).
# % \renewcommand{\familydefault}{\sfdefault} % Uncomment for a sans-serif look

# % Improve the look of code blocks (listings package can do this)
# \usepackage{listings}
# % \lstset{
# %     basicstyle=\ttfamily\footnotesize, % Smaller font for code
# %     breaklines=true, % Automatic line breaking
# %     frame=single, % Add a frame around the code
# %     framerule=0pt, % Remove the rule border
# %     rulecolor=\color{lightgray}, % Color the rule
# %     backgroundcolor=\color{lightgray!20} % Light background color
# % }

# % Custom title page look (optional, depends on 'maketitle' in 'maketitle' element)
# \makeatletter
# \def\maketitle{
#   \begin{titlepage}
#     \centering
#     \includegraphics[width=0.4\textwidth]{DRY.png}\par\vspace{1em} % Your logo
#     {\Huge\bfseries\textsf{pumping python}}\par\vspace{1em} % Project Title
#     {\Large\textsf{how I solve problems with Test Driven Development}}\par\vspace{2em} % Subtitle
#     {\large \@author}\par\vspace{0.5em} % Author
#     {\large \@date}\par\vspace{2cm} % Date
#     % You can add more info here, like a nice quote or a brief abstract
#   \end{titlepage}
# }
# \makeatother

# \hypersetup{
#     colorlinks=true,
#     linkcolor=blue,
#     citecolor=blue,
#     urlcolor=cyan,
# }
#     ''',

    # Removes blank pages and adds to the aesthetic appeal
    'classoptions': ',openany,oneside',

    # For 'howto', you might want to switch to 'manual' for a book-like PDF
    # or keep 'howto' for a document/article look.
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}', # Custom chapter styles

    # Custom document content setup
    'maketitle': r'\maketitle', # Use the custom \maketitle defined in preamble
    'tableofcontents': r'\setcounter{tocdepth}{2}\tableofcontents', # Only show sections up to level 2 in TOC
}

# The LaTeX document class ('report', 'book', 'article', 'howto').
latex_documents = [
    (master_doc, 'pumpingpython.tex', 'pumping python Documentation',
     'Jacob Itegboje', 'manual'),
]