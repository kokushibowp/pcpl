import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from unittest.mock import MagicMock
import math
from modules import BrightnessProcessorDecorator

scenarios("features/calculate_brightness.feature")



"Контекст для передачи данных между шагами"
@pytest.fixture
def context():
    return {}



@given('a processor with smoothing and brightness calculation')
def step_given_processor(context):
    mock_processor = MagicMock()
    mock_processor.calculate_brightness = MagicMock(
        side_effect=lambda value: value * 0.95
    )
    
    context['processor'] = BrightnessProcessorDecorator(mock_processor)
    context['mock_processor'] = mock_processor



@given(parsers.parse('a grayscale pixel with value {value}'))
def step_given_pixel(context, value):
    context['pixel'] = int(value)
    context['expected_raw_brightness'] = int(value)



@when('I calculate brightness for the pixel')
def step_when_calculate(context):
    context['result'] = context['processor'].calculate_brightness(context['pixel'])



@then(parsers.parse('the brightness value should be approximately {expected}'))
def step_then_brightness(context, expected):
    expected = float(expected)
    assert math.isclose(context['result'], expected, abs_tol=1.0), \
        f"Expected {expected}, got {context['result']}"