import cv2
import urllib.request
import numpy as np

# image URL
url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmwla6vUQK67X5KHksARyVrL4Evo509hBcCA&s"

# Reading data from URL
resp = urllib.request.urlopen(url)
image_data = np.asarray(bytearray(resp.read()), dtype="uint8")

# Decode the data in OpenCV
img = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

# Show image
if img is None:
    print("❌ Error: Could not load image from URL")
else:
    cv2.imshow("output", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows() 
