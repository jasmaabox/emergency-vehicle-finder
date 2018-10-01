import pandas as pd
import os
from os.path import relpath

import cv2

def test_img(img_path, rect):
    """Draws boundaries on image"""
    rect = list(map(int, rect))
    img = cv2.imread(img_path)
    for i in range(int(len(rect)/4)):
        img = cv2.rectangle(img,(rect[0+4*i],rect[1+4*i]),(rect[0+4*i]+rect[2+4*i],rect[1+4*i]+rect[3+4*i]),(0,255,0),3)
    cv2.imshow(img_path, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

dir_path = os.path.dirname(os.path.realpath(__file__))

labels = pd.read_csv('labels.csv')
imgs = pd.read_csv('img_paths.csv')

# Write matlab csv data to info format
out_list = []
for i, row in labels.iterrows():
    fname = imgs.Var1[i]
    fname = relpath(fname, dir_path)

    vals = list(map(lambda x: str(int(x-1)), (row.dropna()).tolist()))
    num = int(len(vals)/4)

    if num == 0:
        continue

    # convert matlab to opencv info format
    fixed_vals = []
    for i in range(1, num+1):
        for j in range(i-1, len(vals), num):
            fixed_vals.append(vals[j])
    vals = fixed_vals

    fin_list = [fname, str(num)] + vals

    out_list.append(" ".join(fin_list))

with open('info.lst', 'w') as f:
    f.write('\n'.join(out_list))
    f.close()
