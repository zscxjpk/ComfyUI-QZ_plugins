Installation
节点安装：

cd ComfyUI/custom_nodes

git clone https://github.com/zscxjpk/ComfyUI-QZ_plugins.git

Let's start introducing the use of custom nodes:
让我们开始介绍自定义节点的使用：

QZ_ResolutionPreset:图像分辨率预设

![1](https://github.com/user-attachments/assets/680453aa-439f-4eed-b650-d58816ed92ba)

Commonly used, image zoom, mask zoom, video zoom.
常用的有图像缩放、蒙版缩放、视频缩放。

![2](https://github.com/user-attachments/assets/35c4ece3-33e4-4463-9c8a-7e596bf7b497)

It is possible to customise the input resolution, but be careful to tick Use Custom.
可以自定义输入分辨率，但请注意勾选“使用自定义”。

QZ_WanFrame:万相帧运算

<img width="2157" height="1212" alt="wechat_2025-10-17_173043_707" src="https://github.com/user-attachments/assets/4dd1e4da-6561-4a0e-b61c-4494e991be95" />

For the commonly used multiples of 4+1 in WAN, 4 can be left unchanged and only the frame multiplier needs to be modified. You can also select 'Enable' to customize the input frame rate.
针对wan常用的4的倍数+1，4可以不动只需要修改帧倍数就可以了。也可以勾选启用，自定义输入帧数。

QZ_FrameHold：视频关键帧提取

<img width="2430" height="1230" alt="wechat_2025-10-17_172059_547" src="https://github.com/user-attachments/assets/3ef88e71-fce3-492f-af66-0bed2f35b884" />

Extract keyframes from the video, customize the number of frames to be extracted, and directly obtain the corresponding static image.
提取视频中的关键帧，自定义输入想要提取的帧数，直接得到对应的静态图像。


联系作者：
B站：https://space.bilibili.com/412411578?spm_id_from=333.1007.0.0

C站：https://civitai.com/user/zscxjpk658/models
