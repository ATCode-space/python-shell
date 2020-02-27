# Changes

### 2020-02-29

* Enabled support for list shell commands by dir(Shell)
* Enabled command autocomplete in **BPython** and **IPython** for Shell
* Added ability to run shell commands with no-identifier-like name
* Added access to the last executed command even if exception was raised
* Added property "errors" for stderr output
* Added human-understandable behaviour for str() and repr() of Command instance
* Some internal refactoring and bugfixes