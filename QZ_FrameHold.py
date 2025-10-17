import torch
from comfy.utils import logging


logger = logging.getLogger(__name__)

class QZ_FrameHold:
    CATEGORY = "QZ/Frame"

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output",)

    INPUT_IS_LIST = False
    INPUT_TYPES = lambda: {
        "required": {
            "image": ("IMAGE",),  
            "提取帧索引": ("INT", {
                "default": 1,     
                "min": 1,         
                "max": 9999,     
                "step": 1        
            }),
        }
    }
    
    FUNCTION = "extract_frame"
    DISPLAY_NAME = "QZ 帧提取"

    def extract_frame(self, image, 提取帧索引):

        try:
            frame_count = image.shape[0]            
            zero_based_index = 提取帧索引 - 1
            
            if zero_based_index < 0 or zero_based_index >= frame_count:
                error_msg = f"帧索引超出范围！有效范围: 1-{frame_count}，输入值: {提取帧索引}"
                logger.error(error_msg)

                return (image[0:1, ...],)
            
            selected_frame = image[zero_based_index:zero_based_index+1, ...]
            logger.info(f"成功提取第{提取帧索引}帧（0-based: {zero_based_index}）")
            return (selected_frame,)
            
        except Exception as e:
            logger.error(f"帧提取失败: {str(e)}")
            return (torch.zeros(1, 1, 1, 3, dtype=torch.float32),)


NODE_CLASS_MAPPINGS = {
    "QZ_FrameHold": QZ_FrameHold
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QZ_FrameHold": "QZ 帧提取"
}
