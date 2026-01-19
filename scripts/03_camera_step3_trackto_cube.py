import bpy

print("=== CAMERA_STEP3_TRACKTO ===")

scene = bpy.context.scene
cam = bpy.data.objects.get("Camera")
cube = bpy.data.objects.get("Cube")

print("Found Camera:", bool(cam), "| name:", getattr(cam, "name", None))
print("Found Cube:", bool(cube), "| name:", getattr(cube, "name", None))

if not cam or not cube:
    print("ERROR: Camera or Cube not found. Aborting.")
else:
    # Make camera the active scene camera
    scene.camera = cam

    # Remove old Track To constraints (so we don't stack them)
    removed = 0
    for c in list(cam.constraints):
        if c.type == 'TRACK_TO':
            cam.constraints.remove(c)
            removed += 1
    print("Removed old TRACK_TO constraints:", removed)

    # Add a new Track To constraint
    con = cam.constraints.new(type='TRACK_TO')
    con.name = "TRACK_CUBE"
    con.target = cube

    # These two settings matter a lot:
    # - TRACK_NEGATIVE_Z means camera "looks" down its -Z axis (Blender camera forward)
    # - UP_Y keeps the camera upright using its Y axis as "up"
    con.track_axis = 'TRACK_NEGATIVE_Z'
    con.up_axis = 'UP_Y'

    print("Added constraint:", con.name)
    print("Constraint target:", con.target.name)
    print("track_axis:", con.track_axis, "| up_axis:", con.up_axis)

print("=== DONE ===")
