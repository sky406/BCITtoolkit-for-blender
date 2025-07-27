import bpy
from .microwave import VIEW3DturnaroundPanel, turnAround
from .rename import rename,renameSettings
# the general panel is now the quick tools panel 

class VIEW3D_BCITquicktools(bpy.types.Panel):
    bl_idname = "VIEW3D_quicktools"
    bl_label = "quicktools"
    bl_category = "BCIT tools"
    bl_region_type = "UI"
    bl_space_type = "VIEW_3D"

    def draw(self, context):
        layout = self.layout
        row  = layout.row()
        row.operator(turnAround.bl_idname) 
        # new row 
        layout.separator()
        # renaing tool
        renamegroup = context.scene.additional_props
        
        column = layout.column()
        column.prop(renamegroup,"prefix")
        column.prop(renamegroup,"suffix")
        column.prop(renamegroup,"replacement")
        column.prop(renamegroup,"objType")
        column.operator(rename.bl_idname)



subclasses=[turnAround,renameSettings,rename]
propertygroups = [renameSettings]
def register():
    for subclass in subclasses:
        bpy.utils.register_class(subclass)

    # register the property group
    bpy.types.Scene.additional_props = bpy.props.PointerProperty(type=renameSettings)
    bpy.utils.register_class(VIEW3D_BCITquicktools)

def unregister():
    for subclass in subclasses:
        print(subclass)
        bpy.utils.unregister_class(subclass)
    del bpy.types.Scene.additional_props
    bpy.utils.unregister_class(VIEW3D_BCITquicktools)
    
