## Motion mask annotation

### Step 0: Close Proxy

NEED to close network proxy in settings. Turn Network Proxy to Disabled from Manual.



### Step 1: Set up Track Anything

Run the following:

```shell
conda activate track-anything
cd /home/hulz/labelData/Track-Anything
python app.py --device cuda:0 

#default: --kittidir '/home/hulz/data/win_id4_share/KITTI' --outputdir '/home/hulz/labelData/Track-anything-data/kitti-after-ta'
```



### Step 2: Prepare files for video segments

In folder: `txt-for-ta`, name the file as: `$xx_$y_$aaaa-$bbbb.txt` for each video segments.

- `$xx` is the data folder name under KITTI, e.g. `00`,`01`,`02`...
- `$y` denotes the subfolder name, `2` for `image_2` and `3` for `image_3`
- `$aaaa` is the start frame number and `$bbbb` is the end frame number, e.g. `0000-0108` means from the first frame to frame 108.

Check the data `$xx/image_$y` and put the video segments of new objects into a new `.txt` file.

In the `.txt` file, put the name of the instances into each line such as the as following:

```txt
1, person
2, person
3, person
```

注意：
这里的video segment指的是单个或一组移动物体从出现到消失的时间段，如一段时间里一辆车从对面开过一直到消失。

如果新运动物体连续不断出现，由于track anything限制，只能标完后手动在labelme中改标签。



### Step 3: Use Track Anything

*KITTI data file path: `$KITTIDIR/odometry/dataset/sequences/$xx/image_$y`*

Upload the `.txt` file and do annotations for each video segments separately.

Refer to [original tutorial](https://github.com/gaomingqi/Track-Anything/blob/master/doc/tutorials.md)

Additionals:

For each of the video segments, you can reverse the whole sequence and do annotations reversely, as it might be easier for closing in objects.

Mask will be saved at: `/home/hulz/labelData/Track-anything-data/kitti-after-ta/mask/$xx/$y/$aaaa-$bbbb`




### Step 4: Convert mask to LabelMe

After finishing the **WHOLE** sequence.

Run the following in terminal:

```shell
conda activate track-anything
cd /home/hulz/labelData/
python mask2labelme.py $xx $y

# change $xx,$y to same as defined above
```



### Step 5: Use AnyLabeling to tweak mask

https://github.com/vietanhdev/anylabeling


Copy all KITTI data under folder: `$KITTIDIR/odometry/dataset/sequences/$xx/image_$y` to `$OUTPUTDIR/forlabelme/$xx_$y`

Can use the command `cp -r $KITTIDIR/odometry/dataset/sequences/$xx/image_$y/* /home/hulz/labelData/Track-anything-data/kitti-after-ta/forlabelme/$xx_$y/`

Open AnyLabeling: 

```shell
conda activate anylabeling
anylabeling
```

Then click `Open Dir` button and open the folder `/home/hulz/labelData/Track-anything-data/kitti-after-ta/forlabelme/$xx_$y`.

Do necessary modification to the annotations. Fix some missing annotations.

**Auto Labeling:**

Click the brain icon at the left bottom, Load `Segment Anything (ViT-H Quant)` model 

Click `+Point` and `-Point` for point prompts, `F` to finish and assign label.

Tweak afterwards.


*For right eye view, you could duplicate the label json files to another folder e.g. `00_3` and use AnyLabeling to tweak*


对于从远处靠近的物体，或是远离的物体，从可以明确辨别物体轮廓开始标注，像素点过少或过于模糊的情况就略过。




