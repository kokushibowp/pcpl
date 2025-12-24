from ...modules.processor_brightness import BrightnessProcessorDecorator
from ...modules.processor import PNGProcessorFactory, PNGProcessor
from unittest.mock import Mock, patch
import pytest

def test_calculate_brightness():
    mock_processor = Mock(spec=PNGProcessor)
    mock_processor.calculate_brightness.return_value = 100
    brightness_processor = BrightnessProcessorDecorator(mock_processor)
    result = brightness_processor.calculate_brightness(10)
    #with patch.object(brightness_processor, '_apply_smoothing', return_value=100):
    #    result = brightness_processor.calculate_brightness(10)
    assert result == 100