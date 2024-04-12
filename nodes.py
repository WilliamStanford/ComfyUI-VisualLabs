
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}


def register_node(identifier: str, display_name: str):
    def decorator(cls):
        NODE_CLASS_MAPPINGS[identifier] = cls
        NODE_DISPLAY_NAME_MAPPINGS[identifier] = display_name

        return cls

    return decorator

@register_node("FloatArrayToPointString", "Point String from float array")
class _:
    CATEGORY = "visuallabs"
    INPUT_TYPES = lambda: {
        "required": {
            "float_array": ("FLOAT", {"array": True}),
        },

    }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("point_string",)
    FUNCTION = "format_float_array"


    def format_float_array(float_array):

        if float_array is None:
            raise ValueError("Float array must be provided.")

        # Convert a single float into a one-element array
        if not isinstance(float_array, np.ndarray):
            float_array = np.array([float_array])

        
        return ", ".join(f"{i}: ({x:.2f})" for i, x in enumerate(float_array))
