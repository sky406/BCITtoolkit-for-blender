from ..rigging import armaturePanel as ap
import bpy

class VIEW3D_PT_BCIT_rigging_panel(bpy.types.Panel):
    #labels
    bl_idname = "VIEW3D_PT_BCIT_rigging_panel"
    bl_label = "rigging panel"
    # placement
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_options = {"DEFAULT_CLOSED"}
    bl_category="BCIT tools"
    
    @classmethod
    def poll(cls, context):
        objtype = context.active_object.type
        return objtype == "ARMATURE"
    
    def draw(self, context):
        layout = self.layout
        layout.label("placeholder text")
        # layout.panel(ap.VIEW3D_PT_BCIT_armature_panel.bl_idname)

subclasses = [ap.VIEW3D_PT_BCIT_armature_panel]
def register():
    bpy.utils.register_class(VIEW3D_PT_BCIT_rigging_panel)
    for i in subclasses:
        i.bl_parent_id = "VIEW3D_PT_BCIT_rigging_panel"
        bpy.utils.register_class(i)
    
    print("rig active")

def unregister():
    for i in subclasses: 
        bpy.utils.unregister_class(i)
    bpy.utils.unregister_class(VIEW3D_PT_BCIT_rigging_panel)
    print("rig innactive")