# -*- coding: utf-8 -*-
"""

Script Name: base.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, division, print_function, unicode_literals

import os, json, inspect

from PyQt5.QtCore import QObject, QMetaObject

class ObjectEncoder(json.JSONEncoder):

    def default(self, obj):
        if hasattr(obj, 'to_json'):
            return self.default(obj.to_json())
        elif hasattr(obj, '__dict__'):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj)
                if not key.startswith('__')
                and not inspect.isabstract(value)
                and not inspect.isbuiltin(value)
                and not inspect.isfunction(value)
                and not inspect.isgenerator(value)
                and not inspect.isgeneratorfunction(value)
                and not inspect.ismethod(value)
                and not inspect.ismethoddescriptor(value)
                and not inspect.isroutine(value)
            )
            return self.default(d)
        return obj


class Iterator(object):

    def __init__(self, sorted_dict):
        self._dict = sorted_dict
        self._keys = sorted(self._dict.keys())
        self._nr_items = len(self._keys)
        self._idx = 0

    def __iter__(self):
        return self

    def next(self):
        if self._idx >= self._nr_items:
            raise StopIteration

        key = self._keys[self._idx]
        value = self._dict[key]
        self._idx += 1

        return key, value

    __next__ = next


class DAMG(QObject):
    pass


# -------------------------------------------------------------------------------------------------------------
# Created by panda on 23/01/2019 - 6:40 PM
# © 2017 - 2018 DAMGteam. All rights reserved