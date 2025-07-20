# the purpose of this is litterally to just make a turnaround animation 
import bpy
from math import radians, degrees
class turnAround(bpy.types.Operator):
    bl_idname = "data.microwave"
    bl_label = "microwave it"
    bl_options = {'REGISTER',"UNDO"} # register give that little popup in the corner to change the values

    num_turns: bpy.props.IntProperty(name="amount of turns",min=0,soft_max=10)
    turn_direction: bpy.props.IntVectorProperty(name="turndirection",soft_min=-2,soft_max=2,default=(0,0,1))

    def execute(self, context):
        # self.report(
        #     {'INFO'},"num"
        #     )
        # get start and end frames
        start= context.scene.frame_start
        end = context.scene.frame_end
        # grab the active object
        active = context.active_object
        # set the starting rotation
        startFrame = active.keyframe_insert(data_path="rotation_euler",frame=start)

        # set the rotation
        self.report({'DEBUG'},f"new rotation {self.turn_direction[2]}")
        oldrotation = active.rotation_euler
        print(oldrotation)
        self.report({'DEBUG'},f"old rotation {oldrotation[0]} {oldrotation[1]} {oldrotation[2]}")
        newrotation = ( # rotation euler is in radians. a good thing to note
            radians(degrees(oldrotation[0])+self.turn_direction[0] * self.num_turns * 360),
            radians(degrees(oldrotation[1])+self.turn_direction[1] * self.num_turns * 360),
            radians(degrees(oldrotation[2])+self.turn_direction[2] * self.num_turns * 360),
        )

        active.rotation_euler = newrotation
        endframe=active.keyframe_insert(data_path="rotation_euler",frame=end)
        
        # set all frames to linear keyframes
        action = active.animation_data.action
        for frame in action.fcurves:
            for f in frame.keyframe_points:
                f.interpolation = 'LINEAR'
        return {'FINISHED'}
    
class VIEW3DturnaroundPanel(bpy.types.Panel):
    bl_idname = "VIEW3DturnarounDPanel"
    bl_label = "microwave"
    bl_category = "shortcuts"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"

    @classmethod
    def poll(cls, context):
        return (context.active_object is not None)

    def draw(self, context):
        layout = self.layout
        layout.operator("data.microwave")
    
        
# for testing purposes
bpy.utils.register_class(turnAround)
bpy.utils.register_class(VIEW3DturnaroundPanel)

# bpy.utils.unregister_class(turnAround)
# bpy.utils.unregister_class(VIEW3DturnaroundPanel)