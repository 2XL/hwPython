#!/usr/bin/python
# -*- coding: utf-8 -*-

# enable chinese char_set
import sys
import lxml

from urllib.request import urlopen
from bs4 import BeautifulSoup

print(sys.version)


def xrange(x):
    return iter(range(x))


def module_one():
    """
    getting started python
    """
    print("python scalar types and operators")
    print(bool(0))
    print(bool(1))
    print(bool("False"))
    print(bool(False))
    print(bool("True"))

    g = 20

    while g > 0 and g != 0:
        g -= 1
        if g == 10:
            print("g == 10!")
            continue
        else:
            print("g == $1".format(g))

    print("python collections: str, bytes, list, dict, set")

    for i in xrange(20):  # "start from 0 up to 20"
        print(i)

    print("multiline str")

    # universal newlines
    print('''
        你好
        世界
        ''')

    txt_raw_str = r"r' raw string prefix"
    txt_str = str("r' raw string prefix")
    print(type(txt_raw_str), type(txt_str))

    print(txt_str.__rmul__(12))
    print(txt_str.__sizeof__())
    print(txt_str.__str__())
    print(txt_str.capitalize())
    print(txt_str.upper())
    print(txt_str.swapcase())

    # unicode string
    string = 'pythön!'

    # print string
    print('The string is:', string)

    # default encoding to utf-8
    string_utf = string.encode()

    # print result
    print('The encoded version is:', string_utf)

    # list sequence of objects mutable

    print(range(20))
    print(list("你好跑一趟好哦你"))

    # dictionary
    d = {
        '你好': 'hello',
        '世界': 'world'
    }
    print(d)
    print(d['你好'])

    for word in d:
        print(word, d[word])


def get_site_title(url):
    # url = 'https://version1.com'

    soup = BeautifulSoup(urlopen(url), 'html.parser')

    # displaying the title
    # print("Title of the website is : ")
    site_title = soup.title.get_text()

    # for word in site_title.split():
    #     print(word)
    return site_title


def py_execution_model():
    """
    layers

    - python module -> convenient import with API
    - python script -> convenient execution from the cli
    - python program -> perhaps composed of many modules

    considering the context of usage.
    """
    pass


def py_code_convention_pep257():
    """
    convention for docstrings.


    [feature]
    describe the feature/purpose the function enhance.

    Args:
        [var]: [definition of var]
        ...

    [Optional]Returns:
        definition of the type and content.
    """


def py_code_convention_pep8():
    """
    two between functions
    that is the number of lines
    """
    pass


def doc_strings():
    """
    literal strings which document functions, modules, and classes
    must be the first statement in the blocks for these constructs.
    -
    - Sphinx - library to create html doc from python docstrings
    """


def everything_is_an_object():
    type(object)
    print(dir(object))
    """
    python uses named references to objects
    assignment attaches a name to an object
    assigning one name to another makes them both point at the same object
    the garbage collector removes objects with no references
    id() returns a unique integer ID for an object
    `is` determines if two names refers tot he same object
    test for equivalence with `==`
    function arguments are passed by object reference
    rebinding function arguments loses the original object reference
    return passes back an object reference to the caller
    function arguments may have a default value
    default argument value are evaluated once, when the function is defined
    python uses dynamic typing
    python has strong typing
    python names are looked up using the LEGB rule
    global references can be read from local scope
    use global to assign to global references from a local scope
    import and def bind names to objects
    type reports the type of an object
    dir introspects the attributes of an objects
    you can access the name of a function or module with __name__
    docstring can be accessed through __doc__
    use len() to measure the length of a string
    the repetition operator,*, repeats a string an integral number of times
    
    """


def py_code_convention_pop498():
    """
    Commonly called f-strings

    embed expresssions inside literal strings, using a minimal syntax
    """
    import math
    print(f'Math constats: pi={math.pi}, e={math.e}')
    print(f'Math constats: pi={math.pi:.30f}, e={math.e:.50f}')

    return (f"one plus one is {1 + 1}")


def build_in_collections():
    """
    str -> inmutable
    list
    dict
    tuple -> immutable sequence of arbitrary objects -> ('','','',) -> () empty
        (a, b(c,d),e)  =(1,2(3,4),5
    range -> sequence representing an arithmetic progression of integers  -> range(stop), (start, stop), (start, stop, step)
    enumerate([sequence of numbers]) -> (index, value)
    set

    indexing -> 0...Inf ---> -0...-Inf -0==0
    Slicing -> a_list[start:stop] -> sublist --> listing = [1,2,3,4,5]; listing[0:2] >>> [1,2]
    """


def module_two():
    pass


def sh_bang():
    print("#!/usr/bin/python")
    print("chmod +x *.py")


def deep_copy():
    """
    none pointers are shared

    use copy module.
    """


