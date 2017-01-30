from setuptools import setup
from setuptools.command.build_py import build_py
import os
import shlex
import subprocess as sp


class Build(build_py):

    def run(self):
        # compile matlib
        path = os.path.dirname(os.path.abspath(__file__))
        prefix = os.path.join(path, 'matlib')
        cmd = shlex.split(
            './waf configure --prefix={prefix} build install'.format(prefix=prefix))
        sp.check_call(cmd, cwd=os.path.join(path, 'src/matlib'))

        build_py.run(self)


setup(
    name='matlib',
    version='0.1.3',
    packages=['matlib'],
    setup_requires=['cffi>=1.0.0'],
    cffi_modules=['build.py:ffi'],
    install_requires=['cffi>=1.0.0'],
    cmdclass={'build_py': Build},
    package_data={'matlib': ['lib/*']},

    # metadata for PyPI
    author='Ivan Nikolaev',
    author_email='voidexp@gmail.com',
    description='Python wrapper for matlib C library',
    license='BSD',
    keywords='math matrix vector linear algebra',
    url='https://github.com/RookieGameDevs/matlib-python')
