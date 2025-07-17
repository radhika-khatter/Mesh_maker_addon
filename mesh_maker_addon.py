bl_info={
    "name":"Mesh Maker Addon",
    "author":"Radhika Khatter",
    "version":(1,0),
    "blender":(3,0,0),
    "location":"View3D> Sidebar > Mesh Maker Tab",
    "description":"Addon to create and manage cubes",
    "category":"Object"
}
import bpy

class MESHMAKER(bpy.types.Panel):
    bl_label="Mesh maker Panel"
    bl_idname="MESHMAKER_PANEL"
    bl_space_type="VIEW_3D"
    bl_region_type="UI"
    bl_category="Mesh maker"

    def draw(self,context):
        layout=self.layout
        layout.label(text="enter number of cubes: ")
        layout.prop(context.scene,"cube_count")
        layout.operator("meshmaker.add_cubes")
        layout.operator("meshmaker.delete_selected")

class MESHMAKER_add_cube(bpy.types.Operator):
    bl_idname="meshmaker.add_cubes"
    bl_label="Create Cubes"
    bl_description="Create N cubes in a grid"

    def execute(self,context):
        N=context.scene.cube_count

        if N >50:
            self.report({'ERROR'},"the number is out of range")
            return {'CANCELLED'}
        
        spacing=2.0

        cube_collection=None

        if "GeneratedCubes" in bpy.data.collections:
            cube_collection=bpy.data.collections["GeneratedCubes"]

        else:
            cube_collection=bpy.data.collections.new("GeneratedCubes")
            bpy.context.scene.collection.children.link(cube_collection)
        existing_count=len(cube_collection.objects)

        for i in range(N):
            index=existing_count+i
            x=(index%5)*spacing
            y=(index//5) *spacing
            bpy.ops.mesh.primitive_cube_add(size=1, location=(x,y,0))
            new_cube=context.active_object
            cube_collection.objects.link(new_cube)
            if new_cube.name in bpy.context.scene.collection.objects:
                bpy.context.scene.collection.objects.unlink(new_cube)
        return {'FINISHED'}

class MESHMAKER_delete_selected(bpy.types.Operator):
    bl_idname="meshmaker.delete_selected"
    bl_label="Delete selected"
    bl_description="Delete all selected objects"

    def execute(self,context):
        selected_objects=context.selected_objects

        if not selected_objects:
            self.report({'WARNING'},"No objects selected")
            return {'CANCELLED'}
        
        for obj in selected_objects:
            bpy.data.objects.remove(obj,do_unlink=True)

        self.report({'INFO'},f"{len(selected_objects)} object(s) deleted")
        return{'FINISHED'}

def register():
    bpy.utils.register_class(MESHMAKER)
    bpy.utils.register_class(MESHMAKER_add_cube)
    bpy.utils.register_class(MESHMAKER_delete_selected)
    bpy.types.Scene.cube_count=bpy.props.IntProperty(
        name="Number of Cubes",
        description="enter the number of cubes to generate",
        default=1,
        min=1,
    )

def unregister():
    bpy.utils.unregister_class(MESHMAKER)
    bpy.utils.unregister_class(MESHMAKER_add_cube)
    bpy.utils.unregister_class(MESHMAKER_delete_selected)
    del bpy.types.Scene.cube_count

