from distutils.core import setup, Extension

setup(name='practice',
        version='3.8.10',
        ext_modules=[Extension('practice', ['practice.c'])]
)

