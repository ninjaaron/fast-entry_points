Fast entry_points
=================
Using ``entry_points`` in your setup.py makes scripts that start really
slowly because it imports ``pkg_resources``, which is a horrible thing
to do if you want your trivial script to execute more or less instantly.
Check it out: https://github.com/pypa/setuptools/issues/510



Importing ``fastentrypoints`` in your setup.py file produces scripts
that looks (more or less) like this:

.. code:: python

  # -*- coding: utf-8 -*-
  import re
  import sys

  from package.module import entry_function

  if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(entry_function())

This is ripped directly from the way wheels do it and is faster than
whatever the heck the normal console scripts do.

Note:

  This bug in setuptools only affects packages built with the normal
  setup.py method. Building wheels avoids the problem and has many other
  benefits as well. ``fastentrypoints`` simply ensures that your user
  scripts will not automatically import pkg_resources, no matter how
  they are built.
  
  When using Python 3.8 and setuptools 47.2 (or newer), console scripts
  do not import pkg_resources.

Usage
-----
To use fastentrypoints, simply copy fastentrypoints.py into your project
folder in the same directory as setup.py, and ``import fastentrypoints``
in your setup.py file. This monkey-patches
``setuptools.command.easy_install.ScriptWriter.get_args()`` in the
background, which in turn produces simple entry scripts (like the one
above) when you install the package.

If you install fastentrypoints as a module, you have the ``fastep``
executable, which will copy fastentrypoints.py into the working
directory (or into a list of directories you give it as arguments) and
append ``include fastentrypoints.py`` to the MANIFEST.in file, and
add an import statement to setup.py. It is available from PyPI.

Be sure to add ``fastentrypoints.py`` to MANIFEST.ini if you want to
distribute your package on PyPI.

Alternatively, you can specify ``fastentrypoints`` as a build system
dependency by adding a ``pyproject.toml`` file (`PEP 518
<https://www.python.org/dev/peps/pep-0518/>`_) with these lines to
your project folder::
 
    [build-system]
    requires = ["setuptools", "wheel", "fastentrypoints"]

It is also possible to install it from PyPI with easy_install in
the setup script:

.. code:: python

  try:
      import fastentrypoints
  except ImportError:
      from setuptools.command import easy_install
      import pkg_resources
      easy_install.main(['fastentrypoints'])
      pkg_resources.require('fastentrypoints')
      import fastentrypoint

Let me know if there are places where this doesn't work well. I've
mostly tested it with ``console_scripts`` so far, since I don't write
the other thing.

Test
----
There is one test. To run it, do ``test/runtest.py``. It installs a
dummy package with fastentrypoints and ensures the generated script is
what is expected.
