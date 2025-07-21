from .presets_data import data, select_brief_by_name

class Bori_KontextPresets:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset": ([preset["name"] for preset in data.get("presets", [])],),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("Prompt",)
    FUNCTION = "get_preset"
    CATEGORY = "Bori Kontext Presets"

    def get_preset(self, preset):
        brief = "The Brief:"+ select_brief_by_name(preset)
        fullString = data.get("prefix") + '\n' + brief + '\n' + data.get("suffix")
        return (fullString,)
