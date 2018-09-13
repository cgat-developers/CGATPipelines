# -*- coding: utf-8 -*-
#
# test documentation build configuration file, created by
# sphinx-quickstart on Fri Feb  7 11:33:27 2014.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys
import os

import cgat.Pipeline as P
import cgatPipelines

################################################################
# Options related to cgat pipelines

# path were documentation source resides.
# Use environment variable SPHINX_DOCSDIR.
# If unset, take the location of cgatPipelines
docsdir = os.environ.get("SPHINX_DOCSDIR",
                         os.path.join(os.path.dirname(cgatPipelines.__file__),
                                      'pipeline_docs'))

if not os.path.exists(docsdir):
    raise ValueError("documentation directory '%s' not found" % docsdir)

themedir = os.path.join(os.path.dirname(cgatPipelines.__file__),
                        'pipeline_docs',
                        'themes')
logopath = os.path.join(themedir, "cgat_logo.png")

################################################################
# Import pipeline configuration from pipeline.ini in the current
# directory and the common one.

# PATH were code for pipelines is stored
pipelinesdir = os.path.dirname(cgatPipelines.__file__)

# The default configuration file - 'inifile' is read by
# sphinx-report.
inifile = os.path.join(os.path.dirname(cgatPipelines.__file__),
                       'configuration',
                       'pipeline.ini')

PARAMS = P.getParameters([inifile, "pipeline.ini"])


def setup(app):
    app.add_config_value('PARAMS', {}, True)

################################################################
################################################################
################################################################
# The pipeline assumes that sphinxreport is called within the
# working directory. If the report is in a separate build directory,
# change the paths below.
#
# directory with export directory from pipeline
# This should be a directory in the build directory - you can
# link from here to a directory outside the build tree, though.
exportdir = os.path.abspath(PARAMS['exportdir'])

datadir = os.path.abspath(PARAMS['datadir'])

################################################################
################################################################
################################################################
# sphinx options
################################################################
# General information about the project.
project = PARAMS['projectname']
copyright = PARAMS['copyright']

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = PARAMS['version']
# The full version, including alpha/beta/rc tags.
release = PARAMS['release']

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path = [os.path.abspath('.'),
            pipelinesdir,
            os.path.abspath('%s/trackers' % docsdir)] + sys.path

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.doctest',
              'sphinx.ext.coverage',
              'sphinx.ext.pngmath',
              'sphinx.ext.ifconfig',
              'sphinx.ext.intersphinx',
              'cgatReport.only_directives',
              'cgatReport.report_directive',
              'sphinx.ext.inheritance_diagram',
              'cgatReport.errors_directive',
              'cgatReport.warnings_directive',
              'cgatReport.roles']

if P.CONFIG.has_section('intersphinx'):
    intersphinx_mapping = dict(
        [(x, (os.path.abspath(y), None))
         for x, y in P.CONFIG.items('intersphinx')])

# Included at the end of each rst file
rst_epilog = '''
.. _cgat Training Programme: http://www.cgat.org
.. _cgat Pipelines: https://www.cgat.org/downloads/public/cgat/documentation/Pipelines.html#pipelines
.. _cgat Scripts: https://www.cgat.org/downloads/public/cgat/documentation/cgat.html#cgat
.. _pysam: http://code.google.com/p/pysam/
.. _samtools: http://samtools.sourceforge.net/
.. _tabix: http://samtools.sourceforge.net/tabix.shtml/
.. _Galaxy: https://main.g2.bx.psu.edu/
.. _cython: http://cython.org/
.. _python: http://python.org/
.. _pyximport: http://www.prescod.net/pyximport/
.. _sphinx: http://sphinx-doc.org/
.. _ruffus: http://www.ruffus.org.uk/
.. _sphinxreport: http://code.google.com/p/sphinx-report/
.. _sqlite: http://www.sqlite.org/
.. _make: http://www.gnu.org/software/make
.. _UCSC: http://genome.ucsc.edu
.. _ENSEMBL: http://www.ensembl.org
.. _GO: http://www.geneontology.org
.. _gwascatalog: http://www.genome.gov/gwastudies/
.. _distlid: http://distild.jensenlab.org/
.. _mysql: https://mariadb.org/
.. _postgres: http://www.postgresql.org/
.. _bedtools: http://bedtools.readthedocs.org/en/latest/
.. _UCSC Tools: http://genome.ucsc.edu/admin/git.html
.. _git: http://git-scm.com/
.. _sge: http://wikis.sun.com/display/GridEngine/Home
.. _alignlib: https://github.com/AndreasHeger/alignlib
'''

# Add any paths that contain templates here, relative to this directory.
# Add any paths that contain templates here, relative to this directory.
templates_path = [os.path.relpath('%s/_templates' % docsdir)]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
# source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = 'test'
copyright = '2014, %cgat%'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
# today = ''
# Else, today_fmt is used as the format for a strftime call.
# today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']
exclude_patterns = ["**/.*.rst"]

# The reST default role (used for this markup: `text`) to use for all
# documents.
# default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
# add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
# add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
# show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
# modindex_common_prefix = []

# If true, keep warnings as "system message" paragraphs in the built documents.
# keep_warnings = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'cgat'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = [themedir]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
# html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
# html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = logopath

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
# html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Add any extra paths that contain custom files (such as robots.txt or
# .htaccess) here, relative to this directory. These files are copied
# directly to the root of the documentation.
# html_extra_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
# html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
# html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {}

# If false, no module index is generated.
# html_domain_indices = True

# If false, no index is generated.
# html_use_index = True

# If true, the index is split into individual pages for each letter.
# html_split_index = False

# If true, links to the reST sources are added to the pages.
# html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
# html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
# html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
# html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'testdoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
# 'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
# 'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
# 'preamble': '',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    ('index', 'test.tex', 'test Documentation',
     '\\%cgat\\%', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
# latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
# latex_use_parts = False

# If true, show page references after internal links.
# latex_show_pagerefs = False

# If true, show URL addresses after external links.
# latex_show_urls = False

# Documents to append as an appendix to all manuals.
# latex_appendices = []

# If false, no module index is generated.
# latex_domain_indices = True


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'test', 'test Documentation',
     ['%cgat%'], 1)
]

# If true, show URL addresses after external links.
# man_show_urls = False


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    ('index', 'test', 'test Documentation',
     '%cgat%', 'test', 'One line description of project.',
     'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
# texinfo_appendices = []

# If false, no module index is generated.
# texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
# texinfo_show_urls = 'footnote'

# If true, do not generate a @detailmenu in the "Top" node's menu.
# texinfo_no_detailmenu = False
