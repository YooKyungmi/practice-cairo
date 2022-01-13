import cv2
from shapely.geometry import Polygon
import numpy as np
import geopandas as gpd

img = cv2.imread('coco.png')
#img=cv2.resize(img,dsize=(0,0),fx=1.5,fy=1.5,interpolation=cv2.INTER_LINEAR) #확인하려고 사진 크기 조절
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold를 이용하여 binary image로 변환
ret, thresh = cv2.threshold(imgray,170,255,0)

#contours는 point의 list형태. 예제에서는 사각형이 하나의 contours line을 구성하기 때문에 len(contours) = 1. 값은 사각형의 꼭지점 좌표.
#hierachy는 contours line의 계층 구조
contours, hierachy = cv2.findContours(thresh, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
image = cv2.drawContours(img, contours, -1, (0,255,0), 1)

cv2.imshow('image', image)
poly_objs = []
for i in range(len(contours)):                                #여기가 벡터화
    if (i > 0) and (len(contours[i]))>2:
        poly_objs.append(Polygon(np.squeeze(contours[i])))   #1차원 배열로 만든 후 리스트에 추가

polygons = poly_objs
polygons = gpd.GeoDataFrame(polygons, columns = ['geometry'])
polygons.to_file('coco1.svg')
cv2.waitKey(0)