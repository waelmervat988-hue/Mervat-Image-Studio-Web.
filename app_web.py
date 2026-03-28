from flask import Flask, render_template, request
import cv2
import os
import numpy as np
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    f1 = request.files.get('file1')
    f2 = request.files.get('file2')
    filter_type = request.form.get('filter')

    if f1:
        path1 = os.path.join(app.config['UPLOAD_FOLDER'], "img1.jpg")
        f1.save(path1)
        img = cv2.imread(path1)

        if filter_type == 'gray':
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        elif filter_type == 'sepia':
            kernel = np.array([[0.272, 0.534, 0.131], [0.349, 0.686, 0.168], [0.393, 0.769, 0.189]])
            img = cv2.transform(img, kernel)
        
        elif filter_type == 'invert':
            img = cv2.bitwise_not(img) # عكس الألوان
            
        elif filter_type == 'edges':
            img = cv2.Canny(img, 100, 200) # كشف الحواف
            
        elif filter_type == 'bright':
            matrix = np.ones(img.shape, dtype="uint8") * 50
            img = cv2.add(img, matrix) # زيادة الإضاءة
            
        elif filter_type == 'merge' and f2:
            path2 = os.path.join(app.config['UPLOAD_FOLDER'], "img2.jpg")
            f2.save(path2)
            img2 = cv2.imread(path2)
            if img2 is not None:
                img2 = cv2.resize(img2, (img.shape[1], img.shape[0])) # توحيد الحجم
                img = cv2.addWeighted(img, 0.5, img2, 0.5, 0) # دمج 50% لكل صورة

        final_name = "mervat_result.jpg"
        final_path = os.path.join(app.config['UPLOAD_FOLDER'], final_name)
        cv2.imwrite(final_path, img)
        
        return render_template('index.html', filename=final_name, salt=time.time())

    return "يرجى اختيار الصور!"

if __name__ == '__main__':
    app.run(debug=True)