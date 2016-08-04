from setuptools import setup
try:
    import fastentrypoints
except ImportError:
    from urllib import request
    fastep = request.urlopen('https://raw.githubusercontent.com/ninjaaron/fast-entry_points/master/fastentrypoints.py')
    namespace = {}
    exec(fastep.read(), namespace)

setup(
    name='fastentrypoints',
    version='0.2',
    py_modules=['fastentrypoints'],
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/fast-entry_points',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    license='BSD',
    entry_points={'console_scripts': ['fastep=fastentrypoints:main']},
)
