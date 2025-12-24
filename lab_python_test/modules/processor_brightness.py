from .processor import ImageProcessor

class BrightnessProcessorDecorator(ImageProcessor):
    def __init__(self, processor):
        self._processor = processor

    def load(self):
        self._processor.load()

    def calculate_brightness(self, pixel):
        smoothed = self._apply_smoothing(pixel)
        return self._processor.calculate_brightness(smoothed)

    def get_brightness_grid(self):
        return self.image

    def _apply_smoothing(self, pixel):
        return int(pixel * 0.5)
