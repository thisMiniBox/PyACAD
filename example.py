"""
CAD管理器使用示例
此文件展示如何使用拆分后的CAD管理器模块。
"""

from CadManager import CadManager, degrees_to_radians, create_point_3d

def main():
    print("AutoCAD CAD管理器示例")
    print("=" * 50)

    # 示例1: 基本连接和绘图
    print("\n示例1: 基本连接和绘图")
    print("-" * 30)

    try:
        with CadManager(visible=True) as cad:
            print("已连接到AutoCAD")

            # 获取应用程序信息
            info = cad.get_application_info()
            print(f"AutoCAD版本: {info['version']}")

            # 添加一些图形
            cad.add_line([0, 0, 0], [100, 100, 0])
            cad.add_circle([50, 50, 0], 25)
            cad.add_text("Hello AutoCAD", [10, 10, 0], 5)

            # 添加多段线
            vertices = [[0, 0], [50, 0], [50, 50], [0, 50]]
            cad.add_lw_polyline(vertices)

            print("图形创建完成")

            # 显示实体摘要
            cad.print_entity_summary()

    except Exception as e:
        print(f"错误: {e}")

    # 示例2: 图层和线型管理
    print("\n示例2: 图层和线型管理")
    print("-" * 30)

    try:
        with CadManager(visible=True) as cad:
            # 创建新图层
            cad.create_layer("MyLayer", color=1, line_type="Continuous")
            cad.create_layer("AnotherLayer", color=3)

            # 获取所有图层
            layers = cad.get_all_layers()
            print(f"图层列表: {layers}")

            # 设置活动图层
            cad.set_active_layer("MyLayer")
            print("已设置活动图层为 'MyLayer'")

    except Exception as e:
        print(f"错误: {e}")

    # 示例3: 工具函数使用
    print("\n示例3: 工具函数使用")
    print("-" * 30)

    # 角度转换
    radians = degrees_to_radians(180)
    print(f"180度 = {radians} 弧度")

    # 创建点
    point = create_point_3d(10, 20, 30)
    print(f"创建的点: {point}")

    print("\n示例执行完成！")
    print("=" * 50)

if __name__ == "__main__":
    # 注意: 这些示例需要安装AutoCAD和pywin32
    # 如果没有安装AutoCAD，示例会失败
    main()