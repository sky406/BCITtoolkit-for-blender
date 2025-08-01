import bpy

class VIEW3D_PT_BCIT_armature_panel(bpy.types.Panel):
    # labels 
    bl_idname = "VIEW3D_PT_BCIT_armature_panel"
    bl_label = "armature quickPanel"
    # placement 
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"
    # bl_options = {"DEFAULT_CLOSED"}
    
    @classmethod
    def poll(cls, context):
        objtype = context.active_object.type
        return objtype == "ARMATURE"

    def draw(self, context):
        layout = self.layout
        arm = context.object.data
        # axes row
        row = layout.row(align=True)
        row.prop(arm,"show_axes",text="show axes")
        row.prop(arm,"axes_position",text="position")
        # display type
        row = layout.row(align=False)
        row.prop(arm,"display_type",text="shape")
# TODO find and add some useful amature shorcuts to put in this
