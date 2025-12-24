import pytest
from main import solve_biquadratic

def test_four_real_roots():
    result = solve_biquadratic(1, -5, 4)
    expected = [-2, -1, 1, 2]
    assert sorted(result) == sorted(expected)

def test_no_real_roots():
    result = solve_biquadratic(1, 2, 3)
    assert len(result) == 0

def test_degenerate_case_A_zero():
    result = solve_biquadratic(0, 1, -4)
    expected = [-2, 2]
    assert sorted(result) == sorted(expected)

def test_infinite_solutions():
    result = solve_biquadratic(0, 0, 0)
    assert result == ["Бесконечно много решений"]

def test_single_zero_root():
    result = solve_biquadratic(0, 5, 0)
    assert result == [0.0]

def test_double_zero_root():
    result = solve_biquadratic(1, 0, 0)
    assert result == [0.0]

def test_negative_coefficients():
    result = solve_biquadratic(1, -6, 9)
    expected = [-1.7320508075688772, 1.7320508075688772] 
    assert len(result) == 2
    assert abs(result[0] - expected[0]) < 1e-9
    assert abs(result[1] - expected[1]) < 1e-9