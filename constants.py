"""
AutoCAD COM API 类型定义和枚举常量
"""

from typing import List

# 类型别名
Point3D = List[float]  # [x, y, z]
Point2D = List[float]  # [x, y]
Vector3D = List[float]  # [x, y, z]
Vector2D = List[float]  # [x, y]

# ============================================================================
# 枚举常量定义（基于AutoCAD COM API）
# ============================================================================

class AcWindowState:
    """窗口状态枚举"""
    acNorm = 0    # 正常窗口
    acMin = 1     # 最小化
    acMax = 2     # 最大化

class AcZoomScaleType:
    """缩放比例类型枚举"""
    acZoomScaledAbsolute = 0       # 绝对比例
    acZoomScaledRelative = 1       # 相对比例
    acZoomScaledRelativePSpace = 2 # 相对于图纸空间

class AcActiveSpace:
    """活动空间枚举"""
    acModelSpace = 1      # 模型空间
    acPaperSpace = 2      # 图纸空间

class AcRegenType:
    """重生成类型枚举"""
    acActiveViewport = 0  # 仅活动视口
    acAllViewports = 1    # 所有视口

class AcPatternType:
    """填充图案类型枚举"""
    acHatchPatternTypePreDefined = 0    # 预定义图案
    acHatchPatternTypeUserDefined = 1   # 用户定义图案
    acHatchPatternTypeCustomDefined = 2 # 自定义图案

class AcAttributeMode:
    """属性模式枚举"""
    acAttributeModeNormal = 0      # 正常模式
    acAttributeModeInvisible = 1   # 不可见
    acAttributeModeConstant = 2    # 常量
    acAttributeModeVerify = 4      # 验证
    acAttributeModePreset = 8      # 预置

class AcAngleUnits:
    """角度单位枚举"""
    acDegrees = 0          # 度
    acDegreeMinuteSeconds = 1  # 度分秒
    acGrads = 2            # 百分度
    acRadians = 3          # 弧度
    acSurveyorUnits = 4    # 测量单位

class AcUnits:
    """线性单位枚举"""
    acDefaultUnits = -1    # 默认单位
    acScientific = 1       # 科学计数法
    acDecimal = 2          # 十进制
    acEngineering = 3      # 工程单位
    acArchitectural = 4    # 建筑单位
    acFractional = 5       # 分数单位

class AcCoordinateSystem:
    """坐标系统枚举"""
    acWorld = 0            # 世界坐标系 (WCS)
    acUCS = 1              # 用户坐标系
    acDisplayDCS = 2       # 显示坐标系
    acPaperSpaceDCS = 3    # 图纸空间DCS
    acOCS = 4              # 对象坐标系

# InitializeUserInput 位标志
class AcInputFlags:
    """用户输入初始化标志"""
    ACRX_NULL = 0          # 无限制
    ACRX_NONULL = 1        # 不允许空输入
    ACRX_NOZERO = 2        # 不允许零值
    ACRX_NONEG = 4         # 不允许负值
    ACRX_NOLIM = 8         # 不检查图形界限
    ACRX_DASH = 32         # 使用虚线拖引线
    ACRX_2D = 64           # 忽略Z坐标
    ACRX_3D = 128          # 强制3D坐标

    