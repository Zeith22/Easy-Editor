from PIL import Image, ImageFilter, ImageOps
import os
from .widgets import *

work_dir = ''
file_path = None
work_image = None
filenames = []
extensions = ['.png', '.jpg', '.jpeg']
def filter(listnames):
    output_list =[]
    for i in listnames:
        for j in extensions:
            if j in i:
                output_list.append(i)
    return output_list
def show_dialog():
    global work_dir
    global filenames
    work_dir = filedialog.getExistingDirectory()
    try:
        filenames = filter(os.listdir(work_dir))
        filelist.clear()
        for i in filenames:
            filelist.addItem(i)

    except:
        pass
    print(filenames)
def show_image():
    try:
        global file_path
        global work_image
        file_path = filelist.currentItem().text()
        file_path = os.path.join(work_dir, file_path)
        img = QPixmap(file_path)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path)
    except:
        pass
def wb_image():
    global file_path
    global work_image
    try:
        work_image = work_image.convert("L")
        path = os.path.abspath(__file__+"/../..")
        name_file = file_path.split('/')[-1]
        file_path1 = os.path.join(path,'rezult', name_file)
        work_image.save(file_path1)
        img = QPixmap(file_path1)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path1)
    except:
        pass
def rotate_left():
    global file_path
    global work_image
    try:
        work_image = work_image.transpose(Image.ROTATE_90)
        path = os.path.abspath(__file__+"/../..")
        name_file = file_path.split('/')[-1]
        file_path1 = os.path.join(path,'rezult', name_file)
        work_image.save(file_path1)
        img = QPixmap(file_path1)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path1)
    except:
        pass
def rotate_right():
    global file_path
    global work_image
    try:
        work_image = work_image.transpose(Image.ROTATE_270)
        path = os.path.abspath(__file__+"/../..")
        name_file = file_path.split('/')[-1]
        file_path1 = os.path.join(path,'rezult', name_file)
        work_image.save(file_path1)
        img = QPixmap(file_path1)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path1)
    except:
        pass
def miror():
    global file_path
    global work_image
    try:
        work_image = ImageOps.mirror(work_image)
        path = os.path.abspath(__file__+"/../..")
        name_file = file_path.split('/')[-1]
        file_path1 = os.path.join(path,'rezult', name_file)
        work_image.save(file_path1)
        img = QPixmap(file_path1)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path1)
    except:
        pass
def sharpness():
    global file_path
    global work_image
    try:
        work_image = work_image.filter(ImageFilter.SHARPEN)
        path = os.path.abspath(__file__+"/../..")
        name_file = file_path.split('/')[-1]
        file_path1 = os.path.join(path,'rezult', name_file)
        work_image.save(file_path1)
        img = QPixmap(file_path1)
        img = img.scaled(500,500)
        imagelabel.setPixmap(img)
        work_image = Image.open(file_path1)
    except:
        pass

filelist.currentRowChanged.connect(show_image)
browse.clicked.connect(show_dialog)
wb_btn.clicked.connect(wb_image)
left_btn.clicked.connect(rotate_left)
right_btn.clicked.connect(rotate_right)
sharpness_btn.clicked.connect(sharpness)
mirror_btn.clicked.connect(miror)
