import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# --- Cube definition ---
cube_vertices = np.array([
    [-1, -1, -1],
    [ 1, -1, -1],
    [ 1,  1, -1],
    [-1,  1, -1],
    [-1, -1,  1],
    [ 1, -1,  1],
    [ 1,  1,  1],
    [-1,  1,  1]
])

# Move cube away from origin so axes don't appear to rotate
cube_offset = np.array([1.5, 1.5, 0])
cube_vertices = cube_vertices + cube_offset

edges = [
    (0,1), (1,2), (2,3), (3,0),
    (4,5), (5,6), (6,7), (7,4),
    (0,4), (1,5), (2,6), (3,7)
]

def rotation_matrix(ax_deg, ay_deg, az_deg):
    ax, ay, az = np.deg2rad([ax_deg, ay_deg, az_deg])

    Rx = np.array([
        [1, 0, 0],
        [0, np.cos(ax), -np.sin(ax)],
        [0, np.sin(ax),  np.cos(ax)]
    ])

    Ry = np.array([
        [ np.cos(ay), 0, np.sin(ay)],
        [ 0, 1, 0],
        [-np.sin(ay), 0, np.cos(ay)]
    ])

    Rz = np.array([
        [np.cos(az), -np.sin(az), 0],
        [np.sin(az),  np.cos(az), 0],
        [0, 0, 1]
    ])

    return Rz @ Ry @ Rx

# --- Figure ---
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection="3d")
plt.subplots_adjust(bottom=0.25)

ax.set_xlim(-3, 5)
ax.set_ylim(-3, 5)
ax.set_zlim(-3, 5)

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_title("Cube Rotating Independently of Axes")

# Draw axes (fixed)
ax.plot([-3, 3], [0, 0], [0, 0], color="black")
ax.plot([0, 0], [-3, 3], [0, 0], color="black")
ax.plot([0, 0], [0, 0], [-3, 3], color="gray")

# Points along axes
axis_pts = np.linspace(-2.5, 2.5, 6)
ax.scatter(axis_pts, np.zeros_like(axis_pts), np.zeros_like(axis_pts), color="red")
ax.scatter(np.zeros_like(axis_pts), axis_pts, np.zeros_like(axis_pts), color="blue")

# --- Initial cube lines ---
cube_lines = []
for e in edges:
    p1, p2 = cube_vertices[e[0]], cube_vertices[e[1]]
    line, = ax.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]], color="green", linewidth=2)
    cube_lines.append(line)

# --- Sliders ---
ax_x = plt.axes([0.2, 0.15, 0.6, 0.03])
ax_y = plt.axes([0.2, 0.10, 0.6, 0.03])
ax_z = plt.axes([0.2, 0.05, 0.6, 0.03])

slider_x = Slider(ax_x, "Rotate X", 0, 360, valinit=0)
slider_y = Slider(ax_y, "Rotate Y", 0, 360, valinit=0)
slider_z = Slider(ax_z, "Rotate Z", 0, 360, valinit=0)

def update(_):
    R = rotation_matrix(slider_x.val, slider_y.val, slider_z.val)

    # rotate around cube center, not origin
    center = cube_offset
    rotated = (cube_vertices - center) @ R.T + center

    for line, e in zip(cube_lines, edges):
        p1, p2 = rotated[e[0]], rotated[e[1]]
        line.set_data([p1[0], p2[0]], [p1[1], p2[1]])
        line.set_3d_properties([p1[2], p2[2]])

    fig.canvas.draw_idle()

slider_x.on_changed(update)
slider_y.on_changed(update)
slider_z.on_changed(update)

plt.show()