def list_math_behaviour():
    aa = [1, 2, 3]
    print(aa)
    bb = aa * 5
    print(aa)
    print(bb)
    print(bb[:2] * 2)

    del bb[5]
    print(bb)
    bb.remove(1)  # removes the first
    print(bb)

    bbb = list(filter(lambda temp: temp != 1, bb))
    print(bbb)

    bbb += [1, 1, 1]
    bbb.extend([2, 2, 2])
    print(bbb)
    bbb.reverse()
    print(bbb)

    bbb.sort()
    print(bbb)


def dictionaries():
    """
    dict {
        key: value
    }

    as with lists, dict copies are shadow by default


    deep copy =>
    dict(random_dict) || random_dict.copy()
    for merge or override =>
    random_dict.update(another_dict)


    dict.keys() => keys
    dict.values() => values
    dict.items() => [(keys, values),...]
    """


def set_types():
    """
    unordered collection of unique elements
    sets are mutable
    elements in a set must be immutable

    sample_set = {1,2,3,4}

    """
    sample_set = {1, 2, 3, 4}
    sample_set.add(12)
    sample_set.update([12, 22, 222])
    sample_set.remove(1)
    sample_set.discard(12)

    sample_set_copy = sample_set
    print(sample_set_copy == sample_set)
    print(sample_set_copy is sample_set)
    sample_set_copy = sample_set.copy()
    print(sample_set_copy == sample_set)
    print(sample_set_copy is sample_set)
    sample_set_copy = set(sample_set)
    print(sample_set_copy == sample_set)
    print(sample_set_copy is sample_set)

    # operaciones para espacios vectoriales
    sample_set_copy.union(sample_set)
    sample_set_copy.difference(sample_set)
    sample_set_copy.intersection(sample_set)

    print(sample_set_copy.issubset(sample_set),
          sample_set_copy.issuperset(sample_set),
          sample_set_copy.isdisjoint(sample_set))


def protocols():
    """
    A set of operations that a type must support to implement the protocol
    Do not need to be defined as interfaces or base classes.
    Types only need to provide functioning implementations

    Container -> str, list, dict, range, tuple, set, bytes
        in || not in
    Sized -> str, list, dict, range, tuple, set, bytes
        len(container)
    Iterable -> str, list, dict, range, tuple, set, bytes
        for item in iterable:
            ...
    Sequence -> str, list, range, tuple, bytes
        item = sequence[index] -> retrieve item by index
        index = sequence.index(item) -> check if item exist and retreive index
        num = sequence.count(item) -> check if item exist and retreive #num times it appears
        r = reversed(sequence) -> can be reversed
    Mutable Sequence -> list
    Mutable Set -> set
    Mutable Mapping -> dict

    """


def shadow_copy():
    """
    pointers may be shared among copies in deeper layers, changes on one is reflected to others
    """
    listing = [1, 2, 3, 4, 5]
    print(listing[1:2])
    print(listing[:2])
    print(listing[2:])
    print(listing[1:-1])
    print(listing[:])

    copy_listing = listing
    print(listing is copy_listing)  # same id
    print(listing == copy_listing)  # equivalent
    print(id(listing))
    print(id(copy_listing))

    copy_listing = listing[:]  # different identity
    print(listing is copy_listing)  # not same id
    print(listing == copy_listing)  # equivalent
    print(id(listing))
    print(id(copy_listing))

    # >>> [1,5,4]
    copy_listing = listing.copy()  # different identity, the best choice can apply for different types
    print(listing is copy_listing)  # not same id
    print(listing == copy_listing)  # equivalent
    print(id(listing))
    print(id(copy_listing))

    # >>> [1,5,4]
    copy_listing = list(listing)  # different identity
    print(listing is copy_listing)  # not same id
    print(listing == copy_listing)  # equivalent
    print(id(listing))
    print(id(copy_listing))


def exceptions_types():
    """
    Error handling strategies:
        * Check preconditions to prevent exceptions
        * Ask forgiveness to handle exceptions (in favour, avoid interspersed with error handling)
    Type
     Error

    context_manager => clear up actions for exceptions
    try:
        ...
    [except: ] optional
        ...
    finally:
        ...
    errors should never pass silently,unless explicitly silenced.

    platform/version specific adapters...
        windows/linux/macos ...
        android/ios
        browser compatibility specific

    """


def iterable_iteration():
    """
    [expr(item) for item in iterable]
    [lambda(item) for item in iterable]

    iterable.iter() -> iterator object
    iterator.next() -> next value of sequence

    """

    lengths = []
    words = """
    Actively scan device characteristics for identification, Apply market research to generate audience insights, Compartir tus análisis de navegación y grupos de interés con terceros, Create a personalised ads profile, Create a personalised content profile, Develop and improve products, Enriquecer el perfil con información de terceros, Measure ad performance, Measure content performance, Select basic ads, Select personalised ads, Select personalised content, Storage and access to geolocation information for targeted advertising purposes, Storage and access to geolocation information to carry out marketing studies, Store and/or access information on a device, Use precise geolocation data
    """.split()
    for word in words:
        lengths.append(len(word))

    print(lengths)

    from math import factorial
    fact_list = [len(str(factorial(x))) for x in range(20)]
    print(fact_list)
    fact_set = {len(str(factorial(x))) for x in range(20)}
    print(fact_set)
    return fact_set


