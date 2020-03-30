import urllib
import cv2,time
import numpy as np
first_frame = None

url= ’http://192.168.2.52:8080/shot.jpg’
imgResp = urllib.urlopen(url)
imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
img = cv2.imdecode(imgNp,-1)
cv2.namedWindow(‘image’,cv2.WINDOW_NORMAL)
cv2.resizeWindow(‘image’,600,600)

i=0
while True:
	imgResp=urllib.urlopen(url)
	imgNp=np.array(bytearray(imgResp.read()),dtype=n.uint8)
	img=cv2.imdecode(imgNp,-1)
	cv2.imshow(‘image’,img)
	cv2.imwrite(‘test.jpg’’,img)
	key=cv2.waitKey(1)
	if key==ord(‘q’):
		break

cv2.destroyAllWindows