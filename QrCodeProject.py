import cv2
import numpy as np
from pyzbar.pyzbar import decode

# img = cv2.imread('Student.jpg')
cap = cv2.VideoCapture(0)

cap.set(3, 640)
cap.set(4, 480)

with open('myDataFile.txt') as f:
    # każda linia będzie odczytana i dodana do listy na bazie linii jako podziału nowej rzeczyw  liście
    myDataList = f.read().splitlines()
    print(myDataList)


while True:

    success, img = cap.read()
    for barcode in decode(img):
        #Przerobić kod z bytów - z literką b na samą liczbę
        myData = barcode.data.decode('utf-8')
        print(myData)
        #Jeśli jest w pliku myDataFile to authirized else un-authorized
        if myData in myDataList:
            myOutput = 'Authorized'
            myColor = (0,255,0)
        else:
            myOutput = 'Un-Authorized'
            myColor = (0, 0, 255)
        #Rozpoczęcie pracy nad kwadratem
        pts = np.array([barcode.polygon], np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(img, [pts], True, myColor, 5)
        pts2 = barcode.rect
        #Dodanie tekstu do kwadratu wraz z czcionką i kolorem
        cv2.putText(img, myOutput, (pts2[0], pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, myColor, 2)

    cv2.imshow('Result', img)
    key = cv2.waitKey(1)

    if key==81 or key==113:
        break