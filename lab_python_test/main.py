import sys
import modules
import os
import copy

factory = modules.PNGProcessorFactory()
processor = factory.create_processor(sys.argv[1])
processor.load()
processor_brightness = modules.BrightnessProcessorDecorator(processor)
processor_brightness.load()
renderer = modules.TextImageRenderer(modules.SimpleASCIIStrategy())
renderer2 = modules.TextImageRenderer(modules.ASCIIStrategy())
image = copy.deepcopy(processor.image)
i = 0
j = 0 
for row in processor.image:
    for pixel in row:
        image[i][j] = processor_brightness.calculate_brightness(pixel)
        j += 1
    j = 0
    i += 1
renderer.draw(image)
renderer.draw(processor.get_brightness_grid())