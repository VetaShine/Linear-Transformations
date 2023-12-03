import cv2
from cv2.typing import MatLike
import numpy as np
import click


def download_image(filename: str) -> MatLike:
    return cv2.imread(filename)


def save_image(filename: str, image: MatLike):
    cv2.imwrite(filename, image)


@click.command()
@click.option("--input", default="input.png", help="Input filename.")
@click.option("--output", default="output.png", help="Output filename.")
@click.option("--gauss", is_flag=True, help="Apply Gaussian blur.")
@click.option("--median", is_flag=True, help="Apply median blur.")
@click.option("--sharpness", is_flag=True, help="Increase the sharpness.")
def transform(input: str, output: str, gauss: bool, median: bool, sharpness: bool):
    image = download_image(input)
    if gauss:
        image = cv2.GaussianBlur(image, (0, 0), 2)
    if median:
        image = cv2.medianBlur(image, 3)
    if sharpness:
        kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
        image = cv2.filter2D(image, -1, kernel)
    save_image(output, image)


if __name__ == "__main__":
    transform()
