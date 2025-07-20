# the purpose of this is litterally to just make a turnaround animation 
import bpy

class turnAround(bpy.types.Operator):
    bl_idname = "data.microwave"
    bl_label = "microwave it"
    bl_options = {'REGISTER',"UNDO"} # register give that little popup in the corner to change the values

    num_turns: bpy.props.IntProperty(name="amount of turns",min=0,soft_max=10)

    def execute(self, context):
        self.report(
            {'INFO'},"num"
            )
        return {'FINISHED'}
    
class VIEW3DturnaroundPanel(bpy.types.Panel):
    bl_idname = "VIEW3DturnarounDPanel"
    bl_label = "microwave"
    bl_category = "shortcuts"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"

    def draw(self, context):
        layout = self.layout
        layout.operator("data.microwave")
        
    
bpy.utils.register_class(turnAround)
bpy.utils.register_class(VIEW3DturnaroundPanel)

# bpy.utils.unregister_class(turnAround)
# bpy.utils.unregister_class(VIEW3DturnaroundPanel)