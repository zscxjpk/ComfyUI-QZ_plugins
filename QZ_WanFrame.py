import torch
from comfy.utils import logging  # 修正导入路径

# 设置日志
logger = logging.getLogger(__name__)

class QZ_WanFrame:
    """
    帧计算节点：接收三个整数输入，计算并输出 输入1 × 输入2 + 输入3 的结果
    """
    # 节点的类别，在ComfyUI界面中显示
    CATEGORY = "QZ/Frame"
    # 节点的显示名称
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("计算结果",)
    
    # 输入端口定义
    INPUT_IS_LIST = False
    INPUT_TYPES = lambda: {
        "required": {
            "输入视频帧单元": ("INT", {"default": 4, "min": 0, "max": 9999, "step": 1}),
            "帧倍数": ("INT", {"default": 13, "min": 1, "max": 999, "step": 1}),
            "帧添加数值": ("INT", {"default": 1, "min": 0, "max": 9999, "step": 1}),
        }
    }
    
    FUNCTION = "calculate"
    DISPLAY_NAME = "QZ 帧计算"

    def calculate(self, 输入视频帧单元, 帧倍数, 帧添加数值):
        """
        执行计算：输入视频帧单元 × 帧倍数 + 帧添加数值
        """
        try:
            # 执行计算
            result = 输入视频帧单元 * 帧倍数 + 帧添加数值
            logger.info(f"帧计算完成: {输入视频帧单元} × {帧倍数} + {帧添加数值} = {result}")
            return (result,)
        except Exception as e:
            logger.error(f"帧计算出错: {str(e)}")
            # 出错时返回0
            return (0,)

# 节点注册
NODE_CLASS_MAPPINGS = {
    "QZ_WanFrame": QZ_WanFrame
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "QZ_WanFrame": "QZ 帧计算"
}
    