import cv2
import sys
import numpy as np
import seam_carving # 설치 : pip install seam-carving

img = cv2.imread('../data/beach.jpg')
if img is None :
    sys.exit('파일을 찾을 수 없습니다.')

h,w,c = img.shape

#girl_mask = cv2.imread("../data/beach_girl.png", cv2.IMREAD_GRAYSCALE)  # keep_mask에 사용, 보호할 영역

# 가로로 길게
dst1 = seam_carving.resize(
    img,  # input image (rgb or gray)
    size=(w+200, h),  # target size
    energy_mode="backward",  # choose from {backward, forward}
    order="width-first",  # choose from {width-first, height-first}
    keep_mask=None  # object mask to protect from removal
)

# 가로로 짧게
dst2 = seam_carving.resize(
    img,  # input image (rgb or gray)
    size=(w-200, h),  # target size
    energy_mode="backward",  # choose from {backward, forward}
    order="width-first",  # choose from {width-first, height-first}
    keep_mask=None,  # object mask to protect from removal
)

# 세로로 길게
dst3 = seam_carving.resize(
    img,  # input image (rgb or gray)
    size=(w, h+80),  # target size
    energy_mode="backward",  # choose from {backward, forward}
    order="height-first",  # choose from {width-first, height-first}
    keep_mask=None # object mask to protect from removal
)

# 세로로 짧게
dst4 = seam_carving.resize(
    img,  # input image (rgb or gray)
    size=(w, h-80),  # target size
    energy_mode="backward",  # choose from {backward, forward}
    order="height-first",  # choose from {width-first, height-first}
    keep_mask=None,  # object mask to protect from removal
)

padding = np.full((h, 8, c), 255, dtype=np.uint8)
img_carved1 = np.hstack((img, padding, cv2.resize(img,dsize=(w+200,h)), padding, dst1))
img_carved2 = np.hstack((img, padding, cv2.resize(img,dsize=(w-200,h)), padding, dst2))
cv2.imshow('Seam Carving - resizing h+', img_carved1)
cv2.imshow('Seam Carving - resizing h-', img_carved2)

padding2 = np.full((8, w, c), 255, dtype=np.uint8)
img_carved3 = np.vstack((img, padding2, cv2.resize(img,dsize=(w,h+200)), padding2, dst3))
img_carved4 = np.vstack((img, padding2, cv2.resize(img,dsize=(w,h-200)), padding2, dst4))
#cv2.imshow('Seam Carving - resizing v+', img_carved3)
#cv2.imshow('Seam Carving - resizing v-', img_carved4)

cv2.waitKey()
cv2.destroyAllWindows()
