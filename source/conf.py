# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from sphinx_revealjs.themes import get_theme_path

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "attakei's presentations"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "2022.10.11"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_revealjs",
    "sphinxcontrib.budoux",
    "sphinxcontrib.sass",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for REVEALJS output
revealjs_style_theme = "css/my-solarized.css"
revealjs_static_path = ["_static"]
revealjs_css_files = [
    "revealjs4/plugin/highlight/zenburn.css",
]
revealjs_script_conf = {
    "controls": False,
    "hash": True,
    "center": False,
    "transition": "none",
}
revealjs_script_plugins = [
    {
        "src": "revealjs4/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
]

# -- Options for extensions
# sphinxcontrib-budoux
budoux_targets = ["h1", "h2", "h3"]

# sphinxcontrib-sass
sass_src_dir = "_sass"
sass_out_dir = "_static/css"
sass_include_paths = [
    get_theme_path("sphinx_revealjs") / "static/revealjs4/css/theme",
]
sass_targets = {
    "my-solarized.scss": "my-solarized.css",
}
