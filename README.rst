SHORT FILM PIPELINE
===================

This application can be used to build, manage, and optimise film making pipelines. The latest version is compatible
with Windows 10 and may run on earlier versions. It does not run in Maya 2016 or lower.

Due to VFX Reference Platform and the large invention, we need to stay with python 2.7 but expect to migrate to python 3 in 2019 (Delayed to 2020).
Details are `here <http://www.vfxplatform.com>`_

REQUIREMENTS
============

Python 3.6 for Windows:

    - 64 bit `download <https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86_64.exe>`_

    - 32 bit `download <https://repo.anaconda.com/archive/Anaconda3-5.2.0-Windows-x86.exe>`_

Also require extra python packages, you do not have to worry about it, it will be automatically installed.

SOFTWARE PACKAGE
======================

    - `Maya 2017 and/or Maya 2018 <https://www.autodesk.com/education/free-software/maya>`_ with `VMM for maya <https://www.mediafire.com/#gu9s1tbb2u4g9>`_, `Vray 3.6 <https://www.chaosgroup.com/vray/maya>`_ & `Phoenix FD 3.0 <https://www.chaosgroup.com/phoenix-fd/maya>`_
    - `Mari <https://www.foundry.com/products/mari>`_
    - `Nuke <https://www.foundry.com/products/nuke>`_
    - `ZBrush <https://pixologic.com/zbrush/downloadcenter/>`_
    - `Houdini <https://www.sidefx.com/download/>`_

NOTE:

    - You can install Photoshop, Premiere, After Effects or anything you want with `Adobe Creative Cloud <https://www.adobe.com/creativecloud/catalog/desktop.html>`_
    - For VMM for maya, remember to configure the path once it is opened in Maya. (sadly, the author has stopped developing the plugin.)

LIBRARY SUPPORT
===============

I spent many years to build this library for texturing and referencing. The library is now freely availalbe to everyone.
You may also find the following libraries useful, You will need an `mediafie <https://mediafire.com>`_ account to be able to download.

    - `ALPHA library <https://www.mediafire.com/#21br3oz8gf44j>`_
    - `HDRI library <https://www.mediafire.com/#33moon9n0qagc>`_
    - `TEXTURE library <https://www.mediafire.com/#v5t32j935afg7>`_

HOW TO USE PIPELINE MANAGER
===========================

Go to the diretory of 'PipelineTool' folder, hold down Shift + right-click -> Open PowerShell window here/Open command window here
In CommandPrompt/WindowShell:

.. code:: bash

    start python main.py                             python setup.py build

REFERENCE
=========

For Plugins/Files that I am using, you can see `here <bin/data/docs/reference.rst>`_.
Copyright (C) 2017 - 2018 by DAMGteam - `details <bin/data/docs/copyright.rst>`_.

NOTE:
====

    - Put note here.