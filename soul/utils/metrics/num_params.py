def count_parameters(model, trainable=False):
    """
    统计参数量

    Args:
        model: 模型对象
        trainable: 是否只统计可训练参数

    Returns:
        参数量
    """
    if trainable:
        return sum(p.numel() for p in model.parameters() if p.requires_grad)
    return sum(p.numel() for p in model.parameters())