from setuptools import setup
import fastentrypoints

setup(
    name='fastentrypoints',
    version='0.3',
    py_modules=['fastentrypoints'],
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/fast-entry_points',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    license='BSD',
    entry_points={'console_scripts': ['fastep=fastentrypoints:main']},
)
