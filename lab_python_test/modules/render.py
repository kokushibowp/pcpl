from abc import ABC, abstractmethod

class RenderingStrategy(ABC):
    @abstractmethod
    def render(self, brightness_value):
        pass

class SimpleASCIIStrategy(RenderingStrategy):
    def render(self, brightness_value):
        chars = " .:-=+*#%"
        idx = int(brightness_value / 255 * len(chars))
        return chars[min(idx, len(chars) - 1)]

class ASCIIStrategy(RenderingStrategy):
    def render(self, brightness_value):
        chars = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"
        idx = int(brightness_value / 255 * len(chars))
        return chars[min(idx, len(chars) - 1)]

class BlockASCIIStrategy(RenderingStrategy):
    def render(self, brightness_value):
        chars = "▏▎▍▌▋▊▉█"
        idx = int(brightness_value / 255 * len(chars))
        return chars[min(idx, len(chars) - 1)]
    
class TextImageRenderer:
    def __init__(self, strategy: RenderingStrategy):
        self.strategy = strategy

    def draw(self, brightness_grid):
        f = open('result.txt', 'w')
        for row in brightness_grid:
            str = "".join(self.strategy.render(pixel) for pixel in row)
            print(str)
            f.write(str + '\n')
        f.close()
