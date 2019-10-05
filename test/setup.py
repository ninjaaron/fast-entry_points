from setuptools import setup
import fastentrypoints

setup(
    name='dummypkg',
    version='0.0.0',
    py_modules=['dummy'],
    description='dummy package for the test',
    entry_points={'console_scripts': ['hello=dummy:main']},
)
