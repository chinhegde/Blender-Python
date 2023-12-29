import bpy, numpy as np
import addon_utils, pathlib, bmesh

bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete()

addon = 'io_import_images_as_planes'

loaded_default, loaded_state = addon_utils.check(addon)

if not loaded_state:
    addon_utils.enable(addon)


def import_image_as_plane(image_path):
    # check if the image exists on disk
    if image_path.exists():
        # import the image as a plane
        bpy.ops.import_image.to_plane(files=[{"name": str(image_path)}])


# create a variable that will hold the path to the target image
image_path = pathlib.Path.home() / "Kaedim" / "plate_inv.jpg"
print("image path", image_path)

import_image_as_plane(image_path)

plane = bpy.context.object

dimensions = plane.dimensions

width = dimensions.x
height = dimensions.y

mesh_object = bpy.context.active_object
    
material = mesh_object.data.materials[0]

if material.node_tree:
    
    image_node = None
    
    for node in material.node_tree.nodes:
        if node.type == 'TEX_IMAGE':
            image_node = node
            break

    if image_node:
        # Access image data
        image = image_node.image
        width, height = image.size
        pixel_values = np.empty((width, height,4), dtype=np.float32)
        
        image.pixels.foreach_get(pixel_values.ravel())

        pixel_values *= 255
        pixel_values = (pixel_values > 0).astype(np.uint8)

        imageNp = pixel_values.astype(np.uint8)

binary_image = imageNp[:, :, 0]

print("-----------",binary_image.max())

vertices=[]
edges=[]
faces=[]

max_height = 40

W = binary_image.shape[1]
H = binary_image.shape[0]

for Y in range(binary_image.shape[0]):
    for X in range(binary_image.shape[1]):
        pixelIntensity = imageNp[Y][X]
        Z = (pixelIntensity * max_height)
        vertices.append((X,Y,Z))


for X in range(binary_image.shape[1]-1):
    for Y in range(binary_image.shape[0]-1):
        face_v1= X+Y*W
        face_v2=X + 1 + Y* W
        face_v3=X + 1 + (Y+1) * W
        
        faces.append((face_v1,face_v2,face_v3))
        
        
        
new_mesh=bpy.data.meshes.new("new_mesh")
new_mesh.from_pydata(vertices,edges,faces)
new_mesh.update()

new_object = bpy.data.objects.new("new_object",new_mesh)
view_layer=bpy.context.view_layer
view_layer.active_layer_collection.collection.objects.link(new_object)