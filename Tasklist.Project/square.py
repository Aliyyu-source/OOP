import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 (needed for 3D)

# --- Square definition (centered at origin in XY plane) ---
square_pts = np.array([
    [-1, -1, 0],
    [ 1, -1, 0],
    [ 1,  1, 0],
    [-1,  1, 0],
    [-1, -1, 0],  # close the loop
])

def rotation_matrix_z(theta_deg):
    theta = np.deg2rad(theta_deg)
    c, s = np.cos(theta), np.sin(theta)
    return np.array([
        [ c, -s, 0],
        [ s,  c, 0],
        [ 0,  0, 1]
    ])

# --- Figure and 3D axes setup ---
fig = plt.figure(figsize=(7, 7))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(bottom=0.2)  # leave space for slider

# Axis limits
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_zlim(-3, 3)

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Rotate Square in 3D')

# Draw main axes lines
ax.plot([-3, 3], [0, 0], [0, 0], color='black', linewidth=1)  # X-axis
ax.plot([0, 0], [-3, 3], [0, 0], color='black', linewidth=1)  # Y-axis
ax.plot([0, 0], [0, 0], [-3, 3], color='gray', linewidth=1)   # Z-axis (optional)

# Add points along X and Y axes
x_points = np.linspace(-2.5, 2.5, 6)
y_points = np.linspace(-2.5, 2.5, 6)

ax.scatter(x_points, np.zeros_like(x_points), np.zeros_like(x_points),
           color='red', s=30, label='X-axis points')
ax.scatter(np.zeros_like(y_points), y_points, np.zeros_like(y_points),
           color='blue', s=30, label='Y-axis points')

ax.legend(loc='upper left')

# Initial square plot (will be updated)
rot_mat = rotation_matrix_z(0)
square_rot = square_pts @ rot_mat.T
square_line, = ax.plot(square_rot[:, 0], square_rot[:, 1], square_rot[:, 2],
                       color='green', linewidth=2)

# --- Slider for rotation angle ---
ax_angle = plt.axes([0.2, 0.05, 0.6, 0.03])  # [left, bottom, width, height]
angle_slider = Slider(ax_angle, 'Angle (deg)', 0, 360, valinit=0, valstep=1)

def update(angle):
    rot = rotation_matrix_z(angle)
    sq = square_pts @ rot.T
    square_line.set_data(sq[:, 0], sq[:, 1])
    square_line.set_3d_properties(sq[:, 2])
    fig.canvas.draw_idle()

angle_slider.on_changed(update)

plt.show()

