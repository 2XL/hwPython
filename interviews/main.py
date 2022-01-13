#!/usr/bin/python
# -*- coding: utf-8 -*-

import functools


# 007.py

def 二进制(x=1):
    return int(x, 1 << 1)


def 零():
    return b'0'


def 七():
    return b'1111111'[2:-2]


if __name__ == "__main__":
    print("%s" % functools.reduce(
        lambda a, b: str(a) + str(b),
        (二进制(x) for x in (零(), 零(), 七())), ''))
