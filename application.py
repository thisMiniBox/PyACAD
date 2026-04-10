"""
CAD管理器应用程序控制模块
"""

from typing import Dict, Any
from constants import Point3D
from exceptions import ConnectionError

class ApplicationMixin:
    """应用程序控制混合类"""

    def get_application_info(self) -> Dict[str, str]:
        """
        获取AutoCAD应用程序信息

        Returns:
            包含应用程序信息的字典
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return {
            "name": self._acad.Name,
            "version": self._acad.Version,
            "full_name": self._acad.FullName,
            "path": self._acad.Path,
            "caption": self._acad.Caption,
            "locale_id": self._acad.LocaleId
        }

    def set_window_state(self, state: int) -> None:
        """
        设置AutoCAD窗口状态

        Args:
            state: 窗口状态 (AcWindowState.acNorm/acMin/acMax)
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.WindowState = state

    def set_window_position(self, left: float, top: float, width: float, height: float) -> None:
        """
        设置AutoCAD窗口位置和大小

        Args:
            left: 窗口左边缘位置（像素）
            top: 窗口上边缘位置（像素）
            width: 窗口宽度（像素）
            height: 窗口高度（像素）
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.Left = left
        self._acad.Top = top
        self._acad.Width = width
        self._acad.Height = height

    def zoom_all(self) -> None:
        """缩放显示全部图形"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.ZoomAll()

    def zoom_extents(self) -> None:
        """范围缩放"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.ZoomExtents()

    def zoom_window(self, min_point: Point3D, max_point: Point3D) -> None:
        """
        窗口缩放

        Args:
            min_point: 窗口左下角点
            max_point: 窗口右上角点
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.ZoomWindow(min_point, max_point)

    def zoom_center(self, center: Point3D, magnify: float) -> None:
        """
        中心缩放

        Args:
            center: 中心点
            magnify: 放大倍数
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._acad.ZoomCenter(center, magnify)