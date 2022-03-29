# SLAM-REC-HV-version-1.0-test


![GitHub Brillante](https://github.com/MAB1144-Python/Document/blob/main/portada_Mesa%20de%20trabajo%201.jpg)

#### In this repository is the compilation of the tests carried out with the REC-HV v1.0 software, with online execution and low implementation cost, for the reconstruction of static scenes by points of high variability. In this, a dynamic object that performs a tour in the scene is detected, segmented and eliminated.

#### Rec-HV was developed in Python 3 and ROS with execution in ubuntu 18.06, it incorporates different tools, including ORB-SLAM, which is a visual odometry system. A 2D LIDAR (RPLIDAR A1) and a kinect (v1.0) were used as instruments. 

#### To show in depth the behavior of the software, a compilation of videos of the execution of the system in various scenarios is presented, and datasets of each scenario, software and different user guides are made available to the community of SLAM researchers. repository will be built by receiving contributions, opinions and new research on this area.

#### The datasets are composed of point clouds, lidar data sets, the position vector and the Euler angles for 400 recorded cycles.

#### To encourage the staggered development of this technology, researchers are encouraged to leave their opinions, doubts and contributions, in order to create spaces for the appropriation of this technology and strengthen SLAM research.

#### The respective code is in the rdslam folder, in this repository.

https://github.com/MAB1144-Python/SLAM-REC-HV-version-1.0-test/tree/main/rdslam

#### Installation guide for Rec-HV

https://github.com/MAB1144-Python/Installation_guide

### Control Scenario detection test.

#### The control scenario is made up of elements with materials that are easy to capture with the sensors. In the test, there was a robotic vehicle, which carried out the routes at a speed of 2.78m/s.

[![Alt text](https://img.youtube.com/vi/WSVlEiB-iQM/0.jpg)](https://youtu.be/WSVlEiB-iQM)

#### test dataset link 1.

https://drive.google.com/file/d/1kIZeFtes6nw38msn9hPmzpdYuX5q9MrD/view?usp=sharing

#### test dataset link 2.

https://drive.google.com/file/d/1_bv6Oza35ynK-kPxmFh8rpoXYACJWE3h/view?usp=sharing

### Reconstruction test in real environments

#### Tests were carried out in different scenarios to evaluate the behavior of the software. The dynamic object was a person who crosses the scene, for each scenario the download link of the dataset and a video of the test are left.

![GitHub Brillante](https://github.com/MAB1144-Python/Document/blob/main/escenas%20todas_Mesa%20de%20trabajo%201.jpg)

### Reconstruction test in scenario A.

#### In this scenario, the background is perpendicular to the X axis of the sensors, it has non-reflective materials such as glass, which generates areas of loss of points.

[![Alt text](https://img.youtube.com/vi/bhjiSwBkPpA/0.jpg)](https://youtu.be/bhjiSwBkPpA)

#### test dataset link.

https://drive.google.com/file/d/1adMnJOL9Mdg8f47oQOM6eJiNjsG4Oaz-/view?usp=sharing

### Reconstruction test in scenario B.

#### In this scenario the background is not perpendicular to the X axis of the sensors, it has non-reflective materials and an open space area, with loss of points.

[![Alt text](https://img.youtube.com/vi/ByWTqAcy7pA/0.jpg)](https://youtu.be/ByWTqAcy7pA)

#### test dataset link.

https://drive.google.com/file/d/1YQGNnzR4fdt5R0DwQj0SoEE3H3iAaJsN/view?usp=sharing

#### test with rotation dataset link.

https://drive.google.com/file/d/150U5IJcXCkcaLZ8_DHJN4835LZnpmpLy/view?usp=sharing

### Reconstruction test in scenario C.

#### In this scenario, the background is not perpendicular to the X axis of the sensors, it has reflective materials in the vast majority of the environment, however it presents an area of open space and a strip of high variability area, with loss of points.

[![Alt text](https://img.youtube.com/vi/s_6GpLxKSJA/0.jpg)](https://youtu.be/s_6GpLxKSJA)

#### test dataset link.

https://drive.google.com/file/d/1lQo5gUK9vnFUsofJQ0wd-T5kXOLzFR1t/view?usp=sharing

### Reconstruction test in scenario D.

#### In this scenario, the bottom is not perpendicular to the X axis of the sensors, it is characterized by having a depth that is over the limit of the Kinect's measurement capacity, it has a fairly complex distribution of static objects.

[![Alt text](https://img.youtube.com/vi/8NJJ-8n0R5I/0.jpg)](https://youtu.be/8NJJ-8n0R5I)

#### test dataset link.

https://drive.google.com/file/d/1_Ui49soAT_sTSj1ABUqnC2PhgicTUkQm/view?usp=sharing

### Reconstruction test in scenario E.

#### In this scenario, the background is not perpendicular to the X axis of the sensors, it is characterized by having a depth that is above the limit of the Kinect's measurement capacity, it has non-reflective materials and loss of points in some areas.

[![Alt text](https://img.youtube.com/vi/bm_InupCFsA/0.jpg)](https://youtu.be/bm_InupCFsA)

#### repositories of interest.
#### https://github.com/MAB1144-Python/Research-in-SLAM
#### https://github.com/MAB1144-Python/rotation-and-traslate-Point-Cloud-3D
#### https://github.com/MAB1144-Python/Machine-Learning-and-Deep-Learning

##### contact
##### https://www.linkedin.com/in/brayanandrumontenegroembus/
##### bamontenegro@unicauca.edu.co
