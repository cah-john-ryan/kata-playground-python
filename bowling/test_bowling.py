import pytest

from bowling.bowling import Bowling

@pytest.fixture
def subject():
    return Bowling()

def throw_frame_repeatedly(subject, number_of_frames, first_throw, second_throw):
    for _ in range(number_of_frames):
        subject.throw(first_throw)
        subject.throw(second_throw)

def throw_spare(subject, first_throw):
    subject.throw(first_throw)
    subject.throw(10 - first_throw)

@pytest.mark.parametrize('number_of_frames, first_throw, second_throw, expected_score', [
    (10, 0, 0, 0),
    (10, 1, 1, 20),
    (10, 2, 2, 40),
    (10, 1, 3, 40)
])
def test_throws_that_do_not_clear_the_frame(subject, number_of_frames, first_throw, second_throw, expected_score):
    throw_frame_repeatedly(subject, number_of_frames, first_throw, second_throw)
    assert subject.score() == expected_score, "The score should be correct for when a frame is not cleared"

def test_spare_is_thrown(subject):
    throw_spare(subject, 5) # frame 1, 10 + 1 because of the spare achieved here
    subject.throw(1) # frame 2, 2 points
    subject.throw(1)
    throw_frame_repeatedly(subject, 8, 0, 0)
    assert subject.score() == 11 + 2, "The score should be correct for when a single spare is made"

def test_spare_is_thrown_plus_five(subject):
    throw_spare(subject, 5) # frame 1, 10 + 5 because of the spare achieved here
    subject.throw(5) # frame 2, 6 points
    subject.throw(1)
    throw_frame_repeatedly(subject, 8, 0, 0)
    assert subject.score() == 15 + 6, "The score should be correct for when a single spare is made"

def test_spare_is_thrown_twice_in_a_row(subject):
    throw_spare(subject, 5) # frame 1, 10 + 5 because of the spare achieved here
    throw_spare(subject, 5) # frame 2, 10 + 1 because of the spare achieved here
    subject.throw(1) # frame 2, 2 points
    subject.throw(1)
    throw_frame_repeatedly(subject, 7, 0, 0)
    assert subject.score() == 15 + 11 + 2, "The score should be correct for when a single spare is made"

def test_a_strike_is_thrown(subject):
    subject.throw(10) # frame 1, 18
    subject.throw(4) # frame 2, 8
    subject.throw(4)
    throw_frame_repeatedly(subject, 8, 0, 0)
    assert subject.score() == 18 + 8, "The score should be correct for when a strike is made"

def test_two_strikes_are_thrown(subject):
    subject.throw(10) # frame 1, 10 + (10 + 4) = 24
    subject.throw(10) # frame 2, 10 + (4 + 4) = 18
    subject.throw(4) # frame 3, 8
    subject.throw(4)
    throw_frame_repeatedly(subject, 7, 0, 0)
    assert subject.score() == 24 + 18 + 8, "The score should be correct for when two strikes are made"

def test_strike_and_spare_combination(subject):
    subject.throw(10) # frame 1, 10 + 10 = 20
    throw_spare(subject, 5) # frame 2, 10 + 4 = 14
    subject.throw(4) # frame 3, 8
    subject.throw(4)
    throw_frame_repeatedly(subject, 7, 0, 0)
    assert subject.score() == 20 + 14 + 8, "The score should be correct for when a strike and spare are present"

def test_perfect_game(subject):
    for _ in range(9):
        subject.throw(10)
    subject.throw(10) # frame 10
    subject.throw(10)
    subject.throw(10)
    assert subject.score() == 300, "The score should be 300 for a perfect game"

def test_all_spare(subject):
    for _ in range(9):
        throw_spare(subject, 5)
    subject.throw(5) # frame 10
    subject.throw(5)
    subject.throw(5)
    assert subject.score() == 150, "The score should be 150 for a all spares in a game"