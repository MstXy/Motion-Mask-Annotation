from imantics import Polygons, Mask
import cv2
import json
import numpy as np
import sys

# merge:
import os


# DATA = "00"
# SEQ = "2"


fp = sys.argv[1]
DATA = sys.argv[2]
SEQ = sys.argv[3]

filepath = "{}/mask/{}/{}".format(fp, DATA, SEQ)
# filepath = "/home/zcy/data/4t_data/Track-anything-data/kitti-after-ta/mask/{}/{}".format(DATA, SEQ)
output_path = "{}/forlabelme/{}_{}".format(fp, DATA, SEQ)
# output_path =  "/home/zcy/data/4t_data/Track-anything-data/kitti-after-ta/forlabelme/{}_{}".format(DATA, SEQ)

cumulative_num_classes = 0

for segment in sorted(os.listdir(filepath)):
    # segment are segment folder names
    _start = int(segment.split("-")[0])
    print(segment)
    for mf in sorted(os.listdir(os.path.join(filepath, segment))):
        print(mf)
        mask = cv2.imread(os.path.join(filepath, segment, mf), 0)
        # mask2onehot
        label_path = "./txt-for-ta/{}_{}_{}.txt".format(DATA, SEQ, segment)
        label_file = open(label_path).readlines()
        num_classes = len(label_file)
        # need to remap label due to bugs in TrackAnything
        mapK = np.unique(mask)
        mapV = np.arange(num_classes+1)
        for key,val in zip(mapK,mapV):
            mask[mask==key] = val 
        _mask = np.array([mask == i for i in range(num_classes + 1)]).astype(np.uint8)
        all_point = []
        for i in range(1, _mask.shape[0]): # ignore background
            polygons = Mask(_mask[i]).polygons()
            if polygons.points:
                all_point.append({
                    "label": str(i + cumulative_num_classes),
                    "points": (polygons.points)[0].tolist()
                    })

        out_dict = {  
                        "version": "5.2.0.post4",
                        "flags": {},
                        "shapes" : all_point,
                        "imagePath": "{:06d}.png".format(_start + int(mf.split(".")[0])),
                        "imageData": None,
                        "imageHeight": 376,
                        "imageWidth": 1241
                    }

        if not os.path.exists(output_path):
            os.makedirs(output_path)

        with open(os.path.join(output_path, "{:06d}.json".format(_start + int(mf.split(".")[0]))), "w") as f:
            json.dump(out_dict, f, ensure_ascii=False, indent=2)

    cumulative_num_classes += num_classes