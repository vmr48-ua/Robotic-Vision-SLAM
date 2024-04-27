# Robotic-Vision-SLAM
This project is based on the information and codes provided by Matlab on the topic of vSLAM with a single camera and the contributions of Akbonline for a python implementation of said method.
<p align="center">
  <img src="https://github.com/vmr48-ua/Robotic-Vision-SLAM/assets/78732677/920d9540-620f-4d8f-8cfc-6f25a30bb8ee" alt="Live feature and velocity extraction"/>
</p>

## Algorithm sketch
<p align="justify">To implement a visual Simultaneous Localization And Mapping (vSLAM) workflow, the first step is importing a series of images into a temporary folder. The mapping process is then initialized by grounding a frame as a reference and comparing it to the next so that motion can be tracked. We'll call 'key frames' to each pair of frames whose information has sufficient visual change to ensure proper tracking.</p>


<p align="justify">We will have to plot two different things, the 2D videoframes with the features marked and a 3D representation of said 2D frames where the camera location is induced by triangulation. The initial pose and placement can be derived from the first keyframes, and the features of the posterior frames get compared to those of the first to induce camera location.</p>

<p align="justify">What we call Oriented FAST and rotated BRIEF (ORB) is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance its performance. ORB features are extracted for each frame and matched to those of the last known keyframe. To do that each key frame features have to be stored so that it can be compared to the incoming key frames using a 'bag-of-features' approach. When a key frame is found, local mapping can be computed so that the point cloud updates through triangulation. </p>

## Benchmarking
<p align="justify">  After the results, a comparison with a set file with the ground truth can be used, so as to benchmark the algorithm that we are using to real life data.</p>

A set of benchmarking database can be found on this link to the RGB-D SLAM Dataset and Benchmark: https://cvg.cit.tum.de/data/datasets/rgbd-dataset

## Camera features
<p align="justify">The camera intrinsic and extrinsic matrix has to be provided so as to ensure the proper calibration of the camera. This ensures that the estimated locations behave as expected.</p>

# Contents
<p align="justify">This repository contains the code necessary to run this algorithm in python. Under the folder src we can find all the code and its dependencies, while on the benchmark folder we can find the media that was used in the report.</p>

## Installation
<p align="justify">The dependencies necessary to properly run the code included are:</p>


* OpenCV
```sh
pip install opencv-python
```
* PyGame
```sh
pip install pygame
```
* NumPy
```sh
pip install numpy
```
* Skimage
```sh
pip install scikit-image
```
* Pangolin
  * [Installation Guide](https://github.com/uoip/pangolin)
* G2o
  * [Installation Guide](https://github.com/uoip/g2opy)


<p align="justify"> The dependencies Pangolin and G2o are used for the 3D representation, Pygame as a window renderer, Numpy as an array manager and OpenCV for image processing.</p>

## Usage
<p align="justify"> The file that should be run to recreate the behaviour showed on the report is the file main.py. This file calls to its dependencies to perform the algorithm. The script must be invoked with a mp4 video as an argument that will be the object of analysis. An usage example is</p>

```sh
python3 slam.py prueba.mp4
```
<p align="justify"> Camera and CameraFrame classes are the responsible of the camera calibration and its proper tracking along the whole video. Match_frames ensures that the proper points are matched to the keyframes, printing by console the number of point matches found from one keyframe to the next. Descriptor keeps track of the points and the mesh production. Display makes the 2D representations possible, the 3D one is handled by Descriptor as it already has the point information. Finally, Triangulation, as its name describes, is responsible to compute the 3D points themselves given the relative poses.</p>