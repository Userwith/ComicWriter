import os
import pandas
import cv2
class FileLoader:
    def __init__(self,path):
        self.path = path
        self.file_name_list = os.listdir(path)
    def __len__(self):
        return self.file_name_list.__len__()
    def imread(self,name):
        try:
            return cv2.imread(self.path+name)
        except:
            print("There is no that image")
        return 0

    def imread_gray(self, name):
        try:
            return cv2.imread(self.path + name,cv2.IMREAD_GRAYSCALE)
        except:
            print("There is no that image")
        return 0

if __name__ == "__main__":
    a = FileLoader("../dataset/")
    img = a.imread_gray("test.jpg")
    cv2.imshow("img",img)
    cv2.waitKey()





