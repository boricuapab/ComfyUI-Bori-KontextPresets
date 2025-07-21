from .nodes.Bori_KontextPresets import *

NODE_CLASS_MAPPINGS = {
    # Add mappings here
    "Bori Kontext Presets": Bori_KontextPresets,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Bori Kontext Presets": "Bori Kontext Presets", 
}

print ("\033[38;5;224m")
print ("Bori Kontext Presets")
print ("\033[38;5;173m")
print ("Loaded")
print ("\033[0m")

WEB_DIRECTORY = "./web"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]