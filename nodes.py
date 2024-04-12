
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
            "required": { "float_array" : ("STRING", {}) },
        }
    }
    RETURN_TYPES = ("STRING", {"default": "0:(0.0),\n7:(1.0),\n15:(0.0)\n", "multiline": True})
    RETURN_NAMES = ("point_string",)
    FUNCTION = "format_float_array"


    def format_float_array(float_array):
      return ", ".join(f"{i}: ({x:.2f})" for i, x in enumerate(float_array))
