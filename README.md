# Simulation-in-the-loop Additive Manufacturing for Real-time Structural Validation

This repo accompanies a paper submitted to Additive Manufacturing in 2024 and contains a reproduction of the methodology demonstrated in that paper.

<p align="center">
<img src="figures/simulation_in_the_loop.png" alt="framework of simulation-in-the-loop " width="600"/>

The framework of simulation-in-the-loop real-time FEA product structural quality validation system.
</p>

<p align="center">
<img src="figures/image_segmentation.png" alt="defect segmentation" width="600"/>

The defect segmentation process with U-net.
</p>

<p align="center">
<img src="figures/architecture.png" alt="process of real-time automatic FEA structural quality validation" width="600"/>

The process of real-time automatic FEA structural quality validation on the fourth layer.
</p>

## Requirements
* Python 3.8.5
* Abaqus 2022
* numpy >= 1.20
* tensorflow
* scikit-learn
* scikit-image
* onnxruntime
* onnx
* tf2onnx
* skl2onnx
* opencv-python
* overrides
* dataclasses-json
* matplotlib
* SciencePlots
* segmentation_models
* watchdog

## File structure
The provided code has the following folder structure, where the files are structured based on the stage of the pipeline. 

- Code
    - FEA
	- final_3d_printer_fea
- Data
    - Defect segmentation results
	- DIC test results
	- Tensile test results
- Specimen


The Code folder contains the two parts: 1) the generated Abaqus Python Script from the simulation and 2)the code for running the FEA simulation.

The Data folder contains the three parts: 1) Defect segmentation results, 2) DIC test results, and 3) Tensile test results.

The Specimen folder is the Gcode for the specimen used in the paper



## How to run the code
1. cd .....\final_3d_printer_fea
2. conda activate fea_printing(Virtual Environment)  
3. python main.py

## Notes
1. Replacing the trained image segmentation result (here: New_specimen_with_prosity_and_long_gap.hdf5 in test folder) with your own.
2. Pay attention to the image size, in the paper we use 1368 X 1020, which is resized to 512 X 512 before input into U-net.
3. Replacing the pregenerated Abaqus Python Script (here: Abaqus_simulation.py ) with your own.

## Licensing and Citation

[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg


Cite as:

@Misc{Fu_2024_SimulationintheLoop,   
  author = {Yanzhou Fu and Austin R.J. Downey},   
  howpublished = {GitHub},  
  title  = {Paper-Simulation-in-the-loop-Additive-Manufacturing-for-Real-time-Structural-Validation},   
  year   = {2024},  
  groups = {{ARTS-L}ab},    
  url    = {https://github.com/ARTS-Laboratory/Paper-Simulation-in-the-loop-Additive-Manufacturing-for-Real-time-Structural-Validation},    
}
