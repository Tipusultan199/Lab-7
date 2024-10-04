import numpy as np
import matplotlib.pyplot as plt

# Set print options to avoid scientific notation
np.set_printoptions(suppress=True)

# Angles in radians
theta_1 = np.radians(0)
theta_2 = np.radians(0)
theta_3 = np.radians(0)
theta_4 = np.radians(0)

# Rotation matrix for Z-axis (theta_1)
rot_z_theta_1 = np.array([[np.cos(theta_1), -np.sin(theta_1), 0],
                          [np.sin(theta_1), np.cos(theta_1), 0],
                          [0, 0, 1]])

# Rotation matrix for Y-axis (theta_2, theta_3, theta_4)
rot_y_theta_2 = np.array([[np.cos(theta_2), 0, np.sin(theta_2)],
                          [0, 1, 0],
                          [-np.sin(theta_2), 0, np.cos(theta_2)]])

rot_y_theta_3 = np.array([[np.cos(theta_3), 0, np.sin(theta_3)],
                          [0, 1, 0],
                          [-np.sin(theta_3), 0, np.cos(theta_3)]])

rot_y_theta_4 = np.array([[np.cos(theta_4), 0, np.sin(theta_4)],
                          [0, 1, 0],
                          [-np.sin(theta_4), 0, np.cos(theta_4)]])

# Identity matrix for the base frame
eye = np.eye(3)

# Tool frame w.r.t the base frame
rot_0_5 = eye @ rot_z_theta_1 @ rot_y_theta_2 @ rot_y_theta_3 @ rot_y_theta_4

# Print the final rotation matrix
print("Final Rotation Matrix (Tool Frame w.r.t Base Frame):")
print(rot_0_5)

# Extract the coordinate frame axes (x, y, z) from the rotation matrix
x_axis = rot_0_5[:, 0]  # X-axis (first column)
y_axis = rot_0_5[:, 1]  # Y-axis (second column)
z_axis = rot_0_5[:, 2]  # Z-axis (third column)

# Create vectors for the origin and axes
origin = np.zeros(3)

# Visualize the coordinate frame using matplotlib
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the X, Y, Z axes
ax.quiver(*origin, *x_axis, color='r', label='X-axis')
ax.quiver(*origin, *y_axis, color='g', label='Y-axis')
ax.quiver(*origin, *z_axis, color='b', label='Z-axis')

# Set the axis limits and labels
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_zlim(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.legend()

# Show the plot
plt.show()
