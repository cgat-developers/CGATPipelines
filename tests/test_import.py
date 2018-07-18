'''test_import - test importing all modules and pipelines
=========================================================

:Author: Andreas Heger
:Release: $Id$
:Date: |today|
:Tags: Python

Purpose
-------

This script attempts to import all the python libraries and
pipeline scripts in the CGAT code collection.

Importing a script/module is a pre-requisite for building
documentation with sphinx. A script/module that can not be imported
will fail within sphinx.

This script is best run within nosetests::

   nosetests tests/test_import.py

'''

import os
import glob
import traceback
import imp

from nose.tools import ok_

# DIRECTORIES to examine for python modules/scripts
EXPRESSIONS = (
    ('tests', 'tests/*.py'),
    ('scripts', 'scripts/*.py'),
    ('CGATPipelines', 'CGATPipelines/*.py'))

# Scripts to exclude as they fail imports.
EXCLUDE = (
    # No need to check cgat_check_deps.py
    'cgat_check_deps',
    # No need to check conda.py
    'conda',)


def check_import(filename, outfile):

    prefix, suffix = os.path.splitext(filename)
    dirname, basename = os.path.split(prefix)

    if basename in EXCLUDE:
        return

    if os.path.exists(prefix + ".pyc"):
        os.remove(prefix + ".pyc")

    # ignore script with pyximport for now, something does not work
    pyxfile = os.path.join(dirname, "_") + basename + "x"
    if os.path.exists(pyxfile):
        return

    try:
        imp.load_source(basename, filename)

    except ImportError as msg:
        outfile.write("FAIL %s\n%s\n" % (basename, msg))
        outfile.flush()
        traceback.print_exc(file=outfile)
        ok_(False, '%s scripts/modules - ImportError: %s' %
            (basename, msg))
    except Exception as msg:
        outfile.write("FAIL %s\n%s\n" % (basename, msg))
        outfile.flush()

        traceback.print_exc(file=outfile)
        ok_(False, '%s scripts/modules - Exception: %s' %
            (basename, str(msg)))

    ok_(True)


def test_imports():
    '''test importing

    Relative imports will cause a failure because
    imp.load_source does not import modules that are in the same
    directory as the module being loaded from source.
    '''
    outfile = open('test_import.log', 'a')

    for label, expression in EXPRESSIONS:

        files = glob.glob(expression)
        files.sort()

        for f in files:
            if os.path.isdir(f):
                continue
            check_import.description = os.path.abspath(f)
            yield(check_import, os.path.abspath(f), outfile)
