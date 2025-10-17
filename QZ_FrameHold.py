import torch
from comfy.utils import logging

# 设置日志
logger = logging.getLogger(__name__)

class QZ_FrameHold:
    """
    视频关键帧提取节点：从输入的视频帧序列中提取指定帧作为静态图像输出
    """
    # 节点类别
    CATEGORY = "QZ/Frame"
    # 输出类型及名称
    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("output",)
    
    # 输入端口定义
    INPUT_IS_LIST = False
    INPUT_TYPES = lambda: {
        "required": {
            "image": ("IMAGE",),  # 接收视频帧序列（通常来自Load Video节点）
            "提取帧索引": ("INT", {
                "default": 1,       # 默认提取第1帧
                "min": 1,           # 最小帧索引（1-based）
                "max": 9999,        # 最大帧索引限制
                "step": 1           # 步长为1
            }),
        }
    }
    
    FUNCTION = "extract_frame"
    DISPLAY_NAME = "QZ 帧提取"

    def extract_frame(self, image, 提取帧索引):
        """
        从视频帧序列中提取指定帧并输出
        
        参数:
            image: 视频帧序列张量，形状通常为 (帧数量, 高度, 宽度, 通道)
            提取帧索引: 要提取的帧编号（1-based）
        
        返回:
            提取的单帧图像张量，形状为 (1, 高度, 宽度, 通道)
        """
        try:
            # 视频帧序列通常是 (frame_count, h, w, c) 结构
            frame_count = image.shape[0]
            
            # 转换为0-based索引（用户输入1对应第0帧）
            zero_based_index = 提取帧索引 - 1
            
            # 检查索引有效性
            if zero_based_index < 0 or zero_based_index >= frame_count:
                error_msg = f"帧索引超出范围！有效范围: 1-{frame_count}，输入值: {提取帧索引}"
                logger.error(error_msg)
                # 索引无效时返回第一帧
                return (image[0:1, ...],)
            
            # 提取指定帧并保持维度（增加一个批次维度）
            selected_frame = image[zero_based_index:zero_based_index+1, ...]
            logger.info(f"成功提取第{提取帧索引}帧（0-based: {zero_based_index}）")
            return (selected_frame,)
            
        except Exception as e:
            logger.error(f"帧提取失败: {str(e)}")
            # 出错时返回空图像（实际场景中可根据需求调整）
            return (torch.zeros(1, 1, 1, 3, dtype=torch.float32),)

# 节点注册
NODE_CLASS_MAPPINGS = {
    "QZ_FrameHold": QZ_FrameHold
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QZ_FrameHold": "QZ 帧提取"
}