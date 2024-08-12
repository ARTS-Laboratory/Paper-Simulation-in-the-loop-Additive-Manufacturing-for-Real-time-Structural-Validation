from typing import List

import cv2
import keras
import numpy as np
from skimage import measure

from .feeders import ImageFeeder
from .runners import FEARunner


class Analyzer:

    SIZE_X: int = 512
    SIZE_Y: int = 512
    RESIZE_X: int = 1368
    RESIZE_Y: int = 1020

    img_feeder: ImageFeeder
    img_model: keras.models.Model
    fea_runner: FEARunner

    n_layers: int

    def __init__(
        self,
        img_feeder: ImageFeeder,
        img_model: keras.models.Model,
        fea_runner: FEARunner,
        n_layers: int,
    ) -> None:
        self.img_feeder = img_feeder
        self.img_model = img_model
        self.fea_runner = fea_runner
        self.n_layers = n_layers

    def analyze(self) -> None:
        self._start()
        for curr_layer in range(self.n_layers):
            # preprocess image
            img: np.ndarray = self.img_feeder.fetch()
            img: np.ndarray = img/255
            #print(img)
            img = cv2.resize(img, (Analyzer.SIZE_Y, Analyzer.SIZE_X))
            # run img through model
            img = np.expand_dims(img, axis=0)
            imgss: np.ndarray=np.expand_dims(img, axis=-1)
	    #print(imgss.shape)
            #imgs: np.ndarray = np.expand_dims(img, axis=0)
            preds: np.ndarray = self.img_model.predict(imgss)
            # extract mask from preds
            mask: np.ndarray = np.argmax(preds, axis=3)[0, :, :]
            mask = cv2.resize(mask, (Analyzer.RESIZE_Y, Analyzer.RESIZE_X),
                              interpolation=cv2.INTER_NEAREST)
            mask = np.array(mask, dtype=np.uint8)
            #print(mask)
            #print(mask.shape)
            porosity_area = 1
            for i in range(1368):
                for j in range(1020):
                    #print('here')

                    if mask[i][j] == 3 or mask[i][j] == 4:
                        porosity_area += 1
                        mask[i][j] = 1
                    # elif mask[i][j] == 4:
                    #     mask[i][j] = 2
                    else:
                        pass
                    

            # identify defect contour
            # (n_def, n_pts, 2); c -> (ys, xs)
            contours: List[np.ndarray] = measure.find_contours(mask, 1.5)
            # (n_def, n_pts, 2); c -> (xs, ys)
            contours = list(map(lambda c: np.flip(c, axis=1), contours))
            # run fea
            self.fea_runner.run(curr_layer, contours, porosity_area)
        self._end()

    def _start(self):
        self.img_feeder.start()
        self.fea_runner.start()

    def _end(self):
        self.img_feeder.end()
        self.fea_runner.end()
