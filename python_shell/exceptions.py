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

__all__ = ('CommandDoesNotExist', 'ShellException')


class ShellException(Exception):
    """Defines any exception caused by commands run in Shell"""

    _command = None

    def __init__(self, command):
        super(ShellException, self).__init__()
        self._command = command

    def __str__(self):
        return 'Shell command "{} {}" failed with return code {}'.format(
            self._command.command,
            self._command.arguments,
            self._command.return_code)


class CommandDoesNotExist(ShellException):
    """Defines an exception when command does not exist in the environment"""
    def __init__(self, command):
        super(CommandDoesNotExist, self).__init__(command)

    def __str__(self):
        return 'Command "{}" does not exist'.format(self._command.command)
