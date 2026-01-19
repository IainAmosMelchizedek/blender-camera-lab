import bpy

print("=== CAMERA_STEP2 ===")

scene = bpy.context.scene
cam = scene.camera

if cam is None:
    print("ERROR: No active camera found.")
else:
    cam_data = cam.data
    
    # Read current focal length
    current_lens = cam_data.lens
    print("Current focal length (mm):", current_lens)
    
    # Change focal length
    new_lens = 28.0
    cam_data.lens = new_lens
    
    print("New focal length set to (mm):", cam_data.lens)

print("=== DONE ===")
