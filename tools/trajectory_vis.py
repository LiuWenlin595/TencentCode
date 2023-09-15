import csv
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

colorMap = np.array([
    [0, 0, 0],
    [0, 0, 255],
    [0, 0, 255],
    [0, 0, 255],
    [0, 0, 255],
    [255, 0, 0],
    [255, 0, 0],
    [255, 0, 0],
    [255, 0, 0],
    [255, 0, 0],
    [0, 255, 0]]) / 255.0

def splitTrajectory(traj):
    pos_list = []
    pl = traj.split(",")[:-1]
    for i in range(0, len(pl), 3):
        try:
           d = list(map(float, pl[i:i+3]))
        except:
            pass
        finally:
            if len(d) == 3:
                pos_list.append([830+10*d[0], 840-10*d[2]])
    return pos_list

def sparseTrajectory(trajfile):
    with open(trajfile, 'r') as fp:
        lines = fp.readlines()
        camp1 = splitTrajectory(lines[0])
        camp2 = splitTrajectory(lines[1])
        bomb = splitTrajectory(lines[2])
        values = lines[3].split(",")[:-1]
        lane = lines[4].split(",")
        print("hunky", len(lines), len(camp1), len(camp2), len(bomb), len(values))
        return np.array(camp1), np.array(camp2), np.array(bomb), values, lane

def run(trajfile):
    def update_scatter(i):
        t = np.vstack([camp1[5*i:5*(i+1), :], camp2[5*i:5*(i+1), :], bomb[i, :]])
        scat.set_offsets(t)
        vals = values[6*i:6*(i+1)]
        vals = [float(i) for i in vals]
        behavior.set_text('behavior=%.6f'%vals[0])
        gail.set_text('gail=%.6f'%vals[1])
        gail_1.set_text('gail_1=%.6f'%vals[2])
        battle.set_text('battle=%.6f'%vals[3])
        sparse.set_text('sparse=%.6f'%vals[4])
        lys.set_text('lys=%.6f'%vals[5])
        sum_values.set_text('sum=%.6f'%sum(vals))
        # scat.set_array(colorMap)
        return scat
    
    camp1, camp2, bomb, values, lane = sparseTrajectory(trajfile)
    t_left = [[-32.0, -36.6], [-32.8, -48.0], [-44.4, -49.0], [-50.0, -34.0], [-50.6, -16.6], [-42.4, -14.2], [-32.0, -15.4], [-31.6, -35.8], [-32.0, -36.6]]
    t_mid = [[-2.4, -32.6], [-8.6, -32.4], [-9.8, -23.8], [-1.8, -24.0], [-1.4, -24.4], [-2.4, -32.6]]
    t_right = [[5.8, -30.8], [9.8, -41.6], [22.2, -37.2], [31.6, -18.6], [11.0, -15.6], [6.2, -16.8], [5.8, -30.8]]
    t_sniper = [[-9.6, -36.4], [-10.0, -48.8], [-1.2, -47.4], [-2.2, -32.2], [-2.2, -32.2], [-9.6, -36.4]]
    ct_left = [[-22.4, 40.4], [-21.4, 29.4], [-40.2, 30.2], [-39.4, 40.4], [-27.8, 42.8], [-22.4, 40.4]]
    ct_mid = [[-14.0, 30.6], [-0.8, 31.0], [-0.4, 11.6], [-13.6, 10.2], [-15.4, 28.0], [-14.0, 30.6]]
    ct_right = [[20.4, 42.2], [13.4, 35.8], [13.6, 31.2], [22.8, 32.0], [24.2, 41.6], [21.2, 41.8], [20.4, 42.2]]
    ct_sniper = [[-21.0, 43.8], [-17.6, 27.4], [0.4, 31.6], [-5.0, 50.0], [-20.6, 45.6], [-21.0, 43.8]]
    t_x_left, t_y_left, t_x_mid, t_y_mid, t_x_right, t_y_right, t_x_sniper, t_y_sniper = [], [], [], [], [], [], [], []
    ct_x_left, ct_y_left, ct_x_mid, ct_y_mid, ct_x_right, ct_y_right, ct_x_sniper, ct_y_sniper = [], [], [], [], [], [], [], []
    for pos in t_left:
        t_x_left.append(830+10*pos[0])
        t_y_left.append(840-10*pos[1])
    for pos in t_mid:
        t_x_mid.append(830+10*pos[0])
        t_y_mid.append(840-10*pos[1])
    for pos in t_right:
        t_x_right.append(830+10*pos[0])
        t_y_right.append(840-10*pos[1])
    for pos in t_sniper:
        t_x_sniper.append(830+10*pos[0])
        t_y_sniper.append(840-10*pos[1])
    for pos in ct_left:
        ct_x_left.append(830+10*pos[0])
        ct_y_left.append(840-10*pos[1])
    for pos in ct_mid:
        ct_x_mid.append(830+10*pos[0])
        ct_y_mid.append(840-10*pos[1])
    for pos in ct_right:
        ct_x_right.append(830+10*pos[0])
        ct_y_right.append(840-10*pos[1])
    for pos in ct_sniper:
        ct_x_sniper.append(830+10*pos[0])
        ct_y_sniper.append(840-10*pos[1])

    fig, ax = plt.subplots()
    ax.imshow(plt.imread("./Coastal.png"))
    ax.plot(t_x_left, t_y_left, color='r', linewidth=1, alpha=0.6)
    ax.plot(t_x_mid, t_y_mid, color='r', linewidth=1, alpha=0.6)
    ax.plot(t_x_right, t_y_right, color='r', linewidth=1, alpha=0.6)
    ax.plot(t_x_sniper, t_y_sniper, color='r', linewidth=1, alpha=0.6)
    ax.plot(ct_x_left, ct_y_left, color='r', linewidth=1, alpha=0.6)
    ax.plot(ct_x_mid, ct_y_mid, color='r', linewidth=1, alpha=0.6)
    ax.plot(ct_x_right, ct_y_right, color='r', linewidth=1, alpha=0.6)
    ax.plot(ct_x_sniper, ct_y_sniper, color='r', linewidth=1, alpha=0.6)
    # ax.legend()
    ct_tag = ax.text(1400, 0, f'ct_tag={lane[1]}', fontsize=6)
    t_tag = ax.text(1400, 50, f't_tag={lane[3]}', fontsize=6)
    behavior = ax.text(1400, 100, '', fontsize=6)
    gail = ax.text(1400, 150, '', fontsize=6)
    gail_1 = ax.text(1400, 200, '', fontsize=6)
    battle = ax.text(1400, 250, '', fontsize=6)
    sparse = ax.text(1400, 300, '', fontsize=6)
    lys = ax.text(1400, 350, '', fontsize=6)
    sum_values = ax.text(1400, 400, '', fontsize=6)
    scat = ax.scatter(np.concatenate([camp1[:5, 0], camp2[:5, 0], np.expand_dims(bomb[0, 0], 0)]), 
                      np.concatenate([camp1[:5, 1], camp2[:5, 1], np.expand_dims(bomb[0, 1], 0)]),
                      c=colorMap)
    ani = animation.FuncAnimation(fig, update_scatter, interval=166,frames=int(len(values)/6))
    plt.axis('off')

    # ani.save("{}.mp4".format(trajfile), writer=animation.FFMpegWriter(fps=10))
    plt.show()

if __name__ == "__main__":
    trajectoryFile = "./40_nozstat/402"
    # trajectoryFile = sys.argv[1]
    run(trajectoryFile)
    