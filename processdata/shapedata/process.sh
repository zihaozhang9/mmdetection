pip install git+git://github.com/waspinator/pycococreator.git@0.2.0
pip install tqdm
wget https://patrickwasp.com/wp-content/uploads/2018/04/shapes_train_dataset.zip
unzip shapes_train_dataset.zip
rm -rf __MACOSX
rm -rf  shapes/train/annotations/instances_shape_train2018.json
rm -rf  shapes/train/shapes_train2018/.DS_Store

python mask_to_coco.py
