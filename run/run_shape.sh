pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
pip install tqdm
cd processdata/shapedata/
#python mask_to_coco.py
cd ../../
#python tools/train.py 
rm -rf work_dirs/mask_rcnn_r50_fpn_1x_shape
#./tools/dist_train.sh configs/mask_rcnn_r50_fpn_1x_crertor.py 1 --validate
./tools/dist_train.sh configs/mask_rcnn_r50_fpn_1x_shape.py 1 --validate
#./tools/dist_train.sh configs/mask_rcnn_r50_fpn_1x.py 1
#python test/test_shape.py
#python outhtml.py
