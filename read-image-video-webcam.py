import cv2
print("package imported")

img = cv2.imread("/Users/mithunkumar/Documents/Pics/MithChildhood.jpg")

cv2.imshow("Output", img)
cv2.waitKey(0)

cap = cv2.VideoCapture("")
