import os
import pickle
from abc import ABC, abstractmethod
from typing import List

import numpy as np


class FEARunner(ABC):

    controus: List[List[np.ndarray]]

    def __init__(self) -> None:
        super().__init__()
        self.controus = list()

    def start(self) -> None:
        self.controus = list()

    def end(self) -> None:
        pass

    def run(self, curr_layer: int, curr_contours: List[np.ndarray], porosity_area) -> None:
        self.controus.append(curr_contours)
        self._run(curr_layer, curr_contours, porosity_area)
        #self._run(curr_layer, curr_contours)

    @abstractmethod
    def _run(self, curr_layer: int, curr_contours: List[np.ndarray], porosity_area) -> None:
        pass


class DummyRunner(FEARunner):

    pkl_export_dir: str

    def __init__(self, pkl_export_dir: str) -> None:
        super().__init__()
        self.pkl_export_dir = pkl_export_dir
        os.makedirs(pkl_export_dir, exist_ok=True)

    def _run(self, curr_layer: int, curr_contours: List[np.ndarray], porosity_area: int) -> None:
    #def _run(self, curr_layer: int, curr_contours: List[np.ndarray]) -> None:
        # save curr_contours as pickle file
        # pickle.dump(
        #     curr_contours,
        #     open(os.path.join(self.pkl_export_dir, f"{curr_layer}.pkl"), "wb"))
        # pickle.dump(
        #     porosity_area,
        #     open(os.path.join(self.pkl_export_dir, f"{curr_layer}.pkl"), "wb"))
        pickle.dump(
            #curr_contours,
            [porosity_area, curr_contours],
            open(os.path.join(self.pkl_export_dir, f"{curr_layer}.pkl"), "wb"), protocol=2)
        # don't run fea if there is no defect in current layer

        #if len(curr_contours) == 1702:
        if curr_layer == 0:
            return
        #os.system("abaqus cae noGUI=goodspecimen_fracture.py")
        os.system("abaqus cae script=goodspecimen_fracture.py")



class AbaqasRunner(FEARunner):

    pkl_export_dir: str

    def __init__(self, pkl_export_dir: str) -> None:
        super().__init__()
        self.pkl_export_dir = pkl_export_dir
        os.makedirs(pkl_export_dir, exist_ok=True)

    def _run(self, curr_layer: int, curr_contours: List[np.ndarray], porosity_area: int) -> None:
        # don't run fea if there is no defect in current layer
        if len(curr_contours) == 0:
            return
        pickle.dump(
            curr_contours,
            open(os.path.join(self.pkl_export_dir, f"{curr_layer}.pkl"), "wb"))
        pickle.dump(
            porosity_area,
            open(os.path.join(self.pkl_export_dir, f"{curr_layer}.pkl"), "wb"))
        os.system("echo run abaqas here")
