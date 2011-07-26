# -*- coding: utf-8 -*-
#
# Sage documentation build configuration file, created by
# sphinx-quickstart on Thu Aug 21 20:15:55 2008.
#
# This file is execfile()d with the current directory set to its containing
# dir.
#
# The contents of this file are pickled, so don't put values in the namespace
# that aren't pickleable (module imports are okay, they're removed
# automatically).
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import os
import sys
sys.path.append(os.environ["SAGE_DOC"])
from common.conf import *

# General information about the project.
project = u"Thematic Tutorials"

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = project + " v" + release

# Output file base name for HTML help builder.
htmlhelp_basename = "thematic_tutorials"

# mathfrak isn't defined in jsMath, so using it gives errors.  The
# following line turns it into bold face only when using jsMath, thus
# avoiding the errors, while keeping the nice mathfrak fonts when not
# using jsMath.
try:
    html_theme_options['jsmath_macros'].append("mathfrak : ['\\\\mathbf{#1}', 1]")
except KeyError:
    html_theme_options['jsmath_macros'] = ["mathfrak : ['\\\\mathbf{#1}', 1]"]

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author,
# document class [howto/manual]).
latex_documents = [(
        "index", "thematic_tutorials.tex", u'Thematic Tutorials',
        u'The Sage Development Team', 'manual'),
]

show_authors = True
