from matplotlib import pyplot

import pytest

from pyexample import validate


def test_axes_object_invalid():
    with pytest.raises(ValueError):
        validate.axes_object('junk')


def test_axes_object_with_ax():
    fig, ax = pyplot.subplots()
    fig1, ax1 = validate.axes_object(ax)
    assert isinstance(ax1, pyplot.Axes)
    assert isinstance(fig1, pyplot.Figure)
    assert ax1 is ax
    assert fig1 is fig


def test_axes_object_with_None():
    fig1, ax1 = validate.axes_object(None)
    assert isinstance(ax1, pyplot.Axes)
    assert isinstance(fig1, pyplot.Figure)


@pytest.mark.parametrize(("value", "expected"), [
    (None, []),
    ("", []),
    ([], []),
    ('a', ['a']),
    ([1, 2, 3], [1, 2, 3]),
])
def test_at_least_empty_list(value, expected):
    result = validate.at_least_empty_list(value)
    assert result == expected

