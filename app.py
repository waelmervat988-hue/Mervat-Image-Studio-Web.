import cv2
import matplotlib.pyplot as plt

# قراءة الصورة
img = cv2.imread("image.jpg")

# تحويل الصورة الى أبيض وأسود
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# عرض الصورة
plt.imshow(gray, cmap="gray")
plt.title("Processed Image")
plt.axis("off")
plt.show()