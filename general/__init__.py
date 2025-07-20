import bpy
from .microwave import VIEW3DturnaroundPanel, turnAround
# note for self do i really need a gneral panel probabbly not 
subclasses=[turnAround,VIEW3DturnaroundPanel]
def register():
    for subclass in subclasses:
        bpy.utils.register_class(subclass)

def unregister():
    for subclass in subclasses:
        bpy.utils.unregister_class(subclass)
    
