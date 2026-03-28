import cv2
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
from skimage import exposure
import numpy as np

# 1. استخدام OpenCV لقراءة الصورة الأساسية
img = cv2.imread("image.jpg")
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # تحويل الألوان لتناسب العرض

# 2. استخدام OpenCV لتحويل الصورة لرمادي (Gray)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. استخدام Scikit-image لتحسين تباين الصورة (Equalization)
# ده بيخلي تفاصيل الصورة واضحة جداً بشكل احترافي
enhanced_img = exposure.equalize_hist(gray_img)

# 4. استخدام Pillow للكتابة على الصورة
# بنحول مصفوفة OpenCV لصورة Pillow عشان نعرف نكتب عليها
pil_img = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
draw = ImageDraw.Draw(pil_img)
# بنكتب النص (ملاحظة: لو مفيش ملف خط، هيكتب بخط افتراضي)
draw.text((20, 20), "Designed by MERVAT", fill=(255, 255, 255))
final_pillow_img = np.array(pil_img)

# 5. استخدام Matplotlib لعرض النتائج كلها في لوحة واحدة
plt.figure(figsize=(15, 5))

plt.subplot(1, 4, 1)
plt.imshow(img_rgb)
plt.title("Original (OpenCV)")
plt.axis("off")

plt.subplot(1, 4, 2)
plt.imshow(gray_img, cmap='gray')
plt.title("Gray Scale (OpenCV)")
plt.axis("off")

plt.subplot(1, 4, 3)
plt.imshow(enhanced_img, cmap='gray')
plt.title("Enhanced (Scikit-Image)")
plt.axis("off")

plt.subplot(1, 4, 4)
plt.imshow(final_pillow_img)
plt.title("With Text (Pillow)")
plt.axis("off")

plt.show()