import os
from os import path as osp
import json
from PIL import Image,ImageDraw
from tqdm import tqdm
import cv2
import numpy as np
import shutil
def pil2cv(img):
    return cv2.cvtColor(np.array(img),cv2.COLOR_RGB2BGR)
def creatdir(dst): 
    if os.path.exists(dst):shutil.rmtree(dst) 
    os.makedirs(dst) 

def link_file(src, dst):
    os.system('ln -s %s %s' % (src, dst))   

root_path = '/data/coco'
img_root = osp.join(root_path,'images')
json_root = osp.join(root_path,'jsons')

annotations = 'train/annotations'
shapes_train2018 = 'train/shapes_train2018'
draw_root = 'train/draw'
#import pdb;pdb.set_trace()) 
creatdir(annotations)
creatdir(shapes_train2018)
creatdir(draw_root)


imgfiles = [imgfile for imgfile in os.listdir(img_root)]
for idx, filename in tqdm(enumerate(imgfiles)):
    json_name = osp.splitext(filename)[0]+'.json'
    json_path = osp.join(json_root,json_name)
    img_path = osp.join(img_root,filename)
    save_img = osp.join(shapes_train2018,'%06d'%idx+'.jpeg')#<image_id>.jpeg#<image_id>_<object_class_name>_<annotation_id>.png
    draw_path = osp.join(draw_root,filename)
    img = Image.open(img_path).convert('RGB')
    cv_img = pil2cv(img)
    width = img.width
    height = img.height
    
    result = json.loads(open(json_path).read())
    for num,shape in enumerate(result['label']['label_data']):
        save_mask = osp.join(annotations,'%06d'%idx+'_jiao_{}.png'.format(num))
        mask = Image.new ('RGB', (width, height), (0, 0, 0))
        draw_img = ImageDraw.Draw(mask)
        points = shape['paths']
        polygon = []
        for p in points:
            x = float(p['x'])
            y = float(p['y'])
            polygon.append(x * img.width)
            polygon.append(y * img.height)
        draw_img.polygon(polygon, fill=(255,255,255))
        cv_mask = pil2cv(mask)
        cv2.imwrite(save_mask,cv_mask)
        color_mask = np.random.randint(0, 256, (1, 3), dtype=np.uint8)
        #import pdb;pdb.set_trace()
        b_mask  = np.array(cv_mask[:,:,0]==255)
        cv_img[b_mask] = cv_img[b_mask] * 0.5 + color_mask * 0.5
        contours,hierarchy = cv2.findContours(cv_mask[:,:,0],cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
        for cidx,cnt in enumerate(contours):
            (x, y, w, h) = cv2.boundingRect(cnt)
            cv2.rectangle(cv_img, pt1=(x, y), pt2=(x+w, y+h),color=(0, 0, 255), thickness=3)
            cv2.putText(cv_img,str(num),(x, y),cv2.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    #cv_img = pil2cv(img)
    cv2.imwrite(draw_path,cv_img)
    link_file(img_path,save_img)
