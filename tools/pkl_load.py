import pickle
import numpy as np
np.set_printoptions(threshold=np.inf)

f = open(r'C:\Users\hunkyliu\Desktop\proto_map500a0003_room25531405_pid7741_chn_2022080212.pkl', "rb")   # 文件所在路径
match_info = pickle.load(f, encoding='bytes')
players_frame_list = pickle.load(f, encoding='bytes')
players_ctrl_list = pickle.load(f, encoding='bytes')
# print(match_info.keys())
# print(len(players_frame_list))
# print(type(players_frame_list[0]))
# print(len(players_ctrl_list))
print(players_ctrl_list[0])
f.close()

# inf = str(inf)
# ft = open('test4.txt', 'w')
# ft.write(inf)