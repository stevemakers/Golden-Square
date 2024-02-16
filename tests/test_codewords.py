from lib.codewords import *

def test_codeword_horse_should_return_correct():
    result = check_codeword("horse")
    assert result == "Correct! Come in."

def test_codeword_first_and_last_is_close():
    result = check_codeword('heeeeeheeee')

    assert result == "Close, but nope."

def test_codeword_false_value_returns_wrong():
    result = check_codeword("Rainy")

    assert result == "WRONG!"