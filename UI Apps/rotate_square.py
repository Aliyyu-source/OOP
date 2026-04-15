import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

plt.rcParams['toolbar'] = 'none'


def rot_x(angle):
    a = np.radians(angle)
    return np.array([
        [1, 0, 0],
        [0, np.cos(a), -np.sin(a)],
        [0, np.sin(a), np.cos(a)]
    ])


def rot_y(angle):
    a = np.radians(angle)
    return np.array([
        [np.cos(a), 0, np.sin(a)],
        [0, 1, 0],
        [-np.sin(a), 0, np.cos(a)]
    ])


def rot_z(angle):
    a = np.radians(angle)
    return np.array([
        [np.cos(a), -np.sin(a), 0],
        [np.sin(a), np.cos(a), 0],
        [0, 0, 1]
    ])


def run():
    square = np.array([
        [-0.5, -0.5, 0],
        [0.5, -0.5, 0],
        [0.5, 0.5, 0],
        [-0.5, 0.5, 0],
        [-0.5, -0.5, 0]
    ])

    fig = plt.figure("Rotate The Square")
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    (line,) = ax.plot(square[:, 0], square[:, 1], square[:, 2], 'g--')
    (points,) = ax.plot(square[:, 0], square[:, 1], square[:, 2], 'go')

    plt.subplots_adjust(left=0.15, bottom=0.25)

    ax_x = plt.axes([0.15, 0.15, 0.65, 0.03])
    ax_y = plt.axes([0.15, 0.10, 0.65, 0.03])
    ax_z = plt.axes([0.15, 0.05, 0.65, 0.03])

    slider_x = Slider(ax_x, 'X°', 0, 360, valinit=0)
    slider_y = Slider(ax_y, 'Y°', 0, 360, valinit=0)
    slider_z = Slider(ax_z, 'Z°', 0, 360, valinit=0)

    def update(val):
        angle_x = slider_x.val
        angle_y = slider_y.val
        angle_z = slider_z.val

        R = rot_x(angle_x) @ rot_y(angle_y) @ rot_z(angle_z)
        rotated = square @ R.T

        line.set_data(rotated[:, 0], rotated[:, 1])
        line.set_3d_properties(rotated[:, 2])

        points.set_data(rotated[:, 0], rotated[:, 1])
        points.set_3d_properties(rotated[:, 2])

        fig.canvas.draw_idle()

    slider_x.on_changed(update)
    slider_y.on_changed(update)
    slider_z.on_changed(update)

    plt.show()
