pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
pip install tqdm
cd processdata/shapedata/
#python process.py
cd ../../
#python tools/train.py 
rm -rf work_dirs/mask_rcnn_r50_fpn_1x_shape
./tools/dist_train.sh configs/mask_rcnn_r50_fpn_1x_shape.py 1 #--resume_from work_dirs/mask_rcnn_r50_fpn_1x_shape/latest.pth --validate
#python test/test_shape.py
#python outhtml.py
