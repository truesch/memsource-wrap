.. image:: https://travis-ci.org/gengo/memsource-wrap.svg?branch=master
    :target: https://travis-ci.org/gengo/memsource-wrap

memsource-wrap
##############
Memsource API Library for Python

This library requires Python 3.5+.

Note
=======
This repository is a fork of gengo/memsource-wrap. Many thanks for the great work done there!

Install
=======

::

    pip install -e 'git+https://github.com/truesch/memsource-python.git@master#egg=Package'

Uninstall
=========

::

    pip uninstall memsource-wrap

Examples
========

::

    import memsource.memsource

    m = memsource.memsource.Memsource(user_name='<user_name>', password='<password>')
    print(m.client.create('test client'))
    # will return a client object

If you already have token, you can omit user_name and password. In this case, this SDK can skip authentication, so it's bit faster.

::

    import memsource.memsource

    m = memsource.memsource.Memsource(token='your token')
    print(m.client.create('test client'))
    # will return a client object
