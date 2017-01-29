from setuptools import setup
from setuptools.command.install import install
import os
import shlex
import subprocess as sp
import sys


class Install(install):

    def run(self):
        path = os.path.dirname(os.path.abspath(__file__))
        prefix = os.path.join(path, 'build')
        cmd = shlex.split(
            './waf configure --prefix={prefix} build install'.format(prefix=prefix))
        sp.check_call(cmd, cwd=os.path.join(path, 'src/matlib'))

        install.run(self)


setup(
    name='matlib',
    version='0.1+d302b04',
    packages=['matlib'],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['build.py:ffi'],
    install_requires=['cffi>=1.0.0'],
    cmdclass={'install': Install},

    # metadata for PyPI
    author='Ivan Nikolaev',
    author_email='voidexp@gmail.com',
    description='Python wrapper for matlib C library',
    license='BSD',
    keywords='math matrix vector linear algebra',
    url='https://github.com/RookieGameDevs/matlib-python')
