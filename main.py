# -*- coding: utf-8 -*-
"""

Script Name: main.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals
""" Import """

# Python
import os, sys

# PyQt5
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout, QApplication
from PyQt5.QtCore import QCoreApplication

# damgteam
from __builtin__ import __envKey__, __envVal__, __organization__, __appname__, __version__, __website__
from damgteam.base import DAMG
from cores.environment import System_EnvVariables

# -------------------------------------------------------------------------------------------------------------
""" Config """

env = System_EnvVariables(__envKey__, __envVal__, 'add')



class CoreApp(DAMG):                                                    # Core metadata

    key = 'PLM core application'

    def __init__(self, parent=None):
        super(CoreApp, self).__init__(parent)

        self.organization = __organization__
        self.appName = __appname__
        self.version = __version__
        self.website = __website__

        QCoreApplication.setOrganizationName(self.organization)
        QCoreApplication.setApplicationName(self.appName)
        QCoreApplication.setOrganizationDomain(self.website)
        QCoreApplication.setApplicationVersion(self.version)

class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._parent = parent

        self.mainWidget = QWidget()
        self.layout = QGridLayout()
        self.mainWidget.setLayout(self.layout)

        self.buildUI()

    def buildUI(self):

        pass


class PipelineTool(QApplication):

    def __init__(self, appCore=None):
        super(PipelineTool, self).__init__(sys.argv)

        if appCore is None:
            print('Application does not have a core.')
            return

        self.appCore = appCore

        self.setApplicationDisplayName(self.appCore.appName)

        self.layout = MainWindow()

        self.layout.show()
        self.exec_()

if __name__ == '__main__':
    PipelineTool(CoreApp())











# -------------------------------------------------------------------------------------------------------------
# Created by panda on 21/01/2019 - 8:15 PM
# © 2017 - 2018 DAMGteam. All rights reserved