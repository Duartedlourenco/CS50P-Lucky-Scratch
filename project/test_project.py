from project import calculate_classic_win, validate_bet, deposit_balance, withdraw_balance,calculate_bomb_pot, is_bomb_hit
import pytest

def test_calculate_classic_win():
    values = {"🍋": 2, "🍒": 4}
    assert calculate_classic_win(["🍋", "🍋", "🍋", "🍒", "⭐"], 10, values) == 20
    assert calculate_classic_win(["🍋", "🍒", "⭐", "🔥", "💎"], 10, values) == 0


def test_calculate_bomb_pot():
    multipliers = [1, 1.5, 2]

    assert calculate_bomb_pot(10, 0, multipliers) == 10
    assert calculate_bomb_pot(10, 1, multipliers) == 15
    assert calculate_bomb_pot(10, 2, multipliers) == 20

    with pytest.raises(ValueError):
        calculate_bomb_pot(10, 5, multipliers)


def test_is_bomb_hit():
    assert is_bomb_hit((2, 3), (2, 3)) is True
    assert is_bomb_hit((1, 1), (2, 3)) is False 


def test_validate_bet():
    assert validate_bet(10, 100) is True

    with pytest.raises(ValueError, match="Invalid bet amount"):
        validate_bet(0, 100)

    with pytest.raises(ValueError, match="Insufficient balance"):
        validate_bet(200, 100)


def test_deposit_balance():
    assert deposit_balance(100, 50) == 150
    
    with pytest.raises(ValueError):
        deposit_balance(100, 0)


def test_withdraw_balance():
    assert withdraw_balance(100, 40) == 60

    with pytest.raises(ValueError):
        withdraw_balance(100, 200)