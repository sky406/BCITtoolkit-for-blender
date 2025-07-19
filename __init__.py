import bpy 
from . import rigging as rig
bl_info = {
    "name":"BCIT tools",
    "blender":(4,4,0),
    "author":"wesley nworisa"
}

# class VIEW3D_PT_bcit_tool_panel(bpy.types.Panel):
#     # labels
#     bl_idname = "VIEW3D_PT_BCIT_tool_Panel"
#     bl_label = "BCIT tools"
#     # placement
#     bl_region_type = "UI"
#     bl_space_type = "VIEW_3D"
#     bl_options = {'DEFAULT_CLOSED'}

#     def draw(self,context):
#         layout = self.layout
classes = [rig.VIEW3D_PT_BCIT_rigging_panel]


def register():
    rig.register() 
    print("on")

def unregister():
    rig.unregister
    print("off")