"""
AutoCAD COM API 类型安全的管理类 - 主入口点
此文件是重构后的入口点，将功能拆分到多个模块中以提高可维护性。

提供连接、绘图、管理控制等功能。

示例:
    with CadManager(visible=True) as cad:
        cad.add_line([0, 0, 0], [100, 100, 0])
        cad.add_circle([50, 50, 0], 25)
"""

# 动态导入，支持作为包或独立模块运行
if __package__:
    # 作为包的一部分运行，使用相对导入
    from .cad_manager import CadManager
    from .constants import *
    from .exceptions import *
    from .utils import *
else:
    # 作为独立模块运行，使用绝对导入
    from cad_manager import CadManager
    from constants import *
    from exceptions import *
    from utils import *

# 导出公共接口
__all__ = [
    'CadManager',
    'CadManagerError',
    'ConnectionError',
    'UserInputError',
    'DocumentError',
    'EntityError',
    # 枚举类
    'AcWindowState',
    'AcZoomScaleType',
    'AcActiveSpace',
    'AcRegenType',
    'AcPatternType',
    'AcAttributeMode',
    'AcAngleUnits',
    'AcUnits',
    'AcCoordinateSystem',
    'AcInputFlags',
    # 类型别名
    'Point3D',
    'Point2D',
    'Vector3D',
    'Vector2D',
    # 工具函数
    'degrees_to_radians',
    'radians_to_degrees',
    'create_point_2d',
    'create_point_3d',
    'create_vector_2d',
    'create_vector_3d',
]
