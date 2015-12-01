# Michaelson-Interferometer-Autopilot
A project to automate the Michaelson Interferometer experiment through computer vision.

One very frustating part of the experiment is to stare at the bright rings and count the fringes one by one.
The main goal of this project is to transfer this menial job to the computer.

General Usage scenario.
A continuous video could be taken of the fringes as they are expanding. The total movement of the mirror will be noted down .The video is fed to the software that does the counting for you.

Assuming a general  N=60 fps camera and requirement of n=6 frames to resolve dark and bright fringe temporally, the setup would have an maximum counting speed of  N/n = 10 fringes per second. This is a tremendous improvement relative to manual counting.
