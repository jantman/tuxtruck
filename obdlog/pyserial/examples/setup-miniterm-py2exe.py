# setup script for py2exe to create the miniterm.exe
# $Id$

from distutils.core import setup
import glob, sys, py2exe, os

sys.path.append('..')

sys.argv.extend("py2exe --bundle 1".split())

setup(
    name='miniterm',
    #~ version='0.5',
    zipfile=None,
    options = {"py2exe":
        {
            'dist_dir': 'bin',
            'excludes': ['javax.comm'],
        }
    },
    console = [
        #~ "miniterm_exe_wrapper.py",
        "miniterm.py",
    ],
)
