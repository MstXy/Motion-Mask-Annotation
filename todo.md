### TODO

1. LabelMe
    - check data format
        - poly shape
    - check if could import & modify mask ??
        - can, but need the annotation file to be under the SAME name as the image file. # line 1943 of `app.py`
    - mask to poly: https://github.com/wkentaro/labelme/issues/806 
        - coco2labelme" https://gist.github.com/travishsu/6efa5c9fb92ece37b4748036026342f6 
2. SAM
3. TAM
    - save masks: https://github.com/gaomingqi/Track-Anything/issues/26 
        - but format is `.npy`, or `.png`/`.jpeg`, 
    - Cannot detect multiple objects from different start frame.
        - Workarounds: manually separate video into segments.
    - Backward track??
        - cannot!


4. SAM /w labelme
    - https://github.com/wkentaro/labelme/pull/1262

5. Label anything, label studio with sam
```shell
cd path/to/playground/label_anything

label-studio-ml start sam --port 8003 --with \
  sam_config=vit_h \
  sam_checkpoint_file=./sam_vit_h_4b8939.pth \
  out_mask=True \
  out_bbox=True \
  device=cuda:0
# device=cuda:0 is for using GPU inference. If you want to use CPU inference, replace cuda:0 with cpu.
# out_poly=True returns the annotation of the bounding polygon.
```

### WorkFlow
1. create txt files, multiple for one data folder
2. Reverse?
3. label and track
4. merge into one?
5. mask2labelme
6. open in labelme
7. labelme2coco / labelme2voc / labelme2png ***not yet checked***





### Existing bugs

> ValueError: setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (4541,) + inhomogeneous part.

**Solution:** [known bug, not fixed] drag slider to the beginning, clear marks, reclick `Tracking`.




# Issues in 00_2

589