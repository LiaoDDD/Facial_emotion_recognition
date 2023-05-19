import cv2
from deepface import DeepFace
import numpy as np
from PIL import ImageFont, ImageDraw, Image



# 定義加入文字函式
def putText(x,y,text,size=100,color=(255,255,255)):
    global img
    font = ImageFont.load_default() 
    fontpath = 'NotoSansTC-Regular.otf'            # 字型
    font = ImageFont.truetype(fontpath, size)      # 定義字型與文字大小
    imgPil = Image.fromarray(img)                  # 轉換成 PIL 影像物件
    draw = ImageDraw.Draw(imgPil)                  # 定義繪圖物件
    draw.text((x, y), text_obj[text], fill=color, font=font) # 加入文字
    img = np.array(imgPil)                         # 轉換成 np.array


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("xml/haarcascade_frontalface_default.xml")   # 載入人臉模型

if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    if not ret:
        print("Cannot receive frame")
        break
    img = cv2.resize(frame,(1000,800)) 
    

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # 將鏡頭影像轉換成灰階
    faces = face_cascade.detectMultiScale(gray)      # 偵測人臉

    for (x, y, w, h) in faces:
    # 擴大偵測範圍，避免無法辨識情緒
        x1 = x-60
        x2 = x+w+60
        y1 = y-20
        y2 = y+h+60
        face = img[x1:x2, y1:y2]  # 取出人臉範圍
        try:
            analyze = DeepFace.analyze(img, actions=['emotion'])
            emotion = analyze['dominant_emotion']  # 取得情緒文字
            print(analyze)
            #putText(0,40,emotion) 
            cv2.putText(img, emotion, (x,y-5),cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)                 # 放入文字
        except:
            pass
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 5)
        
    cv2.imshow('G11116015', img)
    if cv2.waitKey(5) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()