# Image Enhancement Tool

## Overview
A powerful Python-based image enhancement tool that provides various image processing capabilities including gamma correction, histogram equalization, brightness/contrast adjustment, and more. This tool is designed to help users enhance and modify their images through an interactive command-line interface.

## Features
- **Gamma Correction**: Adjust image gamma for better exposure
- **Histogram Equalization**: Improve image contrast automatically
- **Brightness Adjustment**: Modify image brightness levels
- **Contrast Adjustment**: Enhance image contrast
- **Sharpness Control**: Adjust image sharpness
- **Saturation Control**: Modify color saturation
- **Exposure Adjustment**: Fine-tune image exposure
- **Real-time Preview**: View changes immediately
- **High-quality Saving**: Save images in JPEG or PNG format with optimized settings

## System Requirements
- Python 3.6 or higher
- Required Python packages (automatically installed via requirements.txt):
  - opencv-python >= 4.5.0
  - numpy >= 1.19.0
  - Pillow >= 8.0.0
  - scikit-image >= 0.18.0

## Installation
1. Clone or download this repository
2. Navigate to the project directory
3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage
1. Run the program:
```bash
python MainCode.py
```

2. When prompted, enter the path to your image file

3. Use the interactive menu to apply various enhancements:
   - 1: Gamma correction
   - 2: Histogram Equalization
   - 3: Brightness adjustment
   - 4: Contrast adjustment
   - 5: Sharpness adjustment
   - 6: Saturation adjustment
   - 7: Exposure adjustment
   - 8: Show current image
   - 9: Save the image
   - 0: Exit

## Image Processing Functions

### Gamma Correction
- Adjusts the gamma value of the image
- Values < 1 make the image brighter
- Values > 1 make the image darker
- Default value: 1.0

### Histogram Equalization
- Automatically improves image contrast
- Works in YCrCb color space
- Preserves color information while enhancing details

### Brightness Adjustment
- Modifies image brightness
- Factor > 1 increases brightness
- Factor < 1 decreases brightness
- Default value: 1.0

### Contrast Adjustment
- Enhances image contrast
- Factor > 1 increases contrast
- Factor < 1 decreases contrast
- Default value: 1.0

### Sharpness Adjustment
- Controls image sharpness
- Factor > 1 increases sharpness
- Factor < 1 decreases sharpness
- Default value: 1.0

### Saturation Adjustment
- Modifies color saturation
- Factor > 1 increases saturation
- Factor < 1 decreases saturation
- Default value: 1.0

### Exposure Adjustment
- Adjusts image exposure using logarithmic correction
- Gain > 1 increases exposure
- Gain < 1 decreases exposure
- Default value: 1.0

## Technical Details

### Image Processing Pipeline
1. Image Loading
   - Supports various image formats
   - Converts to RGB color space
   - Handles errors gracefully

2. Processing
   - Uses numpy arrays for efficient computation
   - Implements various image enhancement algorithms
   - Maintains image quality during processing

3. Image Saving
   - Optimized JPEG encoding
   - Minimal PNG compression
   - Quality preservation

## Dependencies and References
- OpenCV (cv2): For color space conversion and histogram equalization
- NumPy: For efficient array operations
- Pillow (PIL): For image loading, saving, and basic enhancements
- scikit-image: For advanced image processing operations

## Error Handling
The program includes comprehensive error handling for:
- Invalid file paths
- Unsupported image formats
- Processing errors
- Invalid user input

## Best Practices
1. Always work with a copy of your original image
2. Save your work frequently
3. Preview changes before saving
4. Use appropriate enhancement values for your specific image

## Contributing
Feel free to contribute to this project by:
1. Forking the repository
2. Creating a feature branch
3. Submitting a pull request

## License
This project is open source and available under the MIT License.

## Author
[Your Name/Organization]

## Acknowledgments
- OpenCV community for image processing algorithms
- Python Imaging Library (PIL) team
- scikit-image contributors
