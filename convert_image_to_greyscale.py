import cv2


# import image from same directory as python script
image = cv2.imread('test.jpg')

# set scaling factor (large images wouldnt be displayed correctly without this)
scaling_factor = 6
image_scaled = cv2.resize(image, (int(image.shape[1]/scaling_factor), int(image.shape[0]/scaling_factor)))
# create grey_scale version
grey_scaled = cv2.cvtColor(image_scaled, cv2.COLOR_BGR2GRAY)

# show both images
cv2.imshow("Original", image_scaled) 
cv2.imshow('Gray image', grey_scaled)

# permanently save greyscale version in current folder
cv2.imwrite('grey_version.jpg', grey_scaled) 

# close both image previews if any key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
