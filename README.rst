===========
simple-midi-parser
===========

A simple Python midi file parser

Features
========

* Parses SMFs into python objects

Install
=========

::

    pip install simple_midi_parser

Usage
=========

::

    from simple_midi_parser import parse

    midi = parse('./some.mid')

    # or with a file handle

    with open('./some.mid', 'b') as midfile:
        midi = parse(midfile)

Bugs/Features
=============

Feel free to open a github issue `here <https://github.com/pgk/simple-midi-parser/issues>`_.
