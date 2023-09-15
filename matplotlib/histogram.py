import numpy as np
import matplotlib.pyplot as plt

def self_feature():
    data = np.loadtxt('player_features.txt', delimiter = ',')
    title = ['pro_self_pos_x', 'pro_self_pos_y', 'pro_self_pos_z', 'pro_self_rot_x', 'pro_self_rot_y', 'pro_is_battle', 'pro_pos_x', 'pro_pos_y,', 'pro_pos_z',
    'pro_last_turn_right_degree', 'pro_last_turn_down_degree', 'pro_hp', 'pro_view_size', 'pro_view_down_size', 'pro_navtarget_next_dis', 
    'pro_navtarget_nav_diff', 'pro_bm_command_target_pos_x', 'pro_bm_command_target_pos_y', 'pro_bm_command_target_pos_z', 'pro_bm_command_diff_target_pos_x',
    'pro_bm_command_diff_target_pos_z', 'pro_bm_command_next_pos_angle1', 'pro_bm_command_next_pos_angle2']
    idxs = [0, 1, 2, 3, 4, 38, 39, 40, 41, 70, 71, 119, 125, 126, 149, 152, 157, 158, 159, 160, 161, 162, 163]
    print(len(data[0, :]))

    for i in range(len(idxs)):
        data_sample = data[:, idxs[i]]
        plt.figure(i)
        plt.title(title[i])
        plt.hist(data_sample, bins = 30)
        plt.xlabel("value")
        plt.ylabel("count")
        plt.show()

def mate_feature():
    data = np.loadtxt('allay_features.txt', delimiter = ',')
    title = ['pro_is_keyrole', 'pro_distance' , 'pro_hp', 'pro_rot_x', 'pro_rot_y', 'pro_rot_z', 'pro_mate_visible_nums', 'pro_mate_beivisible_nums',
    'pro_mate_min_dis', 'pro_mate_see_enemy_num', 'pro_enemy_see_mate_num', 'pro_mate_pos_x_diff', 'pro_mate_pos_y_diff', 'pro_mate_pos_z_diff',
    'pro_self_see_mate_x_distance', 'pro_self_see_mate_y_distance', 'pro_mate_see_self_x_distance', 'pro_mate_see_self_y_distance', 
    'pro_self_see_mate_rot_x_diff', 'pro_self_see_mate_rot_y_diff']
    idxs = [0, 31, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 76, 77, 78, 79, 80, 81]

    idx = []
    for i in range(len(data)):
        if i % 4 < 2:  # 只有两个队友
            idx.append(i)
    data = data[idx, :]

    for i in range(len(idxs)):
        plt.figure(i)
        data_sample = data[:, idxs[i]]
        plt.title(title[i])
        plt.hist(data_sample, bins = 30)
        plt.xlabel("value")
        plt.ylabel("count")
        plt.show()

def enemy_feature():
    data = np.loadtxt('enemy_features.txt', delimiter = ',')
    title = ['pro_distance', 'pro_hp', 'pro_beidamage', 'pro_body_expose_num', 'pro_nav_distance', 'pro_next_nav_distance', 'pro_distance_full',
    'pro_hp_full', 'pro_beidamage_full', ]
    idxs = [0, 31, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 76, 77, 78, 79, 80, 81]

    idx = []
    for i in range(len(data)):
        if i % 4 < 2:  # 只有两个队友
            idx.append(i)
    data = data[idx, :]

    for i in range(len(idxs)):
        data_sample = data[:, idxs[i]]
        plt.figure(i)
        plt.title(title[i])
        plt.hist(data_sample, bins = 30)
        plt.xlabel("value")
        plt.ylabel("count")
        plt.show()


if __name__=="__main__":
    self_feature()
    # mate_feature()
    # enemy_feature()