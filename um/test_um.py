from um import count


def test_count():
    # Test cases with different occurrences of "um" as a word
    assert count("hello, um, world") == 1
    assert count("yummy") == 0
    assert count("um, um, um") == 3
    assert count("I'm just, um, thinking") == 1


def test_case_insensitivity():
    # Test case with case-insensitive matching
    assert count("Um, um, UM") == 3
    assert count("uM, uM, Um") == 3


def test_word_boundaries():
    # Test cases with words containing "um"
    assert count("album") == 0
    assert count("grumble") == 0
    assert count("mumble") == 0


if __name__ == "__main__":
    test_count()
    test_case_insensitivity()
    test_word_boundaries()
    print("All tests passed")
