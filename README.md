# Robotic-Vision-SLAM
This project is based on the information and codes provided by Matlab on the topic of vSLAM with a single camera and the contributions of Akbonline for a python implementation of said method.
<p align="center">
  <img src="https://github.com/vmr48-ua/Robotic-Vision-SLAM/assets/78732677/920d9540-620f-4d8f-8cfc-6f25a30bb8ee" alt="Live feature and velocity extraction"/>
</p>

## Algorithm sketch
<div align="justify">
To implement a visual Simultaneous Localization And Mapping (vSLAM) workflow, the first step is importing a series of images into a temporary folder. The mapping process is then initialized by grounding a frame as a reference and comparing it to the next so that motion can be tracked. We'll call 'key frames' to each pair of frames whose information has sufficient visual change to ensure proper tracking.
</div>

<div align="justify">
We will have to plot two different things, the 2D videoframes with the features marked and a 3D representation of said 2D frames where the camera location is induced by triangulation. The initial pose and placement can be derived from the first keyframes, and the features of the posterior frames get compared to those of the first to induce camera location.
</div>

<div align="justify">
What we call Oriented FAST and rotated BRIEF (ORB) is basically a fusion of FAST keypoint detector and BRIEF descriptor with many modifications to enhance its performance. ORB features are extracted for each frame and matched to those of the last known keyframe. To do that each key frame features have to be stored so that it can be compared to the incoming key frames using a 'bag-of-features' approach. When a key frame is found, local mapping can be computed so that the point cloud updates through triangulation. 
</div>

## Benchmarking
<div align="justify">
  After the results, a comparison with a set file with the ground truth can be used, so as to benchmark the algorithm that we are using to real life data.
</div>

<div align="justify">
  A set of benchmarking database can be found on this link to the RGB-D SLAM Dataset and Benchmark: https://cvg.cit.tum.de/data/datasets/rgbd-dataset
</div>

## Camera features
<div align="justify">
  The camera intrinsic and extrinsic matrix has to be provided so as to ensure the proper calibration of the camera. This ensures that the estimated locations behave as expected.
</div>

# Contents
<div align="justify">
  This repository contains the code necessary to run this algorithm in python. Its main ...
</div>
