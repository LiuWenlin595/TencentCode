import csv
from matplotlib import pyplot as plt

x = []
mark_count = []
goto_count = []
enemy_count = []
mark_dist = []
time_out = []
self_dead = []
response = []
arrive = []

# with open(r"C:\Users\hunkyliu\Desktop\1.csv", 'r', encoding='utf-8') as f:
#     reader = csv.DictReader(f)
#     for line in reader:
#         # if int(line["x"]) < 500:
#         #     continue
#         x.append(int(line['LadderLevel']))
#         mark_count.append(float(line["MarkCount"]))
#         goto_count.append(float(line['GotoCount']))
#         enemy_count.append(float(line['EnemyCount']))
#         mark_dist.append(float(line['MarkDistance']))
#         time_out.append(float(line['TimeOut']))
#         self_dead.append(float(line['SelfDead']))
#         response.append(float(line['Response']))
#         arrive.append(float(line['Arrive']))
    
# plt.plot(x, mark_count)   # 高段位有明显下降趋势
# plt.plot(x, goto_count)
# plt.plot(x, enemy_count)
# plt.legend(['markCount', 'gotoCount', 'enemyCount'])
# plt.plot(x, mark_dist)   # 有上升趋势
# plt.legend(['markDistance'])
# plt.plot(x, response)   # 无趋势
# plt.legend(['response'])
# plt.plot(x, arrive)   # 无趋势, 到达率过高, 检查代码
# plt.plot(x, time_out)
# plt.plot(x, self_dead)
# plt.legend(['arrive', 'timeOut', 'selfDead'])

# plt.xlabel('count')
# plt.ylabel('level')

# plt.show()

x = []
y1 = []
y2 = []
sum = 0
count = 0

# frame_distance出现几个小高峰, 很可能和毒圈有关, 但是毒圈明显的越到后期缩的越快

with open(r"C:\Users\hunkyliu\Desktop\receiverAliveFrameNum.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for line in reader:
        if int(line["x"]) < 2500:
            continue
        if int(line["x"]) > 5900:
            break
        x.append(float(line['x']))
        if line["y"] == "":
            y1.append(0)
        else:
            y1.append(float(line["y"])/28326) # sender: 69134 61936 50216   # receiver:1600/29889  2500/28326
#         sum += float(line['x']) * float(line["y"])
#         count += float(line["y"])

# print(sum, count)
# print(sum/count)

with open(r"C:\Users\hunkyliu\Desktop\noReceiverAliveFrameNum.csv", 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for line in reader:
        if int(line["x"]) < 2500:
            continue
        if int(line["x"]) > 5900:
            break
        # x.append(float(line['x']))
        if line["y"] == "":
            y2.append(0)
        else:
            y2.append(float(line["y"])/653621)  # sender: 550987 240632 142229  receiver:1600/1228963  2500/653621

plt.plot(x, y1)
plt.plot(x, y2)
plt.xlabel('frame')
plt.ylabel('ratio')
plt.legend(['receiverSuccessFrame', 'noReceiverSuccess'])
plt.show()