import bpy
import math
from mathutils import Vector

print("=== CAMERA_STEP4_ORBIT_CIRCLE ===")

scene = bpy.context.scene
cam = bpy.data.objects.get("Camera")
cube = bpy.data.objects.get("Cube")

if not cam or not cube:
    print("Missing Camera or Cube. cam:", bool(cam), "cube:", bool(cube))
    raise SystemExit

# Settings
start = 1
end = 120
radius = 6.0
height = 1.5

scene.frame_start = start
scene.frame_end = end

# Remove old LOCATION keyframes on the camera (clean slate)
if cam.animation_data and cam.animation_data.action:
    action = cam.animation_data.action
    for fc in list(action.fcurves):
        if fc.data_path == "location":
            action.fcurves.remove(fc)
    print("Removed old camera LOCATION keyframes.")

target = cube.matrix_world.translation

# Key 4 points for a clean circle (you can add more later if you want smoother without interpolation)
key_angles = [
    (start, 0.0),
    (start + (end-start)//4, math.pi/2),
    (start + (end-start)//2, math.pi),
    (start + 3*(end-start)//4, 3*math.pi/2),
    (end, 2*math.pi),
]

for frame, ang in key_angles:
    x = target.x + radius * math.cos(ang)
    y = target.y + radius * math.sin(ang)
    z = target.z + height

    scene.frame_set(frame)
    cam.location = Vector((x, y, z))
    cam.keyframe_insert(data_path="location", frame=frame)
    print(f"Keyed frame {frame}: location = {tuple(cam.location)}")

print("Frame range:", scene.frame_start, "to", scene.frame_end)
print("Active camera:", scene.camera.name if scene.camera else None)
print("Orbit radius:", radius, "| height:", height)
print("=== DONE ===")
