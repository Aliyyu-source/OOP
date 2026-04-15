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
    cube_vertices = np.array([
        [-0.5, -0.5, -0.5],
        [0.5, -0.5, -0.5],
        [0.5, 0.5, -0.5],
        [-0.5, 0.5, -0.5],
        [-0.5, -0.5, 0.5],
        [0.5, -0.5, 0.5],
        [0.5, 0.5, 0.5],
        [-0.5, 0.5, 0.5]
    ])

    edges = [
        (0, 1), (1, 2), (2, 3), (3, 0),
        (4, 5), (5, 6), (6, 7), (7, 4),
        (0, 4), (1, 5), (2, 6), (3, 7)
    ]

    fig = plt.figure("Cube Rotator")
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim([-1, 1])
    ax.set_ylim([-1, 1])
    ax.set_zlim([-1, 1])

    lines = []
    for e in edges:
        (line,) = ax.plot(
            [cube_vertices[e[0], 0], cube_vertices[e[1], 0]],
            [cube_vertices[e[0], 1], cube_vertices[e[1], 1]],
            [cube_vertices[e[0], 2], cube_vertices[e[1], 2]],
            'b-'
        )
        lines.append(line)

    (points,) = ax.plot(cube_vertices[:, 0], cube_vertices[:, 1], cube_vertices[:, 2], 'bo')

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
        rotated = cube_vertices @ R.T

        for idx, e in enumerate(edges):
            lines[idx].set_data(
                [rotated[e[0], 0], rotated[e[1], 0]],
                [rotated[e[0], 1], rotated[e[1], 1]]
            )
            lines[idx].set_3d_properties(
                [rotated[e[0], 2], rotated[e[1], 2]]
            )

        points.set_data(rotated[:, 0], rotated[:, 1])
        points.set_3d_properties(rotated[:, 2])

        fig.canvas.draw_idle()

    slider_x.on_changed(update)
    slider_y.on_changed(update)
    slider_z.on_changed(update)

    plt.show()
