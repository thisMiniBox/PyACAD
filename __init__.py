"""
CAD管理器包 - 用于AutoCAD COM API编程的类型安全封装

此包提供对AutoCAD COM API的高级封装，支持连接管理、文档操作、
实体创建、图层控制、用户输入等功能。

主要类:
    CadManager - 主管理类

使用示例:
    >>> from CadManager import CadManager
    >>> with CadManager(visible=True) as cad:
    ...     cad.add_line([0, 0, 0], [100, 100, 0])
    ...     cad.add_circle([50, 50, 0], 25)
"""

from .cadManager import *

__version__ = "1.0.0"
__author__ = "AutoCAD COM API 封装项目"

# 简化的导出，通过CadManager.py处理详细导出
__all__ = [
    'CadManager',
    'CadManagerError',
    'ConnectionError',
    'UserInputError',
    'DocumentError',
    'EntityError',
]