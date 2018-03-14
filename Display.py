from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_Display import Ui_Display
import sys
import cv2
import numpy as np


class Display(QWidget):
    def __init__(self, parent=None):
        super(Display, self).__init__(parent)
        self.ui = Ui_Display()
        self.ui.setupUi(self)
        self.init_slot()
        self.load_img()

    def init_slot(self):
        self.ui.horizontalSlider_1.valueChanged[int].connect(self.changevalue)
        self.ui.horizontalSlider_2.valueChanged[int].connect(self.changevalue)
        self.ui.horizontalSlider_3.valueChanged[int].connect(self.changevalue)
        self.ui.horizontalSlider_4.valueChanged[int].connect(self.changevalue)
        self.ui.pushButton_1.clicked.connect(self.buttonClicked)
        self.ui.pushButton_2.clicked.connect(self.buttonClicked)

    def buttonClicked(self):
        sender = self.sender()
        if sender == self.ui.pushButton_2:
            cv2.imwrite("./images/15_blurred.jpg", self.blurred)
            cv2.imwrite("./images/15_edged.jpg", self.edged)
            QtWidgets.QMessageBox.information(self, u"info", u"saved done",
                                              buttons=QtWidgets.QMessageBox.Ok,
                                              defaultButton=QtWidgets.QMessageBox.Ok)
        elif sender == self.ui.pushButton_1:
            pass

    def changevalue(self, value):
        sender = self.sender()
        if sender == self.ui.horizontalSlider_1:
            # self.ui.label_4.setText(str(value))
            pass
        elif sender == self.ui.horizontalSlider_2:
            v = 2 * value + 1
            self.ui.label_20.setText("Blurred Image: value = " + str(v))
            self.blurred = cv2.GaussianBlur(self.gray, (v, v), 0)

            pixmap_2 = self.convert_cv2qtgray(self.blurred.copy())
            self.ui.label_2.setPixmap(pixmap_2)
            self.ui.label_2.setCursor(Qt.CrossCursor)

            # self.edged = cv2.Canny(self.blurred, 30, 150)
            self.edged = self.auto_canny(self.blurred)
            pixmap_3 = self.convert_cv2qtgray(self.edged.copy())
            self.ui.label_3.setPixmap(pixmap_3)
            self.ui.label_3.setCursor(Qt.CrossCursor)

        elif sender == self.ui.horizontalSlider_3:
            self.ui.label_30.setText("Edged Image: value = " + str(value))

        elif sender == self.ui.horizontalSlider_4:
            self.ui.label_4.setText(str(value))

    def load_img(self):
        self.image = cv2.imread("./images/15.jpg")
        self.gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.blurred = cv2.GaussianBlur(self.gray, (5, 5), 0)

        ii = cv2.cvtColor(self.image.copy(), cv2.COLOR_BGR2RGB)
        pixmap_1 = self.convert_cv2qt(ii)
        self.ui.label_1.setPixmap(pixmap_1)
        self.ui.label_1.setCursor(Qt.CrossCursor)

        pixmap_2 = self.convert_cv2qtgray(self.blurred.copy())
        self.ui.label_2.setPixmap(pixmap_2)
        self.ui.label_2.setCursor(Qt.CrossCursor)

        # self.edged = cv2.Canny(self.blurred, 30, 150)
        self.edged = self.auto_canny(self.blurred)
        pixmap_3 = self.convert_cv2qtgray(self.edged.copy())
        self.ui.label_3.setPixmap(pixmap_3)
        self.ui.label_3.setCursor(Qt.CrossCursor)

        # (_, cnts, _) = cv2.findContours(self.edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        # print("I count {} ellipses in this image".format(len(cnts)))

    def convert_cv2qt(self, image):
        show = cv2.resize(image, (576, 412))
        show = cv2.cvtColor(show, cv2.COLOR_BGR2RGB)
        QImg = QImage(show.data, show.shape[1], show.shape[0], 3 * show.shape[1], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(QImg)
        return pixmap

    def convert_cv2qtgray(self, image):
        show = cv2.resize(image, (576, 412))
        QImg = QImage(show.data, show.shape[1], show.shape[0], show.shape[1], QImage.Format_Indexed8)
        pixmap = QPixmap.fromImage(QImg)
        return pixmap

    # Reference:
    # https://www.pyimagesearch.com/2015/04/06/zero-parameter-automatic-canny-edge-detection-with-python-and-opencv/
    def auto_canny(self, image, sigma=0.33):
        # compute the median of the single channel pixel intensities
        v = np.median(image)

        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(image, lower, upper)

        # return the edged image
        return edged


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = Display()
    ui.show()
    sys.exit(app.exec_())
