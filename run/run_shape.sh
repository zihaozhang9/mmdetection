pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
pip install tqdm
cd processdata/shapedata/
bash process.sh
cd ../../
#rm -rf work_dirs/mask_rcnn_r50_fpn_1x_shape
#tools/dist_train.sh configs/my/mask_rcnn_r50_fpn_1x_shape.py 1 --validate
python tools/train.py configs/my/mask_rcnn_r50_fpn_1x_shape.py
cd test
python test_shape.py
cd ../
#cd show
#python out_shape.py
#cd ../
