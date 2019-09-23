import os
import cv2
import shutil
#import pdb;pdb.set_trace()
def process(rootPath,savePath):
    if os.path.exists(savePath): shutil.rmtree(savePath) 
    os.makedirs(savePath)
    imgList = [i for i in os.listdir(rootPath) ]#if i.endswith('.bmp')]
    for idx,imgName in enumerate(imgList):
        img = cv2.imread(os.path.join(rootPath,imgName))
        #w = h = 1024
        #img_width,img_height = img.shape[1],img.shape[0]
        #scale = float(w)/max(img_width,img_height)
        #height = int(img_height * scale)
        #width = int(img_width * scale)        
        #img = cv2.resize(img,(width, height))
        cv2.imwrite(os.path.join(savePath,imgName),img)

def out2html(rootPath):
    f = open('out.html','w')
    f.close()
    imgList = [i for i in os.listdir(rootPath) ]#if i.endswith('.bmp')]
    #import pdb;pdb.set_trace()
    for idx,imgName in enumerate(imgList):
        f = open('out.html','a')
        wstr = '<tr><td><img src="'+os.path.join(rootPath,imgName)+'"></img></td></tr>\r\n'
        f.write(wstr)
        f.close()
        if idx>100:
            break
    print(idx+1)

def out2html2(rootPath,rootPath2):
    f = open('out.html','w')
    f.close()
    imgList = [i for i in os.listdir(rootPath) ]#if i.endswith('.bmp')]
    #import pdb;pdb.set_trace()
    for idx,imgName in enumerate(imgList):
        f = open('out.html','a')
        imgPath1 = os.path.join(rootPath,imgName)
        imgPath2 = os.path.join(rootPath2,imgName)
        wstr = '<tr><td><img src="'+imgPath1+'"></img><img src="'+imgPath2+'"></img></td></tr><br>\r\n'
        f.write(wstr)
        f.close()
        if idx>100:
            break
    print(idx+1)
rootPath = '/data/jiao/images/'
rootPath2= 'test/outputs_jiao'
savePath = 'tmpdata/draws/'
#process(rootPath,savePath)
out2html(rootPath2)
#savePath = ''
#out2html2(savePath,rootPath2)
