from PIL import Image, ImageDraw, ImageFont
import re

def draw_points_on_image(img, mapped_points):
    """
    在图片上绘制点

    :param img: PIL.Image对象，要绘制点的图片
    :param mapped_points: list，映射后的点坐标列表，每个元素为一个坐标元组
    :return: PIL.Image对象，绘制点后的图片
    """
    # 绘制底图
    draw = ImageDraw.Draw(img)

    # 绘制点
    point_radius = 3  # 点的半径
    point_color = 'red'  # 点的颜色
    font_size = 8  # 字体大小
    font_color = (0, 255, 255)  # 字体颜色
    font = ImageFont.truetype('/cbs/codm_mp/codm_mp_sail/codm_cpu/ai_service/tools/plot_ai_trajectory/font/msyh.ttc', font_size)
    count = 0
    for point in mapped_points:
        draw.ellipse((point[0]-point_radius, point[1]-point_radius,
                      point[0]+point_radius, point[1]+point_radius),
                     fill=point_color, outline=point_color)
        # # 绘制文字
        # text = f"({count})"  # 文字内容
        # text_width, text_height = draw.textsize(text, font=font)  # 计算文字大小
        # text_x = point[0] - text_width // 2  # 计算文字位置
        # text_y = point[1] + point_radius + 2  # 计算文字位置
        # draw.text((text_x, text_y), text, font=font, fill=font_color)  # 绘制文字
        # count += 1

    return img
# 打开底图

# 打开txt文件
with open('./plot_pickup_points/forrest/inhouse.txt', 'r') as f:
    # 读取文件内容
    lines = f.readlines()

    # 提取每一行的XY值
    # pattern = r'X=(-?\d+\.\d+),Y=(-?\d+\.\d+)'
    points = []
    for line in lines:
        nums = [float(num) for num in line.split()]
        pointXZ = [nums[1]/100, nums[0]/100]
        points.append(tuple(pointXZ))

    # 游戏地图坐标点
    print(points)

img = Image.open('./plot_pickup_points/forrest/forrest_map.png')

# 图片大小和游戏地图坐标范围
img_width, img_height = img.size
print(img_width, img_height)
map_left, map_top, map_right, map_bottom = -5550, 2666.83, -7279.32, 3870.88

# 游戏地图坐标点
# points = [(-6631.47, 3332.55),(-6185.58, 3022.52)]

# 计算坐标映射比例
x_ratio = img_width / (map_right - map_left)
y_ratio = img_height / (map_top - map_bottom)

# 计算坐标映射后的点位置
mapped_points = [((p[0] - map_left) * x_ratio, (map_top - p[1]) * y_ratio) for p in points]

# 绘制点并保存图片
img_with_points = draw_points_on_image(img, mapped_points)

# 显示图片
img.save('./plot_pickup_points/forrest/forrest_inhouse.png')
