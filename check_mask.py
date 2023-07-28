import cv2
import numpy as np
import matplotlib.pyplot as plt
'''
two backends
'tf' # for tesnorflow
'np' # for numpy/pytorch
'''
mask = cv2.imread('/home/zcy/data/4t_data/Track-anything-data/kitti-after-ta/mask/00/2/0631-0655/00000023.png', 0)
print(np.unique(mask))
plt.imshow(mask)
plt.show()

