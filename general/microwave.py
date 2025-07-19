# the purpose of this is litterally to just make a turnaround animation 
import bpy

class VIEW3DturnarounDPanel(bpy.types.Panel):
    pass


class turnAround(bpy.types.Operator):
    bl_idname = "BCIT_microwaveAnimator"
    bl_label = "microwave it"

    def execute(self, context):
        pass