from distutils.core import setup, Extension
setup(name='hello',
        version='3.8.10',
        ext_modules=[Extension('hello', ['hello.c'])]
)
