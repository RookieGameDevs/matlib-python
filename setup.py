from setuptools import setup
from setuptools.command.build_py import build_py
import os
import shlex
import site
import subprocess as sp
import sys


def lib_suffix():
    if sys.platform.startswith('linux'):
        return 'so'
    elif sys.platform.startswith('darwin'):
        return 'dylib'
    elif sys.platform.startswith('win32') or sys.platform.startswith('cygwin'):
        return 'dll'


class Build(build_py):

    def run(self):
        # compile matlib
        path = os.path.dirname(os.path.abspath(__file__))
        prefix = os.path.join(path, 'build')
        cmd = shlex.split(
            './waf configure --prefix={prefix} build install'.format(prefix=prefix))
        sp.check_call(cmd, cwd=os.path.join(path, 'src/matlib'))

        build_py.run(self)


setup(
    name='matlib',
    version='0.1.2',
    packages=['matlib'],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['build.py:ffi'],
    install_requires=['cffi>=1.0.0'],
    cmdclass={'build_py': Build},
    data_files=[
        (site.getsitepackages()[0], ['build/lib/libmat.{suffix}'.format(suffix=lib_suffix())])
    ],

    # metadata for PyPI
    author='Ivan Nikolaev',
    author_email='voidexp@gmail.com',
    description='Python wrapper for matlib C library',
    license='BSD',
    keywords='math matrix vector linear algebra',
    url='https://github.com/RookieGameDevs/matlib-python')
