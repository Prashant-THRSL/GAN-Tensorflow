import glob
import os

import numpy as np


# ==============================================================================
# =                                    run                                     =
# ==============================================================================

img_paths = glob.glob(os.path.join('Specs_NoSpecs', '*.png'))
img_lbl_files = [img_path.replace('.png', '.csv') for img_path in img_paths]

img_lbls = []
for img_path, img_lbl_file in zip(img_paths, img_lbl_files):
    img_lbl = np.genfromtxt(img_lbl_file, dtype=int, usecols=1, delimiter=',')

    glasses = img_lbl[0] if img_lbl[0] <= 1 else -1  

    one_hot_mapping = {0: [1, 0],
                       1: [0, 1],
                       -1: [0, 0]}
    
    glasses = one_hot_mapping[glasses]

    img_lbl = np.concatenate((glasses), axis=0)
    img_lbls.append(img_lbl)


def save_lbl(img_paths, img_lbls, save_path):
    with open(save_path, 'w') as f:
        for img_path, img_lbl in zip(img_paths, img_lbls):
            f.write(os.path.split(img_path)[-1])
            for lbl in img_lbl:
                f.write(' %d' % (lbl * 2 - 1))
            f.write('\n')

save_lbl(img_paths[:8000], img_lbls[:8000], 'train_label.txt')
save_lbl(img_paths[8000:9000], img_lbls[8000:9000], 'val_label.txt')
save_lbl(img_paths[9000:], img_lbls[9000:], 'test_label.txt')
