import json
import os

filepath = "/home/zcy/data/4t_data/Track-anything-data/kitti-after-ta/forlabelme/00_3"

for file in sorted(os.listdir(filepath)):
    if file.endswith(".json"):
        with open(os.path.join(filepath, file)) as f:
            j = json.load(f)
            j["imageData"] = None
        os.remove(os.path.join(filepath, file))
        with open(os.path.join(filepath, file), 'w') as f:
            json.dump(j, f, indent=4)
