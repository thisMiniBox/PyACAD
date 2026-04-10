# CAD管理器 - AutoCAD COM API 类型安全封装

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

一个用于AutoCAD COM API的高级Python封装库，提供类型安全、模块化的接口，用于自动化AutoCAD操作。

## 📋 目录

- [项目概述](#项目概述)
- [主要特性](#主要特性)
- [系统要求](#系统要求)
- [安装指南](#安装指南)
- [快速开始](#快速开始)
- [API文档](#api文档)
  - [连接管理](#连接管理)
  - [应用程序控制](#应用程序控制)
  - [文档管理](#文档管理)
  - [实体创建](#实体创建)
  - [管理控制](#管理控制)
  - [用户输入](#用户输入)
  - [工具函数](#工具函数)
  - [异常处理](#异常处理)
  - [类型定义](#类型定义)
- [模块结构](#模块结构)
- [示例代码](#示例代码)
- [许可证](#许可证)

## 🎯 项目概述

CAD管理器是一个针对AutoCAD COM API的高级Python封装库，通过模块化设计和类型注解，提供安全、易用的AutoCAD自动化接口。该库将庞大的AutoCAD API拆分为多个功能模块，提高了代码的可维护性和可重用性。

## ✨ 主要特性

- ✅ **类型安全**：全面的类型注解，提高代码可靠性和IDE支持
- ✅ **模块化设计**：功能按模块划分，便于维护和扩展
- ✅ **Mixin模式**：通过多继承组合功能，结构清晰
- ✅ **上下文管理器**：自动连接/断开连接，资源管理更安全
- ✅ **完整API覆盖**：支持绘图、图层、标注、用户输入等核心功能
- ✅ **向后兼容**：保持原有接口，现有代码无需修改
- ✅ **详细文档**：完整的API文档和示例代码
- ✅ **错误处理**：自定义异常类，便于错误诊断和处理

## 🖥️ 系统要求

- **操作系统**: Windows 7/10/11
- **AutoCAD**: 2010及以上版本（推荐2018+）
- **Python**: 3.8及以上版本
- **依赖库**:
  - `pywin32` (用于COM接口)
  - `pythoncom` (COM支持)

## 📦 安装指南

### 1. 安装依赖

```bash
pip install pywin32
```

### 2. 获取CAD管理器

将整个`CadManager`目录复制到您的项目目录中，或通过以下方式安装：

```bash
# 从本地目录安装（开发模式）
pip install -e /path/to/CadManager
```

### 3. 验证安装

```python
import sys
sys.path.insert(0, '.')  # 如果未安装为包，添加当前目录到路径
from CadManager import CadManager
print("CAD管理器导入成功")
```

## 🚀 快速开始

### 基本使用示例

```python
from CadManager import CadManager

# 使用上下文管理器自动管理连接
with CadManager(visible=True) as cad:
    # 添加图形
    cad.add_line([0, 0, 0], [100, 100, 0])
    cad.add_circle([50, 50, 0], 25)
    cad.add_text("Hello AutoCAD", [10, 10, 0], 5)

    # 获取应用程序信息
    info = cad.get_application_info()
    print(f"AutoCAD版本: {info['version']}")

    # 缩放显示全部图形
    cad.zoom_all()
```

### 更多示例

查看 [example.py](example.py) 文件获取完整示例。

## 📚 API文档

### 连接管理 (`connection.py`)

| 方法/属性 | 描述 | 示例 |
|----------|------|------|
| `connect()` | 连接到AutoCAD | `cad.connect()` |
| `disconnect()` | 断开连接 | `cad.disconnect()` |
| `quit_application()` | 退出AutoCAD | `cad.quit_application()` |
| `is_connected` | 连接状态 | `if cad.is_connected:` |
| `application` | AutoCAD应用程序对象 | `app = cad.application` |
| `document` | 当前文档对象 | `doc = cad.document` |
| `model_space` | 模型空间对象 | `ms = cad.model_space` |
| `paper_space` | 图纸空间对象 | `ps = cad.paper_space` |
| `utility` | 实用工具对象 | `util = cad.utility` |

### 应用程序控制 (`application.py`)

| 方法 | 描述 | 示例 |
|------|------|------|
| `get_application_info()` | 获取应用程序信息 | `info = cad.get_application_info()` |
| `set_window_state()` | 设置窗口状态 | `cad.set_window_state(AcWindowState.acMax)` |
| `set_window_position()` | 设置窗口位置和大小 | `cad.set_window_position(0, 0, 800, 600)` |
| `zoom_all()` | 缩放全部 | `cad.zoom_all()` |
| `zoom_extents()` | 范围缩放 | `cad.zoom_extents()` |
| `zoom_window()` | 窗口缩放 | `cad.zoom_window([0,0,0], [100,100,0])` |
| `zoom_center()` | 中心缩放 | `cad.zoom_center([50,50,0], 2.0)` |

### 文档管理 (`document.py`)

| 方法 | 描述 | 示例 |
|------|------|------|
| `new_document()` | 创建新文档 | `doc = cad.new_document()` |
| `open_document()` | 打开现有文档 | `doc = cad.open_document("drawing.dwg")` |
| `save_document()` | 保存文档 | `cad.save_document()` |
| `save_document_as()` | 另存文档 | `cad.save_document_as("new_drawing.dwg")` |
| `close_document()` | 关闭文档 | `cad.close_document(save_changes=True)` |
| `get_document_info()` | 获取文档信息 | `info = cad.get_document_info()` |
| `regen()` | 重生成图形 | `cad.regen(AcRegenType.acAllViewports)` |
| `purge_all()` | 清理未使用对象 | `cad.purge_all()` |
| `send_command()` | 发送命令 | `cad.send_command("LINE 0,0 100,100 ")` |

### 实体创建 (`entities.py`)

| 方法 | 描述 | 示例 |
|------|------|------|
| `add_line()` | 添加直线 | `cad.add_line([0,0,0], [100,0,0])` |
| `add_circle()` | 添加圆 | `cad.add_circle([50,50,0], 25)` |
| `add_arc()` | 添加圆弧 | `cad.add_arc([50,50,0], 25, 0, 3.14)` |
| `add_text()` | 添加单行文字 | `cad.add_text("文本", [10,10,0], 5)` |
| `add_mtext()` | 添加多行文字 | `cad.add_mtext([10,10,0], 50, "多行文本")` |
| `add_polyline()` | 添加二维多段线 | `cad.add_polyline([[0,0], [50,0], [50,50]])` |
| `add_lw_polyline()` | 添加轻量多段线 | `cad.add_lw_polyline([[0,0], [50,0], [50,50]])` |
| `add_3d_polyline()` | 添加三维多段线 | `cad.add_3d_polyline([[0,0,0], [50,0,10], [50,50,20]])` |
| `add_spline()` | 添加样条曲线 | `cad.add_spline([[0,0,0], [30,30,0], [60,0,0]])` |
| `add_hatch()` | 添加图案填充 | `cad.add_hatch(AcPatternType.acHatchPatternTypePreDefined, "ANSI31")` |
| `add_dim_aligned()` | 添加对齐标注 | `cad.add_dim_aligned([0,0,0], [100,0,0], [50,10,0])` |
| `add_dim_radial()` | 添加半径标注 | `cad.add_dim_radial([50,50,0], [75,50,0], 10)` |
| `add_block_reference()` | 插入块参照 | `cad.add_block_reference([0,0,0], "MyBlock")` |

### 管理控制 (`management.py`)

**图层管理**
```python
cad.create_layer("MyLayer", color=1, line_type="Continuous")
layers = cad.get_all_layers()
cad.set_active_layer("MyLayer")
cad.delete_layer("OldLayer")
```

**线型管理**
```python
cad.load_line_type("DASHED", "acad.lin")
cad.set_active_line_type("DASHED")
```

**文字样式管理**
```python
cad.create_text_style("MyStyle", "Arial", height=5.0)
cad.set_active_text_style("MyStyle")
```

**标注样式管理**
```python
cad.set_active_dim_style("Standard")
```

**选择集管理**
```python
selection = cad.create_selection_set("MySelection")
all_entities = cad.select_all()
window_selection = cad.select_window([0,0,0], [100,100,0])
```

**视图管理**
```python
view = cad.create_view("MyView", [50,50,0], 100, 100)
cad.set_active_viewport("Viewport1")
```

**系统变量**
```python
value = cad.get_variable("OSMODE")
cad.set_variable("OSMODE", 0)
```

### 用户输入 (`user_input.py`)

| 方法 | 描述 | 示例 |
|------|------|------|
| `get_point()` | 获取点坐标 | `point = cad.get_point(None, "指定点: ")` |
| `get_distance()` | 获取距离 | `dist = cad.get_distance(None, "输入距离: ")` |
| `get_angle()` | 获取角度 | `angle = cad.get_angle(None, "输入角度: ")` |
| `get_integer()` | 获取整数 | `num = cad.get_integer("输入整数: ")` |
| `get_string()` | 获取字符串 | `text = cad.get_string(True, "输入文本: ")` |
| `get_keyword()` | 获取关键字 | `key = cad.get_keyword("选择[是(Y)/否(N)]: ")` |
| `initialize_user_input()` | 初始化输入选项 | `cad.initialize_user_input(AcInputFlags.ACRX_NONULL)` |

**几何计算**
```python
distance = cad.distance([0,0,0], [100,0,0])
angle = cad.angle_from_x_axis([50,50,0])
point = cad.polar_point([0,0,0], 0.785, 100)
new_point = cad.translate_coordinates([10,10,0], AcCoordinateSystem.acWorld, AcCoordinateSystem.acUCS, False)
```

**单位转换**
```python
radians = cad.angle_to_real("45d", AcAngleUnits.acDegrees)
string = cad.real_to_string(123.456, AcUnits.acDecimal, 2)
value = cad.string_to_real("123.456", AcUnits.acDecimal)
```

**实体操作**
```python
entity, point = cad.get_entity()
cad.prompt("操作完成")
```

**撤销管理**
```python
cad.start_undo_mark()
# 执行一系列操作
cad.end_undo_mark()

# 或使用上下文管理器
with cad.undo_group():
    cad.add_line([0,0,0], [100,0,0])
    cad.add_circle([50,50,0], 25)
```

**实体迭代**
```python
count = cad.get_entity_count()
for i, entity in cad.iterate_entities():
    print(f"实体 {i}: {entity.EntityName}")
cad.print_entity_summary()
```

### 工具函数 (`utils.py`)

| 函数 | 描述 | 示例 |
|------|------|------|
| `degrees_to_radians()` | 度转弧度 | `rad = degrees_to_radians(180)` |
| `radians_to_degrees()` | 弧度转度 | `deg = radians_to_degrees(3.14159)` |
| `create_point_2d()` | 创建二维点 | `point = create_point_2d(10, 20)` |
| `create_point_3d()` | 创建三维点 | `point = create_point_3d(10, 20, 30)` |
| `create_vector_2d()` | 创建二维向量 | `vector = create_vector_2d(1, 0)` |
| `create_vector_3d()` | 创建三维向量 | `vector = create_vector_3d(1, 0, 0)` |

### 异常处理 (`exceptions.py`)

| 异常类 | 描述 | 触发条件 |
|--------|------|----------|
| `CadManagerError` | 基类异常 | 所有CAD管理器异常的基类 |
| `ConnectionError` | 连接异常 | 连接AutoCAD失败时 |
| `UserInputError` | 用户输入异常 | 用户取消输入或输入无效时 |
| `DocumentError` | 文档操作异常 | 文档操作失败时 |
| `EntityError` | 实体操作异常 | 实体创建或操作失败时 |

```python
from CadManager import ConnectionError, UserInputError

try:
    with CadManager() as cad:
        point = cad.get_point(None, "指定点: ")
except ConnectionError as e:
    print(f"连接失败: {e}")
except UserInputError as e:
    print(f"用户输入取消: {e}")
```

### 类型定义 (`constants.py`)

**类型别名**
```python
Point3D = List[float]  # [x, y, z]
Point2D = List[float]  # [x, y]
Vector3D = List[float]  # [x, y, z]
Vector2D = List[float]  # [x, y]
```

**枚举类**
- `AcWindowState` - 窗口状态
- `AcZoomScaleType` - 缩放比例类型
- `AcActiveSpace` - 活动空间
- `AcRegenType` - 重生成类型
- `AcPatternType` - 填充图案类型
- `AcAttributeMode` - 属性模式
- `AcAngleUnits` - 角度单位
- `AcUnits` - 线性单位
- `AcCoordinateSystem` - 坐标系统
- `AcInputFlags` - 用户输入初始化标志

## 📁 模块结构

```
CadManager/
├── __init__.py              # 包初始化，导出公共接口
├── cad_manager.py           # 主类，组合所有功能模块
├── CadManager.py            # 主入口点，保持向后兼容
├── constants.py             # 类型别名和枚举常量
├── exceptions.py            # 自定义异常类
├── utils.py                 # 工具函数
├── connection.py            # 连接管理模块
├── application.py           # 应用程序控制模块
├── document.py              # 文档管理模块
├── entities.py              # 实体创建模块
├── management.py            # 管理控制模块
├── user_input.py            # 用户输入和几何计算模块
├── example.py               # 使用示例
└── CadManager_original.py   # 原文件备份（重构前）
```

## 💡 示例代码

### 示例1：基本绘图

```python
from CadManager import CadManager

with CadManager(visible=True) as cad:
    # 创建图层
    cad.create_layer("轮廓", color=1)  # 红色
    cad.create_layer("标注", color=3)  # 绿色

    # 切换到轮廓图层
    cad.set_active_layer("轮廓")

    # 绘制矩形
    vertices = [[0, 0], [100, 0], [100, 50], [0, 50]]
    cad.add_lw_polyline(vertices)

    # 绘制圆
    cad.add_circle([50, 25, 0], 20)

    # 切换到标注图层
    cad.set_active_layer("标注")

    # 添加标注
    cad.add_dim_aligned([0, 0, 0], [100, 0, 0], [50, -10, 0])
    cad.add_dim_aligned([0, 0, 0], [0, 50, 0], [-10, 25, 0])

    # 添加文字
    cad.add_text("示例图形", [50, 60, 0], 5)

    # 缩放显示全部
    cad.zoom_all()
```

### 示例2：批量操作和撤销

```python
from CadManager import CadManager
import math

with CadManager(visible=True) as cad:
    # 使用撤销组进行批量操作
    with cad.undo_group():
        # 绘制齿轮轮廓
        points = []
        for i in range(36):
            angle = i * 10 * math.pi / 180
            radius = 50 + 10 * math.sin(angle * 5)
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)
            points.append([x, y])

        # 闭合轮廓
        points.append(points[0])
        cad.add_lw_polyline(points)

    print("齿轮绘制完成，可以按Ctrl+Z撤销全部操作")
```

### 示例3：用户交互绘图

```python
from CadManager import CadManager

with CadManager(visible=True) as cad:
    print("交互式绘图示例")
    print("=" * 50)

    # 获取起点
    start_point = cad.get_point(None, "指定起点: ")

    # 获取终点
    end_point = cad.get_point(start_point, "指定终点: ")

    # 绘制直线
    cad.add_line(start_point, end_point)

    # 计算中点
    mid_x = (start_point[0] + end_point[0]) / 2
    mid_y = (start_point[1] + end_point[1]) / 2
    center = [mid_x, mid_y, 0]

    # 获取半径
    radius = cad.get_distance(center, "输入半径: ")

    # 绘制圆
    cad.add_circle(center, radius)

    print("绘图完成！")
```

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件。

## 🤝 贡献指南

欢迎提交Issue和Pull Request来改进这个项目。

## 📞 支持与反馈

如有问题或建议，请通过以下方式联系：
- 提交GitHub Issue
- 发送电子邮件至项目维护者

---

**注意**: 使用此库需要安装AutoCAD和pywin32。在没有安装AutoCAD的环境中运行示例代码会失败。

**安全提示**: 本库仅用于合法的AutoCAD自动化任务，请勿用于非法用途。