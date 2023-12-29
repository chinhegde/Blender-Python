import bpy
import os, pathlib

bpy.ops.object.select_all(action='SELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))

# These can be passed from the previous script which creates the image
width = 935
height = 711

plane = bpy.context.active_object
plane.scale = (width/2, height/ 2, 1)

texture_path = pathlib.Path.home() / "Kaedim" / "plate_inv.jpg"

tex = bpy.data.textures.new(name="Texture", type="IMAGE")
img = bpy.data.images.load(str(texture_path))

tex.image = img
tex.extension = 'REPEAT'

displace_modifier = plane.modifiers.new(name="Displace", type='DISPLACE')
displace_modifier.texture = tex
displace_modifier.strength = 0.1  

bpy.ops.object.modifier_apply(modifier="Smooth")
bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.subdivide(number_cuts=50)

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='DESELECT')
bpy.ops.mesh.select_mode(type='EDGE')
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 20)})

bpy.ops.object.mode_set(mode='OBJECT')
bpy.ops.object.shade_smooth()

bpy.ops.object.mode_set(mode='EDIT')
bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.fill()

bpy.ops.object.mode_set(mode='OBJECT')