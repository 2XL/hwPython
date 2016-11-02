

**Code Reuse**


* [Reusing Code](http://www.scipy-lectures.org/intro/language/reusing_code.html)


* [What goes in init.py](http://mikegrouchy.com/blog/2012/05/be-pythonic-__init__py.html)

    * Note Rule of thumb
        * Sets of instructions that are called several times should be written inside functions for better code reusability.
        * Functions (or other bits of code) that are called from several scripts should be written inside a module, so that only the module is imported in the different scripts (do not copy-and-paste your functions in the different scripts!).
        
    * How modules are found and imported
        * It is searched by a given list of dirs
            * default: /usr/lib/python
            * envdir: $PYTHONPATH # directory path to keep user-defined modules 
            * sys.path: python -c "import sys; print sys.path" # we can module path append to sys.path if the module path is not visible 

    * Packages: directory that contains many modules.
        * __init__.py tells python that a directory is a Python package, from which modules can be imported.
    
    * [Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
        * use meaningful object names
        * indentation: code alignment <compulsory in python> , <up to 4 space>
        * long lines: not overcome more than 80 chars. can be broken with \        
        * spaces: well-spaced code <after comas>, <around arithmetic ops>, ...
        * use conventions as anybody else from the project. or ww.
        * line break before aritmetic operator
        * import (always on top) with separated lines, but from single line: order>> standard libraries>third party library>local library
        * absolute import is preferible, explicit relative import are an acceptable alternative
        * avoid wild card import > from x import *
        * className: CapWord
        * name: NEVER use: Lower L, Upper i, Upper o as single char variable names. 
        * module name: always Lower and _ if it improves readability.
        * instance method: ALWAYS use self for the first arg to (instance methods) default.
        * class method: ALWAYS use cls for the first arg to (class methods) @classmethod
        * use one leading _ for non-public methods and instance variables
        * use two leading _ to invoke python name mangling rules: it is used mainly to avoid accidentally overloading of methods and name conflicts with supperclasses attributes. (write class that is expected to be extended multiple times)
        * always set __all__ even if its empty to support public API introspection 
        * always define __path__ package special attribute in the package root __init__.py file as an array with the reference of all inner __init__.py path
     
     
        