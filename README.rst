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
  sys.exit(entry_function())

This is faster than whatever the heck the normal console scripts do.

Note:

  This bug in setuptools only affects packages built with the normal
  setup.py method. Building wheels avoids the problem and has many other
  benefits as well. ``fastentrypoints`` simply ensures that your user
  scripts will not automatically import pkg_resources, no matter how
  they are built.

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
directory (or into a list of directories you give it as arguments) and
append ``include fastentrypoints.py`` to the MANIFEST.in file, and
add an import statement to setup.py. It is available from PyPI.

You can't really make it a proper dependency because setuptools has to
import it to work, so chicken-egg. right? Luckily, the script is trivial
and will not hurt you project much to copy this 60-line file into the
folder. Be sure to add it to MANIFEST.ini if you want to distributie it
on PyPI.

Let me know if there are places where this doesn't work well. I've
mostly tested it with ``console_scripts`` so far, since I don't write
the other thing.

.. Distributing with PyPI
.. ~~~~~~~~~~~~~~~~~~~~~~
.. PyPI doesn't distribute everything in your project directory, only what
.. it needs to build. This makes importing fastentrypoints a bit tricky. I
.. came up with this crazy hack to make fastentrypoints work even when it
.. is not on the system, thereby making it work with PyPI. It downloads the
.. source into ram an execs it (in its own namespace), and it's gone
.. without a trace.
.. 
.. .. code:: python
.. 
..   try:
..       from urllib import request
..   except ImportError:
..       import urllib2 as request
..   fastep = request.urlopen('https://raw.githubusercontent.com/ninjaaron/fast-entry_points/master/fastentrypoints.py')
..   namespace = {}
..   exec(fastep.read(), namespace)
.. 
.. so yeah, that just happened. If anyone can think of another way to
.. import a module without it being on the system, I'd be glad to hear it.
