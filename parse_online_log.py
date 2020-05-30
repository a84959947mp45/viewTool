#! /usr/bin/env python3
import sys
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path
import math
from matplotlib.lines import Line2D

transform=dict()
transform['ChinaAlt'] = dict(scale=39, offset_x=-35, offset_y=260, plot_args=dict(linewidth=2, alpha=0.9), theta=0)
transform['MexicoAlt'] = dict(scale=450, offset_x=-500, offset_y=1250, plot_args=dict(linewidth=7, alpha=0.9), theta=0)
transform['canada_race'] = dict(scale=380, offset_x=-180, offset_y=1100, plot_args=dict(linewidth=7, alpha=0.9), theta=0)

track='canada_race'

def rotate(x, y, xo, yo, theta):  # rotate x,y around xo,yo by theta (rad)
    theta = theta * math.pi / 180
    xr = math.cos(theta)*(x-xo)-math.sin(theta)*(y-yo) + xo
    yr = math.sin(theta)*(x-xo)+math.cos(theta)*(y-yo) + yo
    return [xr, yr]


def shift(x, y, dx, dy):
    return x+dx, y+dy


def plot_photo_track(img_path):
    img = plt.imread(img_path)
    ax = plt.gca()
    ax.imshow(img)


def on_key(event):
    if event.key == 'q':
        exit()

def get_waypoints(track_name):
    p = Path(
        '/home/chuyj/CGI_DeepRacer/env/simulation_ws/src/deepracer_simulation_environment/routes/')
    return np.load((p / track_name).with_suffix('.npy'))

class ColorMaper:
    colors=['#9b59b6', '#3498db', '#1abc9c', '#f1c40f', '#e74c3c']
    condition=[(0, 4), (4, 6), (6, 8), (8, 10), (10, 12)]

    @staticmethod
    def speed2color(speed):
        for i, cond in enumerate(ColorMaper.condition):
            if speed > cond[0] and speed <= cond[1]:
                return ColorMaper.colors[i] 


    @staticmethod
    def custom_lines():
        customized = []
        for c in ColorMaper.colors:
            customized.append(Line2D([0], [0], color=c, lw=4))
        return customized

    @staticmethod
    def legend_label():
        labels = []
        for cond in ColorMaper.condition:
            labels.append(f'{cond[0]} < speed <= {cond[1]}')
        return labels

def main():
    logfile = sys.argv[1]
    img_path = sys.argv[2]
    dst = sys.argv[3]
    list_x = []
    list_y = []
    count = 0
 
    fig = plt.figure(figsize=(20, 20))
    fig.canvas.mpl_connect('key_press_event', on_key)
    plot_photo_track(img_path)
    with open(logfile, 'r', encoding='UTF-8') as file:
        for line in file:
            if not line.startswith("SIM_TRACE_LOG"):
                if len(list_x) > 1:
                    plot_args = transform[track]['plot_args']
                    plt.plot(list_x, list_y, **plot_args)
                list_x = []
                list_y = []
            else:
                line = line.split(',')
                x, y, speed = float(line[2]), float(line[3]), float(line[6])
                scale = transform[track]['scale']
                x, y = x * scale, y * scale
                x, y = rotate(x, y, 0, 0, transform[track]['theta'])
                x, y = shift(x, y, transform[track]['offset_x'], transform[track]['offset_y'])
                list_x.append(x)
                list_y.append(y)
                if len(list_x) >=2:
                    plt.plot(list_x, list_y, color=ColorMaper.speed2color(speed), **transform[track]['plot_args'] )
                    list_x = [list_x[-1]]
                    list_y = [list_y[-1]]
    plt.legend(ColorMaper.custom_lines(), ColorMaper.legend_label(), loc='lower right', fontsize=30)
    plt.savefig(dst)


if __name__ == "__main__":
    main()
