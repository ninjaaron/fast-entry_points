from setuptools import setup
import fastentrypoints

setup(
    name='fastentrypoints',
    version='0.11',
    py_modules=['fastentrypoints'],
    description='Makes entry_points specified in setup.py load more quickly',
    long_description=open('README.rst').read(),
    url='https://github.com/ninjaaron/fast-entry_points',
    author='Aaron Christianson',
    author_email='ninjaaron@gmail.com',
    license='BSD',
    entry_points={'console_scripts': ['fastep=fastentrypoints:main']},
)
