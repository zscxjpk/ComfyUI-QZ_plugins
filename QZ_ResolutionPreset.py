import os
from nodes import SaveImage

class QZ_ResolutionPreset:
    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "preset_size": (
                    ["1920x1080 (横屏FHD)", "1280x720 (横屏HD)", "960x544 (横屏)", "832x480 (横屏)", 
                     "1080x1920 (竖屏FHD)", "720x1280 (竖屏HD)", "544x960 (竖屏)", "480x832 (竖屏)", 
                     "1024x1024 (1K)", "2048x2048 (2K)"],
                    {"default": "1920x1080 (横屏FHD)"}
                ),
            },
        }
    
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("width", "height")
    FUNCTION = "get_size"

    def get_size(self, preset_size):
        # 预设尺寸映射
        size_map = {
            "1920x1080 (横屏FHD)": (1920, 1080),
            "1280x720 (横屏HD)": (1280, 720),
            "960x544 (横屏)": (960, 544),
            "832x480 (横屏)": (832, 480),
            "1080x1920 (竖屏FHD)": (1080, 1920),
            "720x1280 (竖屏HD)": (720, 1280),
            "544x960 (竖屏)": (544, 960),
            "480x832 (竖屏)": (480, 832),
            "1024x1024 (1K)": (1024, 1024),
            "2048x2048 (2K)": (2048, 2048),
        }
        
        width, height = size_map[preset_size]
        return (width, height)

# 节点注册
NODE_CLASS_MAPPINGS = {
    "QZ_ResolutionPreset": QZ_ResolutionPreset,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QZ_ResolutionPreset": "QZ_分辨率预设",
}
