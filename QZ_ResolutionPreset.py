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
                    ["7680x4320 (8K横屏)", "5760x3240 (6K横屏)", "3840x2160 (4K横屏UHD)", "1920x1080 (横屏FHD)", "1280x720 (横屏HD)",
                     "960x544 (横屏)", "832x480 (横屏)", "768x432 (横屏)", 
                     "4320x7680 (8K竖屏)", "3240x5760 (6K竖屏)", "2160x3840 (4K竖屏UHD)", "1080x1920 (竖屏FHD)", "720x1280 (竖屏HD)", 
                     "544x960 (竖屏)", "480x832 (竖屏)", "432x768 (竖屏)",
                     "1024x1024 (1K)", "2048x2048 (2K)", "4096x4096 (4K)", "6144x6144 (6K)", "8192x8192 (8K)", 
                     "2048x1024 (2K_LatLong)", "4096x2048 (4K_LatLong)", "6144x3072 (6K_LatLong)", "8192x4096 (8K_LatLong)"],
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
            "7680x4320 (8K横屏)": (7680, 4320),
            "5760x3240 (6K横屏)": (5760, 3240),
            "3840x2160 (4K横屏UHD)": (3840, 2160),
            "1920x1080 (横屏FHD)": (1920, 1080),
            "1280x720 (横屏HD)": (1280, 720),
            "960x544 (横屏)": (960, 544),
            "832x480 (横屏)": (832, 480),
            "768x432 (横屏)": (768, 432),

            "4320x7680 (8K竖屏)": (4320, 7680),
            "3240x5760 (6K竖屏)": (3240, 5760),
            "2160x3840 (4K竖屏UHD)": (2160, 3840),
            "1080x1920 (竖屏FHD)": (1080, 1920),
            "720x1280 (竖屏HD)": (720, 1280),
            "544x960 (竖屏)": (544, 960),
            "480x832 (竖屏)": (480, 832),
            "432x768 (竖屏)": (432, 768),

            "1024x1024 (1K)": (1024, 1024),
            "2048x2048 (2K)": (2048, 2048),
            "4096x4096 (4K)": (4096, 4096),
            "6144x6144 (6K)": (6144, 6144),
            "8192x8192 (8K)": (8192, 8192),

            "2048x1024 (2K_LatLong)": (2048, 1024),
            "4096x2048 (4K_LatLong)": (4096, 2048),
            "6144x3072 (6K_LatLong)": (6144, 3072),
            "8192x4096 (8K_LatLong)": (8192, 4096),
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
