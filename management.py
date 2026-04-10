"""
CAD管理器管理控制模块（图层、线型、文字样式等）
"""

from typing import Optional, List, Any
from constants import Point3D
from exceptions import ConnectionError

class ManagementMixin:
    """管理控制混合类"""

    # 图层管理
    # ----------------------------------------------------------------------------

    def create_layer(self, layer_name: str, color: Optional[int] = None,
                     line_type: Optional[str] = None) -> Any:
        """
        创建新图层

        Args:
            layer_name: 图层名称
            color: 颜色索引（可选）
            line_type: 线型名称（可选）

        Returns:
            创建的图层对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        layers = self._doc.Layers
        layer = layers.Add(layer_name)

        if color is not None:
            layer.Color = color
        if line_type is not None:
            layer.Linetype = line_type

        return layer

    def get_layer(self, layer_name: str) -> Any:
        """
        获取指定图层

        Args:
            layer_name: 图层名称

        Returns:
            图层对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self._doc.Layers.Item(layer_name)

    def get_all_layers(self) -> List[str]:
        """
        获取所有图层名称

        Returns:
            图层名称列表
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        layers = self._doc.Layers
        return [layers.Item(i).Name for i in range(layers.Count)]

    def set_active_layer(self, layer_name: str) -> None:
        """
        设置当前活动图层

        Args:
            layer_name: 图层名称
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.ActiveLayer = self._doc.Layers.Item(layer_name)

    def delete_layer(self, layer_name: str) -> None:
        """
        删除图层

        Args:
            layer_name: 图层名称

        Raises:
            ValueError: 无法删除当前图层或0图层时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        layer = self._doc.Layers.Item(layer_name)
        layer.Delete()

    # 线型管理
    # ----------------------------------------------------------------------------

    def load_line_type(self, line_type_name: str, file_name: str) -> None:
        """
        加载线型

        Args:
            line_type_name: 线型名称
            file_name: 线型文件路径
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.Linetypes.Load(line_type_name, file_name)

    def set_active_line_type(self, line_type_name: str) -> None:
        """
        设置当前活动线型

        Args:
            line_type_name: 线型名称
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.ActiveLinetype = line_type_name

    # 文字样式管理
    # ----------------------------------------------------------------------------

    def create_text_style(self, style_name: str, font_name: str,
                          height: float = 0.0, width_factor: float = 1.0,
                          oblique_angle: float = 0.0) -> Any:
        """
        创建文字样式

        Args:
            style_name: 样式名称
            font_name: 字体名称
            height: 文字高度（0表示不固定）
            width_factor: 宽度因子
            oblique_angle: 倾斜角度（弧度）

        Returns:
            创建的文字样式对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        text_styles = self._doc.TextStyles
        style = text_styles.Add(style_name)
        style.fontFile = font_name
        style.Height = height
        style.Width = width_factor
        style.ObliqueAngle = oblique_angle

        return style

    def set_active_text_style(self, style_name: str) -> None:
        """
        设置当前活动文字样式

        Args:
            style_name: 文字样式名称
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.ActiveTextStyle = style_name

    # 标注样式管理
    # ----------------------------------------------------------------------------

    def set_active_dim_style(self, style_name: str) -> None:
        """
        设置当前活动标注样式

        Args:
            style_name: 标注样式名称
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.ActiveDimStyle = style_name

    # 选择集管理
    # ----------------------------------------------------------------------------

    def create_selection_set(self, name: str) -> Any:
        """
        创建选择集

        Args:
            name: 选择集名称

        Returns:
            创建的选择集对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        selection_sets = self._doc.SelectionSets
        # 如果已存在同名选择集，先删除
        try:
            existing = selection_sets.Item(name)
            existing.Delete()
        except:
            pass

        return selection_sets.Add(name)

    def select_all(self) -> Any:
        """
        选择所有实体

        Returns:
            包含所有实体的选择集
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        selection_set = self.create_selection_set("_TempSelectAll")
        selection_set.Select(5)  # acSelectionSetAll
        return selection_set

    def select_window(self, min_point: Point3D, max_point: Point3D) -> Any:
        """
        窗口选择实体

        Args:
            min_point: 窗口左下角点
            max_point: 窗口右上角点

        Returns:
            包含选中实体的选择集
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        selection_set = self.create_selection_set("_TempWindowSelect")
        selection_set.Select(2, min_point, max_point)  # acSelectionSetWindow
        return selection_set

    # 视图和视口管理
    # ----------------------------------------------------------------------------

    def create_view(self, view_name: str, center: Point3D,
                    height: float, width: float) -> Any:
        """
        创建命名视图

        Args:
            view_name: 视图名称
            center: 视图中心点
            height: 视图高度
            width: 视图宽度

        Returns:
            创建的视图对象
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        views = self._doc.Views
        view = views.Add(view_name)
        view.Center = center
        view.Height = height
        view.Width = width

        return view

    def set_active_viewport(self, viewport_name: str) -> None:
        """
        设置当前活动视口

        Args:
            viewport_name: 视口名称
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        viewport = self._doc.Viewports.Item(viewport_name)
        self._doc.ActiveViewport = viewport

    # 系统变量操作
    # ----------------------------------------------------------------------------

    def get_variable(self, var_name: str) -> Any:
        """
        获取系统变量值

        Args:
            var_name: 变量名称

        Returns:
            变量值
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self._doc.GetVariable(var_name)

    def set_variable(self, var_name: str, value: Any) -> None:
        """
        设置系统变量值

        Args:
            var_name: 变量名称
            value: 变量值
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.SetVariable(var_name, value)