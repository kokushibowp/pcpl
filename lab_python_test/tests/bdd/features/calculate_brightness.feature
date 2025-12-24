Feature: Calculate Brightness for Grayscale Pixel
  As an image processor
  I want to calculate brightness of a grayscale pixel after smoothing
  So that I can generate brightness grids for monochrome images

  Scenario: Calculate brightness of a smoothed grayscale pixel
    Given a processor with smoothing and brightness calculation
    And a grayscale pixel with value 120
    When I calculate brightness for the pixel
    Then the brightness value should be approximately 57