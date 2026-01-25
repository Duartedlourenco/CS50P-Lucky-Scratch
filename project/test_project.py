import pytest
from project import calculate_classic_win, validate_bet

def test_scratch():
    ...

def test_classic_game():
    values = {"🍋": 2, "🍒": 4}
    assert calculate_classic_win(["🍋", "🍋", "🍋", "🍒", "⭐"], 10, values) == 20
    assert calculate_classic_win(["🍋", "🍒", "⭐", "🔥", "💎"], 10, values) == 0


    with pytest.raises(ValueError, match="Invalid bet amount"):
        validate_bet(0, 100)

    with pytest.raises(ValueError, match="Insufficient balance"):
        validate_bet(200, 100)


def test_bomb_game():
    ...

def test_manage():
    ...

def test_deposit():
    ...

def test_withdraw():
    ...