import bpy

# new modifier class
class ExpressionModifier(bpy.types.FCurveModifiers):
        bl_idname = "FCurveExpressionModifier"
        bl_label = "FCurve Expression"
        bl_description = "Allows expression in F-curve modifier"
        bl_category = "FCurve"
        type = "EXPRESSION"
        icon = "SCRIPT"
        color = (0.0, 0.0, 0.0)
        priority = 0
        is_active = False
        is_enabled = False

        expression: bpy.props.StringProperty( #type: ignore
            name="Expression",
            description="Expression to be evaluated",
            default="",
            maxlen=1024,
        )

        def check(self, context):
            return True
        
        def update(self, context):
            pass

        def apply(self, context, evaluation_context):
            pass

        def apply_to_keyframes(self, context, evaluation_context, keyframe_points):
            pass

        def apply_to_fcurve(self, context, evaluation_context, fcurve):
            pass

        def draw(self, context, layout):
            pass