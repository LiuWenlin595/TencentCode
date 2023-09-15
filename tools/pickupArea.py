import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from PIL import Image

# img = Image.open('./plot_pickup_points/forrest/forrest_map.png')
img = Image.open('./plot_pickup_points/forrest/forest_big_map.png')
img_width, img_height = img.size
print(img_width, img_height)
# map_left, map_top, map_right, map_bottom = -5550, 2638, -7279.32, 3895  # 2638 3895  #  2666.83 3870.88
map_left, map_top, map_right, map_bottom = -5271.14, 2177.52, -7527.14, 4433.52 
x_ratio = img_width / (map_right - map_left)
y_ratio = img_height / (map_top - map_bottom)


def dfm_xz_convert(pos):
    return [((pos[0]-3700)/100 - map_left) * x_ratio, (map_top - pos[1]/100) * y_ratio]


def run():
    
    # inner_area_polygon.append([[-609286, 373248], [-615210, 373562]])
    # inner_area_polygon.append([[-630990, 303680], [-642513, 303916]])
    # inner_area_polygon.append([[-634712, 278177], [-648075, 278096]])
    # inner_area_polygon.append([[-609703, 373821], [-614745, 374283]])
    # 区域顺序: 酒店、火车站、教堂、小屋、村庄、车站、小镇、检查站、储藏室、码头、牧场、观测站
    inner_area_polygon = []
    inner_area_polygon.append([[-623635, 348002], [-635734, 348002], [-635734, 350134], [-639980, 350134], [-639980, 363279], [-637786, 363279], [-637786, 371664], [-632621, 371664], [-632621, 373085], [-628163, 373085], [-628163, 368964], [-624554, 368964], [-624554, 362782], [-623422, 362782], [-623635, 348002]])
    inner_area_polygon.append([[-631697, 305601], [-644310, 305601], [-644310, 322400], [-634781, 322400], [-634781, 318269], [-633019, 318269], [-633019, 315240], [-631642, 315240], [-631697, 305601]])
    inner_area_polygon.append([[-576564, 334517], [-582347, 334517], [-582347, 340576], [-576564, 340576], [-576564, 334517]])
    inner_area_polygon.append([[-588406, 325705], [-591710, 324934], [-592537, 328459], [-589507, 329615], [-588406, 325705]])
    inner_area_polygon.append([[-694431, 347736], [-698287, 346634], [-705171, 347736], [-702417, 355998], [-696083, 354070], [-694431, 347736]])
    inner_area_polygon.append([[-688648, 333691], [-702968, 333691], [-702968, 340025], [-688648, 340025], [-688648, 333691]])
    inner_area_polygon.append([[-659181, 326255], [-669371, 326255], [-669371, 337822], [-659181, 337822], [-659181, 326255]])
    inner_area_polygon.append([[-609886, 374724], [-614292, 374724], [-614292, 379681], [-609886, 379681], [-609886, 374724]])
    inner_area_polygon.append([[-663863, 294861], [-673501, 294861], [-673501, 303123], [-663863, 303123], [-663863, 294861]])
    inner_area_polygon.append([[-655326, 371970], [-665515, 371695], [-665515, 382160], [-655326, 382160], [-653398, 375826], [-655326, 371970]])
    inner_area_polygon.append([[-572433, 351316], [-587855, 351316], [-587855, 374173], [-572433, 374173], [-572433, 351316]])
    inner_area_polygon.append([[-633570, 278337], [-653673, 278337], [-653673, 299543], [-644861, 303398], [-637425, 302021], [-637425, 295412], [-633570, 295412], [-633570, 278337]])

    outer_area_polygon = []
    outer_area_polygon.append([[-622279, 346634], [-641005, 346634], [-641005, 364810], [-637976, 374173], [-622279, 374173],[-622279, 346634]])
    outer_area_polygon.append([[-628337, 304500], [-645962, 304500], [-645962, 324052], [-633570, 324052], [-628337, 316617], [-628337, 304500]])
    outer_area_polygon.append([[-575738, 333416], [-583449, 333416], [-583449, 343330], [-575738, 343330], [-575738, 333416]])
    outer_area_polygon.append([[-585101, 326255], [-595015, 324052], [-597218, 329835], [-587304, 333416], [-585101, 326255]])
    outer_area_polygon.append([[-693880, 347736], [-705171, 344982], [-705171, 357375], [-693880, 357375], [-693880, 347736]])
    outer_area_polygon.append([[-685894, 331763], [-703794, 331763], [-703794, 340576], [-685894, 340576], [-685894, 331763]])
    outer_area_polygon.append([[-658355, 325705], [-670197, 325705], [-670197, 337822], [-658355, 337822], [-658355, 325705]])
    outer_area_polygon.append([[-608234, 373898], [-615394, 373898], [-615394, 381058], [-608234, 381058], [-608234, 373898]])
    outer_area_polygon.append([[-663037, 293759], [-673501, 293759], [-673501, 304775], [-663037, 304775], [-663037, 293759]])
    outer_area_polygon.append([[-652847, 371695], [-666617, 371695], [-666617, 382986], [-652847, 382986], [-652847, 371695]])
    outer_area_polygon.append([[-571882, 350765], [-588956, 350765], [-588956, 375275], [-571882, 375275], [-571882, 350765]])
    outer_area_polygon.append([[-631917, 276134], [-653949, 276134], [-653949, 304224], [-631917, 304224], [-631917, 276134]])


    inner_area_polygon_x = []
    inner_area_polygon_z = []
    outer_area_polygon_x = [] 
    outer_area_polygon_z = []
    for area_polygon in inner_area_polygon:
        area_polygon_x = []
        area_polygon_z = []
        for point in area_polygon:
            point = dfm_xz_convert(point)
            area_polygon_x.append(point[0])
            area_polygon_z.append(point[1])
        inner_area_polygon_x.append(area_polygon_x)
        inner_area_polygon_z.append(area_polygon_z)
    for area_polygon in outer_area_polygon:
        area_polygon_x = []
        area_polygon_z = []
        for point in area_polygon:
            point = dfm_xz_convert(point)
            area_polygon_x.append(point[0])
            area_polygon_z.append(point[1])
        outer_area_polygon_x.append(area_polygon_x)
        outer_area_polygon_z.append(area_polygon_z)

    fig, ax = plt.subplots()
    # ax.imshow(plt.imread("./plot_pickup_points/forrest/forrest_map.png"))
    ax.imshow(plt.imread("./plot_pickup_points/forrest/forest_big_map.png"))
    for area_polygon in zip(inner_area_polygon_x, inner_area_polygon_z):
        ax.plot(area_polygon[0], area_polygon[1], color='y', linewidth=1, alpha=0.6)
    for area_polygon in zip(outer_area_polygon_x, outer_area_polygon_z):
        ax.plot(area_polygon[0], area_polygon[1], color='r', linewidth=1, alpha=0.6)
    # a = dfm_xz_convert([-623348, 347854])
    # plt.scatter(a[0], a[1])
    # b = dfm_xz_convert([-635780, 347868])
    # plt.scatter(b[0], b[1])
    # ax.legend()
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    run()
    