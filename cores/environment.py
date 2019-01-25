# -*- coding: utf-8 -*-
"""

Script Name: env.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

import os, subprocess, json

from damgteam.base import DAMG

class System_EnvVariables(DAMG):

    """
    This class is all about system environment variable, you can set new, edit or delete or put path into PATH variable.
    This class works only at user level.
    """

    _envKeys                                            = [k for k in os.environ.keys()]        # Environtment keys
    _envVals                                            = [v for v in os.environ.values()]      # Environtment variables
    _paths                                              = os.getenv('PATH').split(';')          # Paths in PATH

    # _data                                               = dict()
    # for key in _envKeys:
    #     _data[key]                                      = os.environ[key]

    def __init__(self, envKey=None, envVal=None, add='add'):
        """
        Do something with environment variable.
        :param envKey: environment key.
        :param envVar: environment variable.
        """
        super(System_EnvVariables, self).__init__()

        self.envKey                                     = envKey
        self.envVal                                     = envVal
        self.add                                        = add

        for key in self._envKeys:
            self._data[key]                             = os.getenv(key)

        if self.add == 'add':
            if not self.envKey is None and not self.envVal is None:
                print('Adding key: {0} and value: {1}'.format(self.envKey, self.envVal))
                self.set_env_var(self.envKey, self.envVal)
        elif self.add == 'remove' or self.add == 'del' or self.add == 'delete':
            if self.check_envKey(self.envKey):
                print('Removing key: {0}'.format(self.envKey))
                self.remove_env_var(self.envKey)
        elif self.add == 'add_to_path':
            if not self.envVal is None:
                print('Add {0} to PATH variable.'.format(self.envVal))
                self.add_to_PATH(self.envVal)
        else:
            print('Not recognise intention from user.')

    def set_env_var(self, envKey, envVal):
        """
        Setting environment variable.
        """
        try:
            os.getenv(envKey)
        except KeyError:
            print('{0} is not existed, create new environment key.'.format(envKey))
            subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
        else:
            if os.getenv(envKey) is None:
                print('{0} has value as None, assign new value {1}'.format(envKey, envVal))
                subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
            else:
                if os.getenv(envKey) != envVal:
                    print('{0} has different value, edit to: {1}'.format(envKey, envVal))
                    subprocess.Popen('SetX {0} {1}'.format(envKey, envVal), shell=True).wait()
                else:
                    print('{0} has already been set to {1}'.format(envKey, envVal))

        self.register(envKey, envVal)

    def remove_env_var(self, envKey):
        """
        Remove environment variable
        """
        try:
            os.getenv(envKey)
        except KeyError:
            print('Environment key: {0} does not exist'.format(envKey))
        else:
            print('Delete environment key: {0}'.format(envKey))
            subprocess.Popen('REG delete HKCU\Environment /F /V {0}'.format(envKey), shell=True).wait()
            self.deregister(envKey)

    def register(self, envKey, envVal):
        """
        Add key and value into data
        """
        if not envKey in self._envKeys:
            print('append {0} to environment key list'.format(envKey))
            self._envKeys.append(envKey)

        if not envVal in self._envVals:
            print('append {0} to environment value list'.format(envVal))
            self._envVals.append(envVal)

        if os.getenv(envKey) == envVal:
            if envKey in self._envKeys and envVal in self._envVals:
                if not envKey in self._data.keys() or self._data[envKey] != envVal:
                    print('append key: {0} and value: {1} into data'.format(envKey, envVal))
                    self._data[envKey]                   = envVal
        else:
            print('Key: {0}, value: {1} are already in data.'.format(envKey, envVal))

    def deregister(self, envKey):
        """
        Remove environment variable.
        """
        if self.check_envKey(envKey):
            if self.check_envVal(os.getenv(envKey)):
                print('Remove environment value: {0}'.format(os.getenv(envKey)))

            print('Remove environment key: {0}'.format(envKey))
            self._envKeys.remove(envKey)

        if envKey in self._data.keys():
            print('Remove environment variable from data.')
            self._data.pop(envKey)

    def add_to_PATH(self, val):
        """
        Add value into existing PATH
        """
        if not self.check_in_PATH(val):
            new_value = '{0};{1}'.format(val, os.getenv('PATH'))
        else:
            new_value = val

        self.set_env_var('PATH', new_value)
        self._paths.append(new_value)

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

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 25/01/2019 - 12:43 PM
# © 2017 - 2018 DAMGteam. All rights reserved