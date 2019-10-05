#!/usr/bin/env python3
import subprocess as sp
import os
import pathlib
import shutil

TEST_DIR = pathlib.Path(__file__).absolute().parent
PROJECT_DIR = TEST_DIR.parent
EXPECTED_OUTPUT = r"""# -*- coding: utf-8 -*-
# EASY-INSTALL-ENTRY-SCRIPT: 'dummypkg==0.0.0','console_scripts','hello'
__requires__ = 'dummypkg==0.0.0'
import re
import sys

from dummy import main

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(main())
"""


def main():
    fep_copy = TEST_DIR / "fastentrypoints.py"
    shutil.copy2(str(PROJECT_DIR/"fastentrypoints.py"), str(fep_copy))

    testenv = pathlib.Path("testenv")
    sp.run(["python3", "-m", "venv", str(testenv)], check=True)
    pip = testenv / "bin" / "pip"
    sp.run([str(pip), "install", TEST_DIR], check=True)

    try:
        with open(str(testenv / "bin" / "hello")) as output:
            output.readline()  # eat shabang line, which is non-deterministic.
            assert output.read() == EXPECTED_OUTPUT
    finally:
        shutil.rmtree(str(testenv))
        os.remove(str(fep_copy))


if __name__ == '__main__':
    main()
