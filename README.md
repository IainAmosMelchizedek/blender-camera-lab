# blender-camera-lab

A beginner-friendly Blender 4.0 Python lab focused on camera control, lens configuration,
constraints, and orbital animation using only scripting.

## Requirements
- Blender 4.0+ (tested on 4.0.2)

## How to Run a Script
1. Open Blender
2. Go to the **Scripting** workspace
3. Open a script from the `scripts/` folder
4. Click **Run Script**
5. Optional: Window → Toggle System Console (Windows) to see print output

## Scripts
- 01_camera_step1_basics.py  
  Finds Camera, Cube, Light. Positions camera and sets it active.

- 02_camera_step2_lens_28mm.py  
  Changes camera focal length to 28mm.

- 03_camera_step3_trackto_cube.py  
  Adds a TRACK_TO constraint so the camera always faces the cube.

- 04_camera_step4_orbit_circle.py  
  Animates the camera orbiting around the cube over 120 frames.

## Philosophy
This project demonstrates how scene control can be fully automated and reproducible
using Python rather than manual UI interaction.

