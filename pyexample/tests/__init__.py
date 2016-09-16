# -*- coding: utf-8 -*-

from pkg_resources import resource_filename

import pytest

import pyexample

def test(*args):
    options = [resource_filename('pyexample', 'tests')]
    options.extend(list(args))
    return pytest.main(options)
