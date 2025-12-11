import pytest
from brute import Brute
from unittest.mock import Mock

@pytest.fixture
def simple_password():
    return Brute("right")

def describe_Brute():
    def bruteOnce_returns_True_when_Correct(simple_password):
        brute = simple_password 
        assert brute.bruteOnce("right") is True

    def bruteOnce_returns_False_when_Incorrect(simple_password):
        brute = simple_password
        assert brute.bruteOnce("wrong") is False

    def bruteMany_calls_bruteOnce(simple_password,mocker):
        brute = simple_password
        mock_bruteOnce = mocker.patch.object(brute,'bruteOnce')
        brute.bruteMany()
        mock_bruteOnce.assert_called()

    def bruteMany_calls_randomGuess(simple_password,mocker):
        brute = simple_password
        mock_randomGuess = mocker.patch.object(brute,'randomGuess',return_value="right")
        brute.bruteMany()
        mock_randomGuess.assert_called()

    def bruteMany_returns_a_time_when_correct(simple_password,mocker):
        brute = simple_password
        mock_randomGuess = mocker.patch.object(brute,'randomGuess',return_value="right")
        assert brute.bruteMany() < 0.2

    def bruteMany_returns_negative_one_when_False(simple_password,mocker):
        brute = simple_password
        mock_randomGuess = mocker.patch.object(brute,'randomGuess',return_value="wrong")
        assert brute.bruteMany(10) is -1