def comprehensions(fact_set):
    """
    Simple is better than complex

    Code is written once but read over and over again
    fewer is clearer
    """
    from pprint import pprint as 印f
    印f(fact_set)

    国家_首都 = {
        '西班牙': "马德里",
        '荷兰': "阿姆斯特丹",
        '中国': "北京",
    }

    capital_to_country = {capital: country for country, capital in 国家_首都.items()}
    印f(国家_首都)
    印f(capital_to_country)


def generators():
    """
    Iterable defined by functions
    Lazy Evaluation
    Can model sequences with no definite end
    Composable into pipelines

    yield: Generator functions must include at least one yield statement.
    They may also include return statements

    Lazy computations can result in complex flow control.
    Forced evaluation can simplify things during dev.

    Generators only do enough work to produce requested data.
    This allows generators to model infinite or just very large sequences.

    Example of such sequences are:
        Random()
        Fibonacci
        Sensor readings
        Mathematical sequences
        Contents of large files


    Generator expressions:
    (expr(item) for item in iterable)

    to recreate a generator from a generator expression you must execute the expression again.
    """

    def fibonacci():
        yield 2
        aa = 2
        bb = 1
        while True:
            yield bb
            aa, bb = bb, aa + bb

    def sample123():
        print("about to yield 1")  # 1
        yield 1  # 1
        print("about to yield 2")  # 2
        yield 2  # 2
        print("about to yield 3")  # 3
        yield 3  # 3
        print("about to yield exit")  # 3
        print("about to yield exit")  # 3
        return None

    index = 0
    for x in sample123():
        index += 1
        print("round ", index, ": ", x)
        continue

    num_set = 10
    fib = fibonacci()
    while True:
        if num_set == 0:
            break
        print(num_set, next(fib))
        num_set -= 1

    # one line generator expression
    ten_square = (x * x for x in range(10))
    print(list(ten_square)[5:8])
    hundred_square = (x * x for x in range(100))
    print(sum(list(hundred_square)))
    from sympy import isprime
    hundred_square_prime = (x * x for x in range(100) if isprime(x))
    print(list(hundred_square_prime))

    from itertools import count, islice
    print("Iter tools")
    hundred_square_prime_iterable = islice((x for x in count() if isprime(x)), 100)

    print(list(hundred_square_prime_iterable)[-10:-1])
    print(sum(list(hundred_square_prime_iterable)[-10:-1]))  # need to recreate to work

    hundred_square_prime_iterable = islice((x for x in count() if isprime(x)), 100)
    print(sum(list(hundred_square_prime_iterable)[-10:-1]))

    # boolean aggregation:
    """
    any: determines if any elements in a series are true
    all: determines if all elements in a series are true
    """
    print(all([True, True, False]))
    print(all([True, True, True]))
    print(all([False, False]))
    print(any(isprime(x) for x in range(100, 110)))


def object_oriented():
    pass


if __name__ == '__main__':
    # # target url
    # site_title = get_site_title('https://version1.com')
    # print(site_title)
    # pass
    # everything_is_an_object()
    #
    # hello = object()
    # empty_tuple = ()
    # multi_tuple = (1, 2, (3, 4), 5)
    # (a, b, (c, d), e) = multi_tuple
    #
    # print(4 in multi_tuple)
    # print(5 in multi_tuple)
    #
    # numbers = ';'.join(['one', 'two', 'three'])
    #
    # print(numbers)
    #
    # print(numbers.partition('two'))
    #
    # country, _, city = "Spain Barcelona".partition(" ")
    # # _  supress unused separators
    # print(country, city)
    # print(py_code_convention_pop498())
    #
    # shadow_copy()
    # list_math_behaviour()
    #
    # set_types()
    # comprehensions(iterable_iteration())
    # generators()
    """
    zip: for bundling lists
    """

    pair = [x * 2 - 1 for x in range(1, 10)][:]
    odd = [x * 2 for x in range(1, 10)][:]
    from random import seed, random

    seed(1)  # pseudo random
    random_values = [random() for x in xrange(10)]

    for x in zip(odd, pair, random_values):
        print(x, "average: ", sum(x) / len(x))
    from itertools import chain

    values = chain(pair, odd, random_values)
    print(all(x > 0 for x in values))

    values = chain(pair, odd, random_values)
    for x in values:
        print(x)
