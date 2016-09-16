#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyexample
----------------------------------

Tests for `pyexample` module.
"""

import pandas

import pytest
import pandas.util.testing as pdtest

from contextlib import contextmanager
from click.testing import CliRunner

from pyexample import pyexample
from pyexample import cli


@pytest.fixture
def data():
    return pandas.DataFrame({
        'A': [1, 5, 9],
        'B': [2, 6, 0],
        'C': [3, 7, 1],
        'D': [4, 8, 2],
    }, index=list('abc'))


def test_load_example_data(data):
    result = pyexample.load_example_data()
    expected = data.copy()
    pdtest.assert_frame_equal(result, expected)


def test_transpose_square(data):
    result = pyexample.transpose_square(data)
    expected = pandas.DataFrame({
        'a': {'A':  1, 'B':  4, 'C':  9, 'D': 16},
        'b': {'A': 25, 'B': 36, 'C': 49, 'D': 64},
        'c': {'A': 81, 'B':  0, 'C':  1, 'D':  4}
    })
    pdtest.assert_frame_equal(result, expected)


@pytest.mark.parametrize(('value', 'decimal', 'expected'), [
    (0.03010, 2,  '3.01%'), (0.020000, 3,   '2.000%'),
    (0.10000, 2, '10.00%'), (5.000120, 3, '500.012%'),
    ('junk', 2, None),
])
def test_format_as_pct(value, decimal, expected):
    if expected is None:
        with pytest.raises(ValueError):
            pyexample.format_as_pct(value)
    else:
        result = pyexample.format_as_pct(value, decimal=decimal)
        assert result == expected


class TestPyexample(object):

    @classmethod
    def setup_class(cls):
        pass

    def test_something(self):
        pass
    def test_command_line_interface(self):
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0
        assert 'pyexample.cli.main' in result.output
        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--help  Show this message and exit.' in help_result.output

    @classmethod
    def teardown_class(cls):
        pass

