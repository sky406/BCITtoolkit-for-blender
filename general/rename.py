import bpy
class renameSettings(bpy.types.PropertyGroup):
    """ this is essentially just a way to store my settings for the rename tool
        its a bit jank so i'll come back to it one of these days
      """
    types = [
        ("MESH", "mesh", "objects lmao"),
        ("ARMATURE", "armature", "bones"),
        ("CURVE", "curve", "(●'◡'●)"),
        ("CAMERA", "camera", "its a camera my dude idk what to tell you"),
        ("LIGHT", "lights", "lighting"),
        
    ]
    

    prefix: bpy.props.StringProperty(name="prefix",description="its a prefix")
    suffix: bpy.props.StringProperty(name="suffix")
    replacement: bpy.props.StringProperty(name="replace")
    objType: bpy.props.EnumProperty(
        name="object type",
        items=types,
        description="Select the object type to rename"
    )

    # for the sake of preventing prefix suffix stacking
    lastPrefix: bpy.props.StringProperty(name="last prefix")
    lastSuffix: bpy.props.StringProperty(name="last suffix")

def renameByType():
    """ 
    type refers to blenders typing system. ie: "ARMATURE"
    this more or less stacks the new name on the type
    """
    # grab data from the scene
    renamesetting = bpy.context.scene.additional_props
    type = renamesetting.objType
    prefix = renamesetting.prefix
    suffix = renamesetting.suffix
    replaceWith = renamesetting.replacement
    lastprefix = renamesetting.lastPrefix
    lastsuffix = renamesetting.lastSuffix
    # 
    def fixName(name):
        fixedname = name
        if len(lastprefix)>0:
            fixedname = fixedname[len(lastprefix):]
    
        if len(lastsuffix)>0:
            fixedname = fixedname[:-len(lastsuffix)]
        return fixedname
    # 
    sceneobjects = bpy.context.editable_objects
    matchingTypes = []
    for obj in sceneobjects:
        if obj.type == type:matchingTypes.append(obj)

    for obj in matchingTypes:
        oldname = obj.name
        oldname = fixName(oldname)
        print(lastsuffix)
        newname = ""
        if prefix != "":
            newname+=f"{prefix}_"
            bpy.context.scene.additional_props.lastPrefix = f"{prefix}_"
        
        if replaceWith != "":
            newname+=replaceWith
        else:
            newname+=oldname
        
        if suffix != "":
            newname+=f"_{suffix}"
            bpy.context.scene.additional_props.lastSuffix = f"_{suffix}"
        obj.name = newname

class rename(bpy.types.Operator):
    bl_idname = "obj.rename"
    bl_label = "rename"
    bl_options = {"UNDO"}
    bl_description = "renames all objects of a particular type"
    
  
    def execute(self, context):
        # small note this refers to rename settings when it is registered
        # so this script only works when called within the quick tools panel
        # renamesetting = context.scene.additional_props
        # objtype = renamesetting.objType
        # prefix = renamesetting.prefix
        # suffix = renamesetting.suffix
        # replacement = renamesetting.replacement
        # print(f"{objtype}, {prefix}, {suffix}, {replacement}")
        renameByType()
        return {'FINISHED'}
    
 


    

