pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
pip install tqdm
cd processdata/coco
bash process.sh
cd ../../
rm -rf work_dirs/mask_rcnn_r50_fpn_1x
./tools/dist_train.sh configs/mask_rcnn_r50_fpn_1x.py 1 #--resume_from work_dirs/mask_rcnn_r50_fpn_1x/latest.pth  #--validate
python test/test.py
python show/out.py
