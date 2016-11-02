from demo import *
"""

__init__.py: can be an empty file but is often used to perform setup needed for the packages (import things, load things into path, etc)

    1. use it to import selected Classes, function. etc. into the package level so they can be conveniently imported.


sample:

package/
    __init__.py
    file.py
    file2.py
    file3.py
    subpackage/
        __init__.py
        submodule1.py
        submodule2.py


case 1: # empty __init__.py

from package.<filename> import <Classname>

case 2: # __init__.py with relative import >> from <filename> import <classname>

from package import <Classname>

case 3: # __init__.py with __all__ which enables import * >> __all__ = ['<filename>', ... ]

from subpackage import *







"""