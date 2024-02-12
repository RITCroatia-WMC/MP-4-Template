import difflib
import pytest

from pi_tester import pi_tester
from pi_tester import display_score

def test_pi_tester_RES_1(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","2"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==1


def test_pi_tester_RES_2(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","4","1","5","5"])

    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==4


def test_pi_tester_RES_3(capsys, monkeypatch, printFeedback=True):

    inputs = iter(["1","4","1","5","9","2","6","5","3","5","8","9","1"])


    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
   
    # Execute the function
      # Run the main function
    result = pi_tester()
    #Get the feedback
    captured = capsys.readouterr()

    assert result==12


def test_display_score_pi_neophyte(capsys):
    score = 3
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Neophyte" in captured.out


def test_display_score_pi_novice(capsys):
    score = 9
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Novice" in captured.out, "The output does not contain the \"PI Novice\""


def test_display_score_pi_expert(capsys):
    score = 100
    display_score(score)
    captured = capsys.readouterr()
    assert "PI Expert" in captured.out, "The output does not contain the \"PI Expert\""