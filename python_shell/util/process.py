"""
MIT License

Copyright (c) 2020 Alex Sokolov

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

from io import open
import os
import subprocess

from .version import is_python2_running


__all__ = ('Subprocess',)


_PIPE = subprocess.PIPE

if is_python2_running():
    _CalledProcessError = OSError
else:
    _CalledProcessError = subprocess.CalledProcessError


class Subprocess(object):
    """A wrapper for subprocess module"""

    CalledProcessError = _CalledProcessError
    PIPE = _PIPE

    @staticmethod
    def run(*args, **kwargs):
        """A simple wrapper for run() method of subprocess"""
        if is_python2_running():
            if 'check' in kwargs:
                kwargs.pop('check')
            process = subprocess.Popen(*args, **kwargs)
            process._stdout, process._stderr = process.communicate()
            return process
        else:
            return subprocess.run(*args, **kwargs)

    @classmethod
    def DEVNULL(cls):
        """A wrapper for DEVNULL which does not exist in Python 2"""
        if is_python2_running():
            return open(os.devnull, 'w')
        else:
            return subprocess.DEVNULL
