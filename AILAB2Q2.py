import numpy as np
import matplotlib.pyplot as plt

import os
print("Current Working Directory:", os.getcwd())
with open("genome.txt", "r") as file:
    genome_sequence = file.read().strip()  


genome_list = list(genome_sequence)
genome_length = len(genome_list)


t = np.linspace(0, 4 * np.pi, genome_length)  # Generates 't' values for 2 turns
x = np.cos(t)  # X-coordinates using cosine function
y = np.sin(t)  # Y-coordinates using sine function
z = np.linspace(0, 5, genome_length)  # Z-coordinates to create vertical spread


color_map = {'A': 'red', 'T': 'blue', 'C': 'green', 'G': 'yellow'}
colors = [color_map.get(base, 'black') for base in genome_list]  


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')


ax.scatter(x, y, z, c=colors, marker='o')


ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
ax.set_title("3D Helix Structure of Genome Sequence")


plt.show()
