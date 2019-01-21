# -*- coding: utf-8 -*-

# © 2017-2019, ETH Zurich, Institut für Theoretische Physik
# Author: Dominik Gresch <greschd@gmx.ch>

import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


os.environ['DJANGO_SETTINGS_MODULE'] = 'rtd_settings'

import aiida
from aiida.backends import settings

# We set that we are in documentation mode - even for local compilation
settings.IN_DOC_MODE = True

# on_rtd is whether we are on readthedocs.org, this line of code grabbed
# from docs.readthedocs.org
# NOTE: it is needed to have these lines before load_dbenv()
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

if not on_rtd:  # only import and set the theme if we're building docs locally
    html_theme = 'sphinx_rtd_theme'
    # Loading the dbenv. The backend should be fixed before compiling the
    # documentation.
    aiida.try_load_dbenv()
else:
    # Back-end settings for readthedocs online documentation.
    # from aiida.backends import settings
    settings.IN_RT_DOC_MODE = True
    settings.BACKEND = "django"
    settings.AIIDADB_PROFILE = "default"

import aiida_symmetry_representation

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.intersphinx', 'sphinx.ext.mathjax',
    'sphinx.ext.viewcode', 'aiida.sphinxext'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'aiida-symmetry-representation'
copyright = u'2018, Dominik Gresch'
author = u'Dominik Gresch'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = aiida_symmetry_representation.__version__
# The short X.Y version.
version = '.'.join(release.split('.')[:2])

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'aiida-symmetry-representationdoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (
        master_doc, 'aiida-symmetry-representation.tex',
        u'aiida-symmetry-representation Documentation', u'Dominik Gresch',
        'manual'
    ),
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(
    master_doc, 'aiida-symmetry-representation',
    u'aiida-symmetry-representation Documentation', [author], 1
)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc, 'aiida-symmetry-representation',
        u'aiida-symmetry-representation Documentation', author,
        'aiida-symmetry-representation', 'One line description of project.',
        'Miscellaneous'
    ),
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/': None,
    'http://z2pack.ethz.ch/strain': None,
    'http://z2pack.ethz.ch/symmetry-representation': None,
}
