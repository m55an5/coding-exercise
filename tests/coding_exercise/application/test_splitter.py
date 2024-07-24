from assertpy import assert_that
import pytest
from coding_exercise.application.splitter import Splitter
from coding_exercise.domain.model.cable import Cable


def test_should_not_return_none_when_splitting_cable():
    assert_that(Splitter().split(Cable(10, "coconuts"), 1)).is_not_none()


@pytest.mark.parametrize("length, name, times", [
    (1024, "apples", 64),
    (2, "apples", 1),
])
def test_should_not_raise_value_error_when_valid_cable_length_valid_times(length, name, times):
    c = Splitter().split(Cable(length, name), times)
    assert len(c) > 0


@pytest.mark.parametrize("length, name, times", [
    (1024, "bananas", 65),
    (2, "bananas", 0),
])
def test_should_raise_value_error_when_valid_cable_length_invalid_times(length, name, times):
    splitter = Splitter()
    with pytest.raises(ValueError):
        splitter.split(Cable(length, name), times)


@pytest.mark.parametrize("length, name, times", [
    (1025, "oranges", 64),
    (1, "oranges", 1),
])
def test_should_raise_value_error_when_invalid_cable_length_valid_times(length, name, times):
    splitter = Splitter()
    with pytest.raises(ValueError):
        splitter.split(Cable(length, name), times)


def test_should_return_formatted_cable_name():
    for i in range(9,12):
        cables = [0] * i
        r = Splitter().format_cable_name("coconuts", cables)
        assert f"coconuts-{i:02}" == r


def test_should_raise_value_error_for_invalid_length_less_than_one():
    splitter = Splitter()
    with pytest.raises(ValueError):
        Splitter().split(Cable(5, "coconuts"), 6)


def test_should_not_raise_error_for_valid_remaining_value_of_zero():
    res = Splitter().split(Cable(5, "coconuts"), 2)
    assert len(res) == 5


def test_should_not_raise_error_for_valid_remaining_value_of_not_zero():
    res = Splitter().split(Cable(11, "coconuts"), 3)
    assert len(res) == 6
  

@pytest.mark.parametrize("length, name, times, result", [
    (
        10, "oranges", 1,   [
                                Cable(5, "oranges-01"),
                                Cable(5, "oranges-02")
                            ]
    ), 
    (
        5, "oranges", 2,   [
                                Cable(1, "oranges-01"),
                                Cable(1, "oranges-02"),
                                Cable(1, "oranges-03"),
                                Cable(1, "oranges-04"),
                                Cable(1, "oranges-05"),
                            ]
    )

])
def test_should_pass_with_valid_values(length, name, times, result):
    r = Splitter().split(Cable(length, name), times)
    assert len(r) == len(result)
    for i in range(len(r)):
        assert Cable(r[i].length, r[i].name == result[i])
    
