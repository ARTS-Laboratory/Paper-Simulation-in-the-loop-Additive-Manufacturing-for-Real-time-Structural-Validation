import os
import sys
from abc import abstractmethod

import cv2
import numpy as np


class ImageFeeder:
    def start(self) -> None:
        pass

    def end(self) -> None:
        pass

    @abstractmethod
    def fetch(self) -> np.ndarray:
        """Get the next image from source.

        Returns:
            (np.ndarray): The next image frame.
        """
        pass


class ManualFeederTerminal(ImageFeeder):

    img_root_dir: str
    max_attempt: int

    def __init__(self, img_root_dir: str, max_attempt: int = 3):
        super().__init__()
        self.img_root_dir = img_root_dir
        self.max_attempt = max_attempt

    def fetch(self) -> np.ndarray:
        # prompt filename from user
        print("Enter filename: ", end="", flush=True)
        img_filename: str = sys.stdin.readline().replace("\n", "")
        img_path: str = os.path.join(self.img_root_dir, img_filename)
        # loop until run out of chance
        for curr_attempt in range(self.max_attempt):
            if os.path.exists(img_path):
                break
            print("File does not exist")
            print("Enter filename: ", end="", flush=True)
            img_filename = sys.stdin.readline().replace("\n", "")
            img_path: str = os.path.join(self.img_root_dir, img_filename)
        # raise error if file does not exist
        if not os.path.exists(img_path):
            raise FileNotFoundError
        img: np.ndarray = cv2.imread(img_path, 0)
        return img
