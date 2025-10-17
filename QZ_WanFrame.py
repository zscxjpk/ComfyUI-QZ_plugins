import torch
from comfy.utils import logging

logger = logging.getLogger(__name__)

class QZ_WanFrame:
    CATEGORY = "QZ/Frame"
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("计算结果",)
    
    INPUT_IS_LIST = False
    INPUT_TYPES = lambda: {
        "required": {
            "使用自定义帧数": ("BOOLEAN", {"default": False, "label_on": "启用", "label_off": "禁用"}),
            "输入视频帧单元": ("INT", {"default": 4, "min": 0, "max": 9999, "step": 1}),
            "帧倍数": ("INT", {"default": 13, "min": 1, "max": 999, "step": 1}),
            "帧添加数值": ("INT", {"default": 1, "min": 0, "max": 9999, "step": 1}),

            "自定义输入帧数": ("INT", {"default": 0, "min": 0, "max": 9999, "step": 1}),
        }
    }
    
    FUNCTION = "calculate"
    DISPLAY_NAME = "QZ wan帧计算"

    def calculate(self, 使用自定义帧数, 输入视频帧单元, 帧倍数, 帧添加数值, 自定义输入帧数):
        try:
            if 使用自定义帧数:
                result = 自定义输入帧数
                logger.info(f"使用自定义帧数: {result}")
            else:
                result = 输入视频帧单元 * 帧倍数 + 帧添加数值
                logger.info(f"帧计算完成: {输入视频帧单元} × {帧倍数} + {帧添加数值} = {result}")
            return (result,)
        except Exception as e:
            logger.error(f"帧计算出错: {str(e)}")
            return (0,)

NODE_CLASS_MAPPINGS = {
    "QZ_WanFrame": QZ_WanFrame
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QZ_WanFrame": "QZ wan帧计算"
}
