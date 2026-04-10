"""
CAD管理器连接管理模块
"""

import win32com.client
import pythoncom
from typing import Any, List
# 动态导入，支持作为包或独立模块运行
if __package__:
    # 作为包的一部分运行，使用相对导入
    from .constants import Point3D, Point2D
    from .exceptions import ConnectionError
else:
    # 作为独立模块运行，使用绝对导入
    from constants import Point3D, Point2D
    from exceptions import ConnectionError

class ConnectionMixin:
    """连接管理混合类"""

    def __init__(self, visible: bool = True, connect_existing: bool = True):
        """
        初始化CAD管理器

        Args:
            visible: 是否显示AutoCAD窗口
            connect_existing: 是否连接到正在运行的AutoCAD实例，否则创建新实例
        """
        self._visible = visible
        self._connect_existing = connect_existing
        self._acad: Any = None
        self._doc: Any = None
        self._connected = False

    def connect(self) -> None:
        """
        连接到AutoCAD应用程序

        Raises:
            ConnectionError: 连接失败时抛出
        """
        try:
            if self._connect_existing:
                # 尝试连接到正在运行的AutoCAD实例
                try:
                    self._acad = win32com.client.GetActiveObject("AutoCAD.Application")
                except:
                    # 没有正在运行的实例，创建新实例
                    self._acad = win32com.client.Dispatch("AutoCAD.Application")
            else:
                # 总是创建新实例
                self._acad = win32com.client.Dispatch("AutoCAD.Application")

            # 设置窗口可见性
            self._acad.Visible = self._visible

            # 获取活动文档
            self._doc = self._acad.ActiveDocument
            self._connected = True

            print(f"已连接到 AutoCAD {self._acad.Version}")

        except Exception as e:
            self._connected = False
            raise ConnectionError(f"无法连接到AutoCAD: {e}")

    def disconnect(self) -> None:
        """
        断开与AutoCAD的连接

        注意：此方法不会退出AutoCAD应用程序，仅释放连接引用。
        """
        if self._connected:
            # 释放对象引用
            self._doc = None
            self._acad = None
            self._connected = False
            print("已断开与AutoCAD的连接")

    def quit_application(self) -> None:
        """
        退出AutoCAD应用程序

        警告：这将关闭AutoCAD，所有未保存的文档可能会丢失。
        """
        if self._acad:
            try:
                self._acad.Quit()
                print("AutoCAD应用程序已退出")
            except Exception as e:
                print(f"退出AutoCAD时出错: {e}")
            finally:
                self._acad = None
                self._doc = None
                self._connected = False

    @property
    def is_connected(self) -> bool:
        """检查是否已连接到AutoCAD"""
        return self._connected

    @property
    def application(self) -> Any:
        """获取AutoCAD应用程序对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")
        return self._acad

    @property
    def document(self) -> Any:
        """获取当前活动文档对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")
        return self._doc

    @property
    def model_space(self) -> Any:
        """获取模型空间对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")
        return self._doc.ModelSpace

    @property
    def paper_space(self) -> Any:
        """获取图纸空间对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")
        return self._doc.PaperSpace

    @property
    def utility(self) -> Any:
        """获取实用工具对象"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")
        return self._doc.Utility

    # ============================================================================
    # 上下文管理器支持
    # ============================================================================

    def __enter__(self):
        """进入上下文时自动连接"""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时自动断开连接"""
        self.disconnect()

    # ============================================================================
    # 内部工具方法
    # ============================================================================

    def _point_to_variant(self, point: Point3D) -> Any:
        """
        将点坐标转换为AutoCAD COM API所需的VARIANT格式

        Args:
            point: 点坐标 [x, y, z]

        Returns:
            VARIANT包装的坐标数组
        """
        return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8,
                                      [float(point[0]), float(point[1]), float(point[2])])

    def _points_to_variant(self, points: List[Point3D]) -> Any:
        """
        将点列表转换为AutoCAD COM API所需的VARIANT格式

        Args:
            points: 点坐标列表 [[x1, y1, z1], [x2, y2, z2], ...]

        Returns:
            VARIANT包装的点数组
        """
        # 展平点列表
        flat_points = []
        for point in points:
            flat_points.extend([float(point[0]), float(point[1]), float(point[2])])
        return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, flat_points)

    def _2d_points_to_variant(self, points: List[Point2D]) -> Any:
        """
        将二维点列表转换为AutoCAD COM API所需的VARIANT格式

        Args:
            points: 二维点坐标列表 [[x1, y1], [x2, y2], ...]

        Returns:
            VARIANT包装的点数组（二维，Z坐标为0）
        """
        # 展平点列表，每个点添加Z坐标0
        flat_points = []
        for point in points:
            flat_points.extend([float(point[0]), float(point[1]), 0.0])
        return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, flat_points)