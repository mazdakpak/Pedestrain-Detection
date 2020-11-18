#github.com/mazzdakpak
#import needed modules
import cv2
import imutils
#init the HOG person
#detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
#get img by the user
img = str(input("Path to img => "))

#Reading the image
image = cv2.imread(img)

#Resizing the image
image = imutils.resize(image , width=min(400 , image.shape[1]))

#Detecting all the regions in the 
#image that has pedestrain inside it
(regions , _)= hog.detectMultiScale(image, winStride=(4,4)  , padding=(4,4) , scale=1.05)

#Drawing regions in the image 
for (x, y , w ,h ) in regions:
    cv2.rectangle(image , (x,y), (x+w , y+h)  , (0,0,255) , 2)

#Showing the output image
cv2.imshow("Image" , image)
cv2.waitKey(0)
cv2.destroyAllWindows()
#github.com/mazdakpak