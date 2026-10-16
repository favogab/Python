
from um import count


def test_single_um():
    # A single "um" should count, even with punctuation.
    assert count("um") == 1
    assert count("um?") == 1
    assert count("um!") == 1
    assert count("(um)") == 1


def test_multiple_um():
    # Count every occurrence, not just the first.
    assert count("Um, thanks, um...") == 2
    assert count("um um um") == 3
    assert count("um,um") == 2
    assert count("um... um? UM!") == 3


def test_case_insensitive():
    # Capitalization should not affect the result.
    assert count("UM") == 1
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM! Um? um.") == 3


def test_um_inside_words():
    # Don't count "um" when it's part of another word.
    assert count("yummy") == 0
    assert count("umbrella") == 0
    assert count("album") == 0
    assert count("maximum") == 0
    assert count("Um, thanks for the album.") == 1
    assert count("hello world") == 0
