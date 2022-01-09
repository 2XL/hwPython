print "Hello World!"


def func(x): return (lambda n: x ** n)


"""
Python lambda functions: aka anonymous functions
    usually used in conjunction with:
        * map
        * reduce
        * filter
"""

number_list = [2, 18, 9, 22, 17, 24, 8, 12, 27]


def is_even(number): return (number % 2 == 0)


def add_one(number): return (number + 1)


def add(x, y): return (x + y)


number_list_even = filter(lambda x: is_even(x), number_list)
number_list_odd = filter(lambda x: not is_even(x), number_list)
number_list_add_one = map(add_one, number_list)
number_list_sum = reduce(add, number_list)

nums = range(2, 50)
for i in range(2, 8):  # 7 x 7 = 49
    print "Round: {} => {}".format(i, nums)  # cada iteracion se eliminan mas numeros.
    nums = filter(lambda x: x == i or x % i, nums)


class D:  attr = 3


class B(D):  pass


class E:  attr = 2


class C(E):  attr = 1


class A(B, C):  pass


X = A()
print(X.attr)

true_div = 1.0 / 2.0  # true division
norm_div = 1.0 // 2.0  # floor division

#  usage:
print func(2)(3)
print number_list
print number_list_even
print number_list_odd
print number_list_add_one
print number_list_sum
print true_div
print norm_div
