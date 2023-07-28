#!/bin/bash
for i in {0..21}
do
  zip -r /home/zcy/data/4t_data/Track-anything-data/kitti-raw-zip/0${i}_image2.zip /home/zcy/data/win_id4_share/KITTI/odometry/dataset/sequences/0$i/image_2
  zip -r /home/zcy/data/4t_data/Track-anything-data/kitti-raw-zip/0${i}_image3.zip /home/zcy/data/win_id4_share/KITTI/odometry/dataset/sequences/0$i/image_3
done