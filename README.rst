Fast entry_points
=================
Using ``entry_points`` in your setup.py makes scripts that start really
slowly because it imports ``pkg_resources``, which is a horrible thing
to do if you want your trivial script to execute more or less instantly.
check it out: https://github.com/pypa/setuptools/issues/510

importing ``fastentrypoints`` in your setup.py file produces scripts
that look like this:

.. code:: python

  import sys
  from package.module import entry_function
  sys.exit(sysentry_function())

This is faster than whatever the heck the normal console scripts do.

Usage
-----
To use fastentrypoints, simply copy fastentrypoints.py into your project
folder in the same directory as setup.py, and ``import fastentrypoints``
in your setup.py file. This monkey-patches
``setuptools.command.easy_install.ScriptWriter.get_args()`` in the
background, which, in turn, produces wonderfully simple entry
scripts (like the one above) when you install the package.

If you install fastentrypoints as a module, you have the ``fastep``
executable, which will copy fastentrypoints.py into the working
directory (or into a list of directories you give it as arguments). It
is available from PyPI.

You can't really make it a proper depenency because setuptools has to
import it to work, so chicken-egg. right? Luckily, the script is trivial
and will not hurt you project much to copy this 40-line file into the
folder.

Let me know if there are places where this doesn't work well. I've
mostly tested it with ``console_scripts`` so far, since I don't write
the other thing.
