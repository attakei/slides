# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
import os
import sys
from pathlib import Path

from sphinx_revealjs.utils import get_revealjs_path

ext_dir = str(Path(__file__).parents[1] / "extensions")
if sys.path[-1] != ext_dir:
    sys.path.append(ext_dir)

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "attakei's presentations"
copyright = "2022, Kazuya Takei"
author = "Kazuya Takei"
release = "2022.12.23"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "oembedpy.adapters.sphinx",
    "rst_pypi_ref.sphinx",
    "sphinx.ext.todo",
    "sphinx_revealjs",
    "sphinx_revealjs.ext.oembed",
    "sphinx_revealjs.ext.sass",
    "sphinx_revealjs.ext.screenshot",
    "sphinxcontrib.blockdiag",
    "sphinxcontrib.budoux",
    "sphinxemoji.sphinxemoji",
    "sphinxext.opengraph",
    "sphinxnotes.strike",
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ja"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

# -- Options for REVEALJS output
revealjs_static_path = ["_static"]
revealjs_css_files = [
    "css/default.css",
    "css/footnotes.css",
    "css/a11y-light.css",
]
revealjs_script_conf = {
    "controls": False,
    "hash": True,
    "center": False,
    "transition": "none",
}
revealjs_script_plugins = [
    {
        "src": "revealjs/plugin/highlight/highlight.js",
        "name": "RevealHighlight",
    },
    {
        "src": "revealjs/plugin/notes/notes.js",
        "name": "RevealNotes",
    },
]

# -- Options for extensions
# sphinx-revealjs.ext.screenshot
revealjs_screenshot_excludes = ["*/?_*"]
# sphinx_revealjs.ext.sass
revealjs_sass_src_dir = "_sass"
revealjs_sass_out_dir = "_static/css"
revealjs_sass_auto_targets = True

# sphinxcontrib-budoux
budoux_targets = ["h1", "h2", "h3"]

# sphinxext-opengraph
ogp_site_url = os.environ.get("SITE_URLBASE", "http://localhost:8000/")
ogp_type = "article"
ogp_custom_meta_tags = [
    '<meta name="twitter:card" content="summary_large_image" >',
    '<meta name="twitter:site" content="@attakei" >',
]
ogp_enable_meta_description = True

# sphinx.revealjs.ext.oembed
revealjs_oembed_urlbase = ogp_site_url[:-1]
