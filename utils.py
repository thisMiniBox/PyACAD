"""
CAD管理器工具函数
"""

from constants import Point2D, Point3D, Vector2D, Vector3D

def degrees_to_radians(degrees: float) -> float:
    """度转弧度"""
    return degrees * 3.141592653589793 / 180.0

def radians_to_degrees(radians: float) -> float:
    """弧度转度"""
    return radians * 180.0 / 3.141592653589793

def create_point_2d(x: float, y: float) -> Point2D:
    """创建二维点"""
    return [x, y]

def create_point_3d(x: float, y: float, z: float = 0.0) -> Point3D:
    """创建三维点"""
    return [x, y, z]

def create_vector_2d(x: float, y: float) -> Vector2D:
    """创建二维向量"""
    return [x, y]

def create_vector_3d(x: float, y: float, z: float = 0.0) -> Vector3D:
    """创建三维向量"""
    return [x, y, z]