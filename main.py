import cv2

img = cv2.imread('monitor-1.png', )

print(type(img))

for i in range(len(img)):
    for j in range(len(img)):
        if img[i, j][2] > 255:
            print(img[i, j])


cv2.waitKey(0)
