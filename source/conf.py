project = "pumping python"
copyright = "2023, JadeCobra LLC"
author = "Jacob Itegboje"

templates_path = ["_templates"]
exclude_patterns = [
    'source/learning_models.rst'
]

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
html_theme = 'press'
html_static_path = ["_static"]
extensions = ["sphinx.ext.autosectionlabel"]
