# -*- coding: utf-8 -*-
"""

Script Name: __init__.py.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

# Python
import os, subprocess, json

class System_EnvVariables:

    """
    This class is all about system environment variable, you can set new, edit or delete or put path into PATH variable.
    """

    _envKeys                                            = [k for k in os.environ.keys()]        # Environtment keys
    _envVals                                            = [v for v in os.environ.values()]      # Environtment variables
    _paths                                              = os.getenv('PATH').split(';')          # Paths in PATH

    _data                                               = dict()
    for key in _envKeys:
        _data[key]                                      = os.environ[key]

    def __init__(self, envKey=None, envVar=None):
        """
        Do something with environment variable.
        :param envKey: environment key.
        :param envVar: environment variable.
        """
        self.envKey                                     = envKey
        self.envVar                                     = envVar

        if not self.envKey is None and not self.envVar is None:
            self.set_env_var(self.envKey, self.envVar)

    def __str__(self):
        return json.dumps({self.__class__.__name__: self.data}, indent=4)

    def __repr__(self):
        return json.dumps({self.__class__.__name__: self.data}, indent=4)

    def set_env_var(self, envKey, envVal):
        """
        Setting environment variable.
        """
        try:
            os.getenv(envKey)
        except KeyError:
            print('1')
            subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
        else:
            if os.getenv(envKey) is None:
                print('2')
                subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
            else:
                if os.getenv(envKey) != envVal:
                    print('3')
                    subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
                else:
                    print('{0} is already set to {1}'.format(envKey, envVal))

        self.update()

    def add_to_PATH(self, val):
        """
        Add value into existing PATH
        """
        if not val in self._paths:
            new_value = '{0};{1}'.format(val, os.getenv('PATH'))
        else:
            new_value = val

        self.set_env_var('PATH', new_value)

    def update(self):
        """
        Update data of system environment variables.
        """
        self._envKeys                                   = [k for k in os.environ.keys()]
        self._envVals                                   = [v for v in os.environ.values()]
        self._paths                                     = os.getenv('PATH').split(';')

        for key in self._envKeys:
            self._data[key]                             = os.environ[key]

        print('Update environment variable successful.')

    def check_envKey(self, key):
        """
        Check if key is exist or not.
        :param key: key should be a string
        :return: True or False
        """
        if not key in self._envKeys:
            return False
        else:
            return True

    def check_envVal(self, val):
        """
        Check if value is exist or not.
        :param val: value should be a string
        :return: True or False
        """
        if not val in self._envVals:
            return False
        else:
            return True

    def check_in_PATH(self, envVal):
        """
        Check if value in path
        :return: True or False
        """
        if not envVal in self._paths:
            return False
        else:
            return True

    @property
    def keys(self):
        return self._envKeys

    @property
    def values(self):
        return self._envVals

    @property
    def paths(self):
        return self._paths

    @property
    def data(self):
        return self._data

    @keys.setter
    def keys(self, new_envKeys):
        self._envKeys                                   = new_envKeys

    @values.setter
    def values(self, new_envVals):
        self._envVals                                   = new_envVals

    @paths.setter
    def paths(self, new_paths):
        self._paths                                     = new_paths

    @data.setter
    def data(self, new_data):
        self._data                                      = new_data

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 21/01/2019 - 8:57 PM
# © 2017 - 2018 DAMGteam. All rights reserved