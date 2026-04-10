"""
CAD管理器实体创建模块
"""

from typing import List, Optional, Any, Sequence
# 动态导入，支持作为包或独立模块运行
if __package__:
    # 作为包的一部分运行，使用相对导入
    from .constants import Point3D, Point2D, Vector3D, AcPatternType
    from .exceptions import ConnectionError
else:
    # 作为独立模块运行，使用绝对导入
    from constants import Point3D, Point2D, Vector3D, AcPatternType
    from exceptions import ConnectionError


class EntitiesMixin:
    """实体创建混合类"""

    def add_line(self, start_point: Point3D, end_point: Point3D) -> Any:
        """
        添加直线

        Args:
            start_point: 起点坐标 [x, y, z]
            end_point: 终点坐标 [x, y, z]

        Returns:
            创建的直线对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        start_variant = self._point_to_variant(start_point)
        end_variant = self._point_to_variant(end_point)

        return self.model_space.AddLine(start_variant, end_variant)

    def add_circle(self, center: Point3D, radius: float) -> Any:
        """
        添加圆

        Args:
            center: 圆心坐标 [x, y, z]
            radius: 半径

        Returns:
            创建的圆对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        center_variant = self._point_to_variant(center)

        return self.model_space.AddCircle(center_variant, float(radius))

    def add_arc(self, center: Point3D, radius: float,
                start_angle: float, end_angle: float) -> Any:
        """
        添加圆弧

        Args:
            center: 圆心坐标 [x, y, z]
            radius: 半径
            start_angle: 起始角度（弧度）
            end_angle: 终止角度（弧度）

        Returns:
            创建的圆弧对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        center_variant = self._point_to_variant(center)

        return self.model_space.AddArc(center_variant, float(radius),
                                      float(start_angle), float(end_angle))

    def add_text(self, text_string: str, insertion_point: Point3D,
                 height: float) -> Any:
        """
        添加单行文字

        Args:
            text_string: 文字内容
            insertion_point: 插入点 [x, y, z]
            height: 文字高度

        Returns:
            创建的文字对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        insertion_variant = self._point_to_variant(insertion_point)

        return self.model_space.AddText(str(text_string), insertion_variant, float(height))

    def add_mtext(self, insertion_point: Point3D, width: float,
                  text: str) -> Any:
        """
        添加多行文字

        Args:
            insertion_point: 插入点 [x, y, z]
            width: 文字框宽度
            text: 文字内容

        Returns:
            创建的多行文字对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        insertion_variant = self._point_to_variant(insertion_point)

        return self.model_space.AddMText(insertion_variant, float(width), str(text))

    def add_polyline(self, vertices: List[Point2D]) -> Any:
        """
        添加二维多段线

        Args:
            vertices: 顶点列表 [[x1, y1], [x2, y2], ...]

        Returns:
            创建的多段线对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式（二维点，Z坐标为0）
        vertices_variant = self._2d_points_to_variant(vertices)

        return self.model_space.AddPolyline(vertices_variant)

    def add_lw_polyline(self, vertices: List[Point2D]) -> Any:
        """
        添加轻量多段线（更高效）

        Args:
            vertices: 顶点列表 [[x1, y1], [x2, y2], ...]

        Returns:
            创建的轻量多段线对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式（二维点，Z坐标为0）
        vertices_variant = self._2d_points_to_variant(vertices)

        return self.model_space.AddLightWeightPolyline(vertices_variant)

    def add_3d_polyline(self, vertices: List[Point3D]) -> Any:
        """
        添加三维多段线

        Args:
            vertices: 顶点列表 [[x1, y1, z1], [x2, y2, z2], ...]

        Returns:
            创建的三维多段线对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 转换为VARIANT格式
        vertices_variant = self._points_to_variant(vertices)

        return self.model_space.Add3DPolyline(vertices_variant)

    def add_spline(self, fit_points: List[Point3D],
                   start_tangent: Optional[Vector3D] = None,
                   end_tangent: Optional[Vector3D] = None) -> Any:
        """
        添加样条曲线

        Args:
            fit_points: 拟合点列表
            start_tangent: 起点切向向量（可选）
            end_tangent: 终点切向向量（可选）

        Returns:
            创建的样条曲线对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        # 设置默认切向向量
        if start_tangent is None:
            start_tangent = [1.0, 0.0, 0.0]
        if end_tangent is None:
            end_tangent = [1.0, 0.0, 0.0]

        # 转换为VARIANT格式
        fit_points_variant = self._points_to_variant(fit_points)
        start_tangent_variant = self._point_to_variant(start_tangent)
        end_tangent_variant = self._point_to_variant(end_tangent)

        return self.model_space.AddSpline(fit_points_variant, start_tangent_variant, end_tangent_variant)

    def add_hatch(self, pattern_type: int, pattern_name: str,
                  associativity: bool = True) -> Any:
        """
        添加图案填充

        Args:
            pattern_type: 图案类型 (AcPatternType)
            pattern_name: 图案名称
            associativity: 是否关联填充

        Returns:
            创建的填充对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.model_space.AddHatch(pattern_type, pattern_name, associativity)

    def add_dim_aligned(self, ext_line1_point: Point3D,
                        ext_line2_point: Point3D,
                        text_position: Point3D) -> Any:
        """
        添加对齐标注

        Args:
            ext_line1_point: 第一条延伸线起点
            ext_line2_point: 第二条延伸线起点
            text_position: 文字位置

        Returns:
            创建的对齐标注对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.model_space.AddDimAligned(ext_line1_point, ext_line2_point, text_position)

    def add_dim_radial(self, center: Point3D, chord_point: Point3D,
                       leader_length: float) -> Any:
        """
        添加半径标注

        Args:
            center: 圆心
            chord_point: 弦点
            leader_length: 引线长度

        Returns:
            创建的半径标注对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.model_space.AddDimRadial(center, chord_point, leader_length)

    def add_block_reference(self, insertion_point: Point3D, block_name: str,
                            x_scale: float = 1.0, y_scale: float = 1.0,
                            z_scale: float = 1.0, rotation: float = 0.0) -> Any:
        """
        插入块参照

        Args:
            insertion_point: 插入点
            block_name: 块名称
            x_scale: X方向比例
            y_scale: Y方向比例
            z_scale: Z方向比例
            rotation: 旋转角度（弧度）

        Returns:
            创建的块参照对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.model_space.InsertBlock(insertion_point, block_name,
                                           x_scale, y_scale, z_scale, rotation)
    