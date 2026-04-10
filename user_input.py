"""
CAD管理器用户输入和几何计算模块
"""

import win32com.client
import pythoncom
from contextlib import contextmanager
from typing import Optional, List, Tuple, Any
# 动态导入，支持作为包或独立模块运行
if __package__:
    # 作为包的一部分运行，使用相对导入
    from .constants import Point3D, AcInputFlags, AcAngleUnits, AcUnits, AcCoordinateSystem
    from .exceptions import ConnectionError, UserInputError
else:
    # 作为独立模块运行，使用绝对导入
    from constants import Point3D, AcInputFlags, AcAngleUnits, AcUnits, AcCoordinateSystem
    from exceptions import ConnectionError, UserInputError

class UserInputMixin:
    """用户输入和几何计算混合类"""

    # 用户输入方法
    # ----------------------------------------------------------------------------

    def get_point(self, base_point: Optional[Point3D] = None,
                  prompt: str = "指定点: ") -> Point3D:
        """
        获取点坐标（用户交互）

        Args:
            base_point: 基准点（可选）
            prompt: 提示信息

        Returns:
            用户指定的点坐标

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetPoint(base_point, prompt)
        except Exception as e:
            raise UserInputError(f"获取点输入失败: {e}")

    def get_distance(self, base_point: Optional[Point3D] = None,
                     prompt: str = "输入距离: ") -> float:
        """
        获取距离值（用户交互）

        Args:
            base_point: 基准点（可选）
            prompt: 提示信息

        Returns:
            用户输入的距离值

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetDistance(base_point, prompt)
        except Exception as e:
            raise UserInputError(f"获取距离输入失败: {e}")

    def get_angle(self, base_point: Optional[Point3D] = None,
                  prompt: str = "输入角度: ") -> float:
        """
        获取角度值（弧度，用户交互）

        Args:
            base_point: 基准点（可选）
            prompt: 提示信息

        Returns:
            用户输入的角度值（弧度）

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetAngle(base_point, prompt)
        except Exception as e:
            raise UserInputError(f"获取角度输入失败: {e}")

    def get_integer(self, prompt: str = "输入整数: ") -> int:
        """
        获取整数值（用户交互）

        Args:
            prompt: 提示信息

        Returns:
            用户输入的整数值

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetInteger(prompt)
        except Exception as e:
            raise UserInputError(f"获取整数输入失败: {e}")

    def get_string(self, has_spaces: bool, prompt: str) -> str:
        """
        获取字符串值（用户交互）

        Args:
            has_spaces: 是否允许包含空格
            prompt: 提示信息

        Returns:
            用户输入的字符串

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetString(has_spaces, prompt)
        except Exception as e:
            raise UserInputError(f"获取字符串输入失败: {e}")

    def get_keyword(self, prompt: str) -> str:
        """
        获取关键字（用户交互）

        Args:
            prompt: 提示信息

        Returns:
            用户选择的关键字

        Raises:
            UserInputError: 用户取消输入时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            return self.utility.GetKeyword(prompt)
        except Exception as e:
            raise UserInputError(f"获取关键字输入失败: {e}")

    def initialize_user_input(self, bits: int,
                              keywords: Optional[str] = None) -> None:
        """
        初始化用户输入选项

        Args:
            bits: 位标志组合 (AcInputFlags)
            keywords: 关键字列表，用空格分隔（可选）
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        if keywords:
            self.utility.InitializeUserInput(bits, keywords)
        else:
            self.utility.InitializeUserInput(bits, "")

    # 几何计算方法
    # ----------------------------------------------------------------------------

    def distance(self, point1: Point3D, point2: Point3D) -> float:
        """
        计算两点间距离

        Args:
            point1: 第一点
            point2: 第二点

        Returns:
            两点距离
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.Distance(point1, point2)

    def angle_from_x_axis(self, point: Point3D) -> float:
        """
        计算点与X轴的夹角

        Args:
            point: 点坐标

        Returns:
            夹角（弧度）
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.AngleFromXAxis(point)

    def polar_point(self, base_point: Point3D, angle: float,
                    distance: float) -> Point3D:
        """
        计算极坐标点

        Args:
            base_point: 基准点
            angle: 角度（弧度）
            distance: 距离

        Returns:
            极坐标点
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.PolarPoint(base_point, angle, distance)

    def translate_coordinates(self, point: Point3D, from_sys: int,
                              to_sys: int, displacement: bool) -> Point3D:
        """
        坐标系统转换

        Args:
            point: 要转换的点
            from_sys: 源坐标系 (AcCoordinateSystem)
            to_sys: 目标坐标系 (AcCoordinateSystem)
            displacement: 是否为位移向量

        Returns:
            转换后的点
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.TranslateCoordinates(point, from_sys, to_sys, displacement)

    # 单位转换方法
    # ----------------------------------------------------------------------------

    def angle_to_real(self, angle_str: str, unit: int) -> float:
        """
        角度字符串转实数（弧度）

        Args:
            angle_str: 角度字符串
            unit: 角度单位 (AcAngleUnits)

        Returns:
            角度值（弧度）
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.AngleToReal(angle_str, unit)

    def real_to_string(self, value: float, unit: int,
                       precision: int) -> str:
        """
        实数转字符串

        Args:
            value: 数值
            unit: 单位 (AcUnits)
            precision: 精度（小数位数）

        Returns:
            格式化字符串
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.RealToString(value, unit, precision)

    def string_to_real(self, string: str, unit: int) -> float:
        """
        字符串转实数

        Args:
            string: 字符串
            unit: 单位 (AcUnits)

        Returns:
            数值
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.StringToReal(string, unit)

    # 实体操作方法
    # ----------------------------------------------------------------------------

    def get_entity(self) -> Tuple[Any, Point3D]:
        """
        通过点选获取实体

        Returns:
            (实体对象, 选择点)

        Raises:
            UserInputError: 用户取消选择时抛出
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        try:
            selected_obj = win32com.client.VARIANT(pythoncom.VT_DISPATCH, None)
            picked_point = win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, None)

            self.utility.GetEntity(selected_obj, picked_point)

            if selected_obj.Value:
                return selected_obj.Value, picked_point.Value
            else:
                raise UserInputError("未选择实体")
        except Exception as e:
            raise UserInputError(f"选择实体失败: {e}")

    def prompt(self, message: str) -> None:
        """
        在命令行显示提示信息

        Args:
            message: 提示信息
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self.utility.Prompt(message)

    # 错误处理类和工具函数
    # ----------------------------------------------------------------------------

    def start_undo_mark(self) -> None:
        """开始撤销标记（用于批量操作）"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.StartUndoMark()

    def end_undo_mark(self) -> None:
        """结束撤销标记"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        self._doc.EndUndoMark()

    @contextmanager
    def undo_group(self):
        """
        撤销组上下文管理器

        用于将一系列操作分组，可以一次性撤销。

        示例:
            with cad.undo_group():
                cad.add_line([0, 0, 0], [100, 0, 0])
                cad.add_circle([50, 50, 0], 25)
        """
        self.start_undo_mark()
        try:
            yield
        finally:
            self.end_undo_mark()

    def create_typed_array(self, var_type: int, lower_bound: int,
                           upper_bound: int) -> List[float]:
        """
        创建类型化数组（用于AutoCAD坐标）

        Args:
            var_type: 变量类型 (pythoncom.VT_R8 表示双精度)
            lower_bound: 下界
            upper_bound: 上界

        Returns:
            创建的数组
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.utility.CreateTypedArray(var_type, lower_bound, upper_bound)

    def get_entity_count(self) -> int:
        """获取模型空间实体数量"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        return self.model_space.Count

    def iterate_entities(self):
        """
        迭代模型空间中的所有实体

        Yields:
            (索引, 实体对象)
        """
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        for i in range(self.model_space.Count):
            yield i, self.model_space.Item(i)

    def print_entity_summary(self) -> None:
        """打印模型空间实体摘要"""
        if not self._connected:
            raise ConnectionError("未连接到AutoCAD")

        print(f"模型空间实体总数: {self.model_space.Count}")
        for i, entity in self.iterate_entities():
            print(f"  实体 {i}: {entity.EntityName} - 图层: {entity.Layer}")