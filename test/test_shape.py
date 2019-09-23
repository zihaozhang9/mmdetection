from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
import os
from os import path as osp
import shutil
#import pdb;pdb.set_trace()
def create_dir(dst):
    if os.path.exists(dst):shutil.rmtree(dst) 
    os.makedirs(dst) 
def show_image(model,imgpath,savepath):
    result = inference_detector(model, imgpath)
    show_result(imgpath, result, model.CLASSES, out_file=savepath)
def show_images(model,imgdir,savedir):
    for imgname in os.listdir(imgdir):
        imgpath = osp.join(imgdir,imgname)
        savepath = osp.join(savedir,imgname)
        show_image(model,imgpath,savepath)

config_file = '/mmdetection/configs/mask_rcnn_r50_fpn_1x_shape.py'
checkpoint_file ='/mmdetection/work_dirs/mask_rcnn_r50_fpn_1x_shape/latest.pth'#'epoch_2.pth'
img_root = '/data/shape/shapes_train2018/'
save_path = '/mmdetection/test/outputs_shape'
create_dir(save_path)

model = init_detector(config_file, checkpoint_file, device='cuda:0') 
#img = 'pycococreator/examples/shapes/train/shapes_train2018/1000.jpeg' 
#show_image(model,imgpath,save_path+'/1000.jpeg')
show_images(model,img_root,save_path)



