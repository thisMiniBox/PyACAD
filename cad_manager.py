"""
AutoCAD COM API 类型安全的管理类
提供连接、绘图、管理控制等功能。

示例:
    with CadManager(visible=True) as cad:
        cad.add_line([0, 0, 0], [100, 100, 0])
        cad.add_circle([50, 50, 0], 25)
"""

from connection import ConnectionMixin
from application import ApplicationMixin
from document import DocumentMixin
from entities import EntitiesMixin
from management import ManagementMixin
from user_input import UserInputMixin

class CadManager(
    ConnectionMixin,
    ApplicationMixin,
    DocumentMixin,
    EntitiesMixin,
    ManagementMixin,
    UserInputMixin
):
    """
    AutoCAD COM API 类型安全的管理类

    提供连接管理、文档操作、实体创建、图层控制等功能。
    使用类型注解确保代码安全性。
    """
    pass