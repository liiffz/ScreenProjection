import random 
import numpy as np
import cv2
import mss
from PIL import Image

##眼动轨迹数据文件
##f=open("data.txt","r")

##设置截图区域
mon = {'top': 60, 'left': 60, 'width': 300, 'height': 300}
sct =mss.mss()
while 1:
    ##从文本文档中读取
    ##note=f.readline().split()
    ##实时读取
    note=[]
    a=random.randint(70,450)
    b=random.randint(70,450)
    note.append(a)
    note.append(b)
    ##对坐标进行映射
    ##.....

    ##截屏
    sct_img=sct.grab(mon)
    img = Image.frombytes('RGB', (sct_img.width, sct_img.height), sct_img.rgb)
    img=np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    ##绘图
    cv2.circle(img,(int(note[0]),int(note[1])),10,(0,0,213))
    cv2.imshow('test', img)
    
    ##设置频率
    if cv2.waitKey(25) & 0xFF == ord('q'):  
        cv2.destroyAllWindows()
        break




##
##图像流实现屏幕共享
##频率一致实现轨迹标注 
