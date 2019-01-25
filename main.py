# -*- coding: utf-8 -*-
"""

Script Name: main.py
Author: Do Trinh/Jimmy - 3D artist.

Description:

"""
# -------------------------------------------------------------------------------------------------------------
from __future__ import absolute_import, unicode_literals

# Python
import os

__envKey__ = 'DAMGTEAM'
__envVal__ = os.getcwd()

from pprint import pprint
from cores.environment import System_EnvVariables
env = System_EnvVariables(__envKey__, __envVal__, 'add')
pprint(env)

# -------------------------------------------------------------------------------------------------------------
# Created by panda on 21/01/2019 - 8:15 PM
# © 2017 - 2018 DAMGteam. All rights reserved