import bpy

print("=== CAMERA_STEP1 ===")
print("Blender version:", bpy.app.version_string)

scene = bpy.context.scene

cam = bpy.data.objects.get("Camera")
cube = bpy.data.objects.get("Cube")
light = bpy.data.objects.get("Light")

print("Active scene:", scene.name)
print("Found Camera:", bool(cam), "| name:", getattr(cam, "name", None))
print("Found Cube:", bool(cube), "| name:", getattr(cube, "name", None))
print("Found Light:", bool(light), "| name:", getattr(light, "name", None))

print("Active camera (scene.camera):", getattr(scene.camera, "name", None))

if cam and cube:
    # Put camera in front of cube and point it straight at the cube
    cam.location = (0.0, -6.0, 1.5)
    cam.rotation_euler = (1.3, 0.0, 0.0)  # a simple "looking down a bit" angle
    scene.camera = cam
    print("Moved camera to:", tuple(cam.location))
    print("Camera rotation (Euler):", tuple(cam.rotation_euler))

print("=== DONE ===")
