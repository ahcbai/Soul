import torch.nn as nn
from soul.neuron import base
import logging

def reset_net(net: nn.Module):
    """
    神经元膜内电压重置

    Args:
        net: 网络模型对象

    Returns:
        None
    """
    for m in net.modules():
        if hasattr(m, 'reset'):
            if not isinstance(m, base.MemoryModule):
                logging.warning(f'Trying to call `reset()` of {m}, which is not spikingjelly.activation_based.base'
                                f'.MemoryModule')
            m.reset()

def set_step_mode(net: nn.Module, step_mode: str):
    """
    设置推理模式

    Args:
        net: 网络模型对象
        step_mode: 推理模式

    Returns:
        None
    """
    for m in net.modules():
        if not isinstance(m, (base.StepModule)):
            logging.warning(f'Trying to set the step mode for {m}, which is not spikingjelly.activation_based'
                            f'.base.StepModule')
        m.step_mode = step_mode
