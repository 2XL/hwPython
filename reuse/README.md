

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
                        