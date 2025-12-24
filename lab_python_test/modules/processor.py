from abc import ABC, abstractmethod
import cv2
import os

class ImageProcessorFactory(ABC):
    @abstractmethod
    def create_processor(self, filepath):
        pass

class PNGProcessorFactory(ImageProcessorFactory):
    def create_processor(self, filepath):
        return PNGProcessor(filepath)

class JPGProcessorFactory(ImageProcessorFactory):
    def create_processor(self, filepath):
        return JPGProcessor(filepath)

class ImageProcessor(ABC):
    def __init__(self, filepath):
        self.filepath = filepath
        self.image = None
        self.width = 150
        self.height = 9999
        self.scaling = 2
        os.system(f'mode {self.width}, {self.height}')

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def calculate_brightness(self, pixel):
        pass

class PNGProcessor(ImageProcessor):
    def load(self):
        self.image = cv2.imread(self.filepath, cv2.IMREAD_GRAYSCALE)
        width = self.image.shape[1]
        height = self.image.shape[0]
        new_width = 300
        new_height = int(height * new_width / width / self.scaling)
        self.image = cv2.resize(self.image, dsize=(new_width, new_height), interpolation=cv2.INTER_AREA)

    def get_brightness_grid(self):
        return self.image
    
    def calculate_brightness(self, pixel):
        return pixel


class JPGProcessor(ImageProcessor):
    def load(self):
        self.image = cv2.imread(self.filepath, cv2.IMREAD_GRAYSCALE)
        width = self.image.shape[1]
        height = self.image.shape[0]
        new_width = 150
        new_height = int(height * new_width / width / self.scaling)
        self.image = cv2.resize(self.image, dsize=(new_width, new_height), interpolation=cv2.INTER_AREA)

    def get_brightness_grid(self):
        return self.image
    
    def calculate_brightness(self, pixel):
        return pixel
