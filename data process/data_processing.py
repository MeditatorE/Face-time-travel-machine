from PIL import Image
import os

#Get filename
filename_1 = os.listdir(r'C:\Users\admin\asian_test\young\\')   
filename_2 = os.listdir(r'C:\Users\admin\asian_test\old\\')

#Modify the parameters of the picture
width = 256
height = 256
os.mkdir(r'C:\Users\admin\asian_test\young_edit')
os.mkdir(r'C:\Users\admin\asian_test\old_edit')
for img in filename_1:
    pic1 = Image.open(r'C:\Users\admin\asian_test\young\\'+img)
    newpic1 = pic1.resize((width, height),Image.ANTIALIAS)
    print(newpic1)
    newpic1.save(r'C:\Users\admin\asian_test\young_edit\\'+img)

for img in filename_2:
    pic2 = Image.open(r'C:\Users\admin\asian_test\old\\'+img)
    newpic2 = pic2.resize((width, height),Image.ANTIALIAS)
    print(newpic1)
    newpic2.save(r'C:\Users\admin\asian_test\old_edit\\'+img)
