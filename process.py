import cv2
import numpy as np
from PIL import Image


class Process:
    def __init__(self, image, back_image, hl=35, hu=85, sl=0, su=255, vl=0, vu=255):
        self.image = image
        self.back_image = back_image
        self.hl = hl
        self.hu = hu
        self.sl = sl
        self.su = su
        self.vl = vl
        self.vu = vu

    def get_image(self, img):
        img = np.asarray(img)
        img_siz = self.img_size()
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, img_siz, interpolation=cv2.INTER_AREA)
        return img

    def img_size(self):
        img = np.asarray(self.image)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img.shape[1], img.shape[0]

    def remove_back(self):
        img = self.get_image(self.image)
        hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
        lower = (self.hl, self.sl, self.vl)
        upper = (self.hu, self.su, self.vu)
        mask = cv2.inRange(hsv_img, lower, upper)
        masked_img = img.copy()
        masked_img[mask != 0] = [0, 0, 0]
        return masked_img

    def join_image(self):
        masked_img = self.remove_back()
        back_img = self.get_image(self.back_image)
        bitwise_or = cv2.bitwise_or(masked_img, back_img)
        return Image.fromarray(bitwise_or)
