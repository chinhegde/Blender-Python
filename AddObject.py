bl_info = {
    "name": "Object Adder",
    "author": "Chinmayi",
    "version": (1,0),
    "blender": (4,0),
    "location": "View3d > Tool",
    "category": "Add Mesh"
    "warning": "",
    "wiki_url": "",
}




import bpy

class TestPanel(bpy.types.Panel):
    bl_label = "Test Panel"
    bl_idname = "PT_TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Test Panel"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "Sample", icon = 'EXPERIMENTAL')
        row.operator('mesh.primitive_cube_add')
        row.operator('mesh.primitive_uv_sphere_add')
        row.operator('object.text_add', icon = 'FILE_FONT')

class PanelA(bpy.types.Panel):
    bl_label = "PanelA"
    bl_idname = "PT_PanelA"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Panel A"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "This is Panel A", icon = 'FAKE_USER_ON')
        row.operator('mesh.primitive_cube_add')

class PanelB(bpy.types.Panel):
    bl_label = "PanelB"
    bl_idname = "PT_PanelB"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Panel B"
    
    def draw(self, context):
        layout = self.layout
        
        row = layout.row()
        row.label(text = "This is Panel B", icon = 'CUBE')

        
def register():
    bpy.utils.register_class(TestPanel)
    
def unregister():
    bpy.utils.unregister_class(TestPanel)
    
if __name__ == "__main__":
    register()