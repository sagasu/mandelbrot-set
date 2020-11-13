import matplotlib.pyplot as plt
import numpy as np
 
image_x = 400
image_y = 300

mesh_x = np.linspace(-2.5, 1.5, num = image_x +1)
mesh_y = np.linspace(-1.5, 1.5, num = image_y +1)

image = np.zeros((len(mesh_y), len(mesh_x)))

for i, y in enumerate(mesh_y):
    for j, x in enumerate(mesh_x):
        cr, ci = x, y
        zr, zi = 0, 0

        count = 0
        isInside = True
        while count <= 50:
            count = count + 1
            z_mod_sq = zr * zr + zi*zi
            if z_mod_sq > 4:
                isInside = False
                break
            zr, zi = (zr*zr - zi*zi + cr), (2*zr*zi + ci)

        if(isInside):
            image[i][j] = 1

plt.imshow(image)
plt.show()
