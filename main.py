from PySide2 import QtWidgets
from PySide2.QtWidgets import QListWidget
from todoUI import Ui_MainWindow
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import Qt
from PySide2.QtGui import *
import json
import os
filename = 'task.json'

# task = {"date":[]}

task = {"data":[]}
isFile = os.path.isfile(filename)
if (not isFile):
    with open(filename, "w") as file:
        json.dump(task,file)



# with open(filename, 'w') as fp:
#     json.dump(task, fp, indent=4)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.view()
        self.add_btn.pressed.connect(self.add)
        self.add_btn.setShortcut("Return")
        self.del_btn.setShortcut("Delete")

        self.del_btn.pressed.connect(self.delete)

    def view(self):
        with open(filename,"r") as file:
            fdata = json.load(file)
            for i in fdata["data"]:
                self.listWidget.addItem(i["name"])

    def add(self):
        list  = self.newtaskedit.text()
        self.listWidget.addItem(list)
        with open(filename, "r+") as file:
            filedata = json.load(file)
            tasklist = dict({"id": self.setId()+1, "name": list, "staus": "Incomplate"})
            filedata["data"].append(tasklist)
            file.seek(0)
            json.dump(filedata, file, indent=4)

    def delete(self):
        listItem = self.listWidget.currentRow()
        print(type(listItem), listItem)
        self.listWidget.takeItem(listItem)
        with open(filename, "r+") as file:
            data = json.load(file)
            del data['data'][listItem-1]
        with open(filename, "w") as file:
            json.dump(data,file,indent=4)
    def setId(self):
        lastid = []
        with open(filename, "r") as file:
            data = json.load(file)
            for i in data["data"]:
                lastid.append(i["id"])
            lastid.sort()
            if len(lastid)<= 0:
                return  lastid == 0
            else:
                return (lastid[-1])


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()