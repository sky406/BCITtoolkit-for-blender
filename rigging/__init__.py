from ..rigging import armaturePanel as ap
import bpy
class VIEW3D_PT_BCIT_rigging_panel(bpy.types.Panel):
    #labels
    bl_idname = "VIEW3D_PT_BCIT_rigging_panel"
    bl_label = "rig tools"
    # placement
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    bl_options = {"DEFAULT_CLOSED"}
    bl_category="BCIT tools"

    def poll(cls,context):
        pass
        # return(context.selection_objects == bpy.types.Armature)
    def draw(self, context):
        print(bpy.context.selected_objects)
        print(bpy.context.active_object)
        print(context.selected_objects)
        layout = self.layout
        # layout.panel(ap.VIEW3D_PT_BCIT_armature_panel.bl_idname)

subclasses = [ap.VIEW3D_PT_BCIT_armature_panel]
def register():
    for i in subclasses:
        bpy.utils.register_class(i)
    bpy.utils.register_class(VIEW3D_PT_BCIT_rigging_panel)
    print("rig active")

def unregister():
    for i in subclasses: 
        bpy.utils.unregister_class(i)
    bpy.utils.unregister_class(VIEW3D_PT_BCIT_rigging_panel)
    print("rig innactive")