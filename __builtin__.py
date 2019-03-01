# -*- coding: utf-8 -*-
"""

Script Name: __builtin__.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

# -------------------------------------------------------------------------------------------------------------
""" Import """

# Python
import os

# damgteam
from damgteam.base import DAMG

# -------------------------------------------------------------------------------------------------------------
""" Metadata """

class Version(DAMG):

    def __init__(self, main=13, subfix=0, resubfix=0, step=1):

        self.step = step
        self._main = main
        self._subfix = subfix
        self._resubfix = resubfix

    def get_version(self):
        return "{0}.{1}.{2}".format(self._main, self._subfix, self._resubfix)

    @property
    def mainVer(self):
        return self._main

    @property
    def subVer(self):
        return self._subfix

    @property
    def reVer(self):
        return self._resubfix

class Names(DAMG):

    def envKey(self):
        """
        Environment key
        """
        return 'PIPELINE_TOOL'

    def envVal(self):
        """
        Environment variable: The current directory
        """
        return os.getcwd()

    def organization(self):
        """
        Name of organization
        """
        return 'DAMGTEAM'

    def appname(self):
        """
        Application name
        """
        return 'Pipeline Manager'

    def homepage(self):
        """
        Homepage website name
        """
        return 'damgteam'

class Links(DAMG):

    def __init__(self):

        self.names = Names()
        self._main = self.names.homepage()
        self._prefix = False
        self._subfix = 'com'

    @property
    def main_site(self):
        return self._main

    @property
    def prefix(self):
        if self._prefix:
            return 'https'
        else:
            return 'http'

    @property
    def subfix(self):
        return self._subfix

    def get_link(self):
        return '{0}://www.{1}.{2}'.format(self.prefix, self.main_site, self.subfix)


class Metadata(DAMG):

    def __init__(self):
        super(Metadata, self).__init__(self)

        self.names = Names

    @property
    def envKey(self):
        return self.names.envKey()

    @property
    def envVal(self):
        return self.names.envVal()

    @property
    def organization(self):
        return self.names.organization()

    @property
    def appname(self):
        return self.names.appname()

    @property
    def website(self):
        return Links().get_link()

    @property
    def version(self):
        return Version().get_version()

# -------------------------------------------------------------------------------------------------------------
""" Logging """

class Log(DAMG):

    def full_option(self):
        return "%(funcName)s: %(levelname)s: %(asctime)s %(filename)s, line %(lineno)s: %(message)s"

    def rml(self):
        return "(relativeCreated:d) (levelname): (message)"

    def tlm1(self):
        return "{asctime:[{lvelname}: :{message}"

    def tlm2(self):
        return '%(asctime)s|%(levelname)s|%(message)s|'

    def tnlm1(self):
        return "%(asctime)s  %(name)-22s  %(levelname)-8s %(message)s"

    def tnlm2(self):
        return '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'

# -------------------------------------------------------------------------------------------------------------
""" Date & time """

class Datetime(DAMG):

    def full_option(self):
        return "%d/%m/%Y %H:%M:%S"

    def dmyhms(self):
        return "%d/%m/%Y %H:%M:%S"

    def mdhm(self):
        return "%m-%d %H:%M"


# -------------------------------------------------------------------------------------------------------------
""" Mode """

class Mode(DAMG):

    def personal(self):
        return 'personal'

    def group(self):
        return 'group'

    def studio(self):
        return 'studio'

    def a_plus(self):
        return 'a+'

    def read(self):
        return 'r'

    def write(self):
        return 'w'


# -------------------------------------------------------------------------------------------------------------
""" Format """

class Format(DAMG):

    def __init__(self, log=Log(), datetime=Datetime(), mode=Mode(), metadata = Metadata):

        self._log = log
        self._datetime = datetime
        self._mode = mode
        self._metadata = metadata



# -------------------------------------------------------------------------------------------------------------
# Created by panda on 2/03/2019 - 4:21 AM
# © 2017 - 2018 DAMGteam. All rights reserved