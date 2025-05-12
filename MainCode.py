import cv2
import numpy as np
from PIL import Image, ImageEnhance
from skimage import exposure, img_as_float, img_as_ubyte


def load_image(path: str) -> Image.Image:
    """Load an image from disk and convert to RGB format.

    Args:
        path (str): Path to the image file (e.g., 'image.jpg').

    Returns:
        Image.Image: PIL Image object in RGB format.

    Raises:
        FileNotFoundError: If the image file does not exist.
        ValueError: If the file is not a valid image.
    """
    return Image.open(path).convert('RGB')


def save_image(image: Image.Image, path: str, quality: int = 100) -> None:
    """Save the image as JPEG or PNG with specified quality.

    Args:
        image (Image.Image): PIL Image object to save.
        path (str): Output file path (e.g., 'output.jpg' or 'output.png').
        quality (int, optional): JPEG quality (1–100). Defaults to 100.

    Notes:
        - For JPEG, uses optimized encoding with no chroma subsampling.
        - For PNG, uses minimal compression for faster saving.
    """
    ext = path.split('.')[-1].lower()
    options = {}
    if ext in ('jpg', 'jpeg'):
        options = {'quality': quality, 'optimize': True, 'subsampling': 0}
    elif ext == 'png':
        options = {'compress_level': 1}
    image.save(path, **options)
    print(f"Saved: {path}")


def apply_gamma(image: Image.Image, gamma: float = 1.0) -> Image.Image:
    """Apply gamma correction to the image.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        gamma (float, optional): Gamma value (e.g., <1 for brighter, >1 for darker). Defaults to 1.0.

    Returns:
        Image.Image: Gamma-corrected PIL Image.

    Notes:
        - Converts to float array for processing, clips values to [0,1], and converts back to uint8.
    """
    arr = img_as_float(np.array(image))  # Convert to [0,1] float array
    corrected = exposure.adjust_gamma(arr, gamma)  # Apply gamma correction
    corrected = np.clip(corrected, 0, 1)  # Ensure values stay in [0,1]
    return Image.fromarray(img_as_ubyte(corrected))  # Convert back to uint8 PIL Image


def apply_hist_eq(image: Image.Image) -> Image.Image:
    """Apply histogram equalization to the Y channel in YCrCb color space.

    Args:
        image (Image.Image): Input PIL Image in RGB format.

    Returns:
        Image.Image: Histogram-equalized PIL Image.

    Notes:
        - Uses OpenCV for color space conversion and histogram equalization.
    """
    arr = np.array(image)  # Convert to NumPy array
    ycrcb = cv2.cvtColor(arr, cv2.COLOR_RGB2YCrCb)  # Convert to YCrCb
    ycrcb[:, :, 0] = cv2.equalizeHist(ycrcb[:, :, 0])  # Equalize Y channel
    rgb = cv2.cvtColor(ycrcb, cv2.COLOR_YCrCb2RGB)  # Convert back to RGB
    return Image.fromarray(rgb)  # Convert to PIL Image


def adjust_brightness(image: Image.Image, factor: float = 1.0) -> Image.Image:
    """Adjust image brightness.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        factor (float, optional): Brightness scale (e.g., >1 to increase). Defaults to 1.0.

    Returns:
        Image.Image: Brightness-adjusted PIL Image.
    """
    return ImageEnhance.Brightness(image).enhance(factor)


def adjust_contrast(image: Image.Image, factor: float = 1.0) -> Image.Image:
    """Adjust image contrast.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        factor (float, optional): Contrast scale (e.g., >1 to increase). Defaults to 1.0.

    Returns:
        Image.Image: Contrast-adjusted PIL Image.
    """
    return ImageEnhance.Contrast(image).enhance(factor)


def adjust_sharpness(image: Image.Image, factor: float = 1.0) -> Image.Image:
    """Adjust image sharpness.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        factor (float, optional): Sharpness scale (e.g., >1 to sharpen). Defaults to 1.0.

    Returns:
        Image.Image: Sharpness-adjusted PIL Image.
    """
    return ImageEnhance.Sharpness(image).enhance(factor)


def adjust_saturation(image: Image.Image, factor: float = 1.0) -> Image.Image:
    """Adjust image color saturation.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        factor (float, optional): Saturation scale (e.g., >1 to increase). Defaults to 1.0.

    Returns:
        Image.Image: Saturation-adjusted PIL Image.
    """
    return ImageEnhance.Color(image).enhance(factor)


def adjust_exposure(image: Image.Image, gain: float = 1.0) -> Image.Image:
    """Apply logarithmic exposure adjustment.

    Args:
        image (Image.Image): Input PIL Image in RGB format.
        gain (float, optional): Exposure gain (e.g., >1 to increase). Defaults to 1.0.

    Returns:
        Image.Image: Exposure-adjusted PIL Image.

    Notes:
        - Uses scikit-image's logarithmic adjustment with clipping to avoid overflow.
    """
    arr = img_as_float(np.array(image))  # Convert to [0,1] float array
    exp = exposure.adjust_log(arr, gain)  # Apply logarithmic exposure
    exp = np.clip(exp, 0, 1)  # Ensure values stay in [0,1]
    return Image.fromarray(img_as_ubyte(exp))  # Convert back to uint8 PIL Image


def main() -> None:
    """Run the interactive image processing loop.

    Prompts the user for an image path, then provides a menu to apply transformations,
    display the image, save the result, or exit. Tracks whether the image has been modified
    to prevent unnecessary saves.
    """
    path = input("Path: ")
    try:
        img = load_image(path)  # Load the initial image
    except Exception as e:
        print("Error loading image:", e)
        return

    current = img.copy()  # Working copy of the image
    modified = False  # Flag to track changesIOLoops = True  # Prevent recursive imports
    modified = False

    while True:
        print("\n1: Gamma \n2: HistEq \n3: Brightness \n4: Contrast "
              "\n5: Sharpness \n6: Saturation \n7: Exposure \n8: Show \n9: Save \n0: Exit")
        choice = input("Choose: ")
        if choice == '0':
            break
        elif choice == '1':
            g = float(input("Gamma [1]: "))  # Get gamma value
            current = apply_gamma(current, g)  # Apply gamma correction
            modified = True
        elif choice == '2':
            current = apply_hist_eq(current)  # Apply histogram equalization
            modified = True
        elif choice == '3':
            f = float(input("Brightness [1]: "))  # Get brightness factor
            current = adjust_brightness(current, f)  # Adjust brightness
            modified = True
        elif choice == '4':
            f = float(input("Contrast [1]: "))  # Get contrast factor
            current = adjust_contrast(current, f)  # Adjust contrast
            modified = True
        elif choice == '5':
            f = float(input("Sharpness [1]: "))  # Get sharpness factor
            current = adjust_sharpness(current, f)  # Adjust sharpness
            modified = True
        elif choice == '6':
            f = float(input("Saturation [1]: "))  # Get saturation factor
            current = adjust_saturation(current, f)  # Adjust saturation
            modified = True
        elif choice == '7':
            g = float(input("Exposure [1]: "))  # Get exposure gain
            current = adjust_exposure(current, g)  # Adjust exposure
            modified = True
        elif choice == '8':
            current.show()  # Display the current image
        elif choice == '9':
            if modified:
                save_image(current, input("Save as: "))  # Save if modified
                modified = False
            else:
                print("Nothing to save.")  # No changes to save
        else:
            print("Invalid.")  # Handle invalid input

        if modified:
            print("Applied.")  # Confirm modification
            current.show()  # Show updated image

if __name__ == '__main__':
    main()