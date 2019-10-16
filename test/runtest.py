#!/usr/bin/env python3
import difflib
import os
#import pathlib
import shutil
import subprocess
import sys
try:
    import pathlib2 as pathlib
except:
    import pathlib

TEST_DIR = pathlib.Path(__file__).absolute().parent
PROJECT_DIR = TEST_DIR.parent
EXPECTED_OUTPUT = r"""# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'dummypkg{version}','console_scripts','hello'
__requires__ = 'dummypkg{version}'
import re
import sys

from dummy import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())"""

# Python 2 needs virtualenv, and Travis already executes in a virtualenv
use_virtualenv = True
use_editable = True

if use_editable:
    EXPECTED_OUTPUT = EXPECTED_OUTPUT.format(version="")
else:
    EXPECTED_OUTPUT = EXPECTED_OUTPUT.format(version="==0.0.0")


def run(*args, **kwargs):
    if sys.version_info >= (3, 5):
        subprocess.run(*args, check=True, **kwargs)
    else:
        subprocess.call(*args, **kwargs)


def main():
    fep_copy = TEST_DIR / "fastentrypoints.py"
    shutil.copy2(str(PROJECT_DIR/"fastentrypoints.py"), str(fep_copy))

    testenv = pathlib.Path("testenv")
    pip = testenv / "bin" / "pip"
    if use_virtualenv:
        run([sys.executable, "-m", "virtualenv", str(testenv)])
    else:
        run([sys.executable, "-m", "venv", str(testenv)])

    if use_editable:
        run([str(pip), "install", "-e", str(TEST_DIR)])
    else:
        run([str(pip), "install", str(TEST_DIR)])

    try:
        with open(str(testenv / "bin" / "hello")) as output:
            output.readline()  # eat shabang line, which is non-deterministic.
            result = output.read().strip()
            assert result == EXPECTED_OUTPUT
    finally:
        shutil.rmtree(str(testenv))
        os.remove(str(fep_copy))


if __name__ == '__main__':
    main()
