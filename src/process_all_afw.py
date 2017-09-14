# from os import listdir
from shutil import copyfile
import os, shutil

lfw_path = '/media/diego/7C101BCB101B8AF2/Python/Datasets_Deep_Learn/Faces/LFW/lfw/lfw_mtcnnpy_160'
train_path = '/media/diego/7C101BCB101B8AF2/Python/Datasets_Deep_Learn/Faces/LFW/lfw/test/train/'
test_path = '/media/diego/7C101BCB101B8AF2/Python/Datasets_Deep_Learn/Faces/LFW/lfw/test/test/'
n_train_images = 5
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def remove_directory(directory):
    if os.path.exists(directory):
        shutil.rmtree(directory)


folder_list = os.listdir(lfw_path)

for folder in folder_list:
    img_folder = os.path.join(lfw_path, folder)
    img_train = os.path.join(train_path, folder)
    img_test = os.path.join(test_path, folder)
    # print(isfile(img_folder))
    if not os.path.isfile(img_folder):
        create_directory(img_train)
        create_directory(img_test)
        # remove_directory(img_train)
        # remove_directory(img_test)
        imgs = os.listdir(img_folder)
        i, n_imgs = 0, len(imgs)
        while i<n_imgs and i<n_train_images:
            shutil.copyfile(os.path.join(img_folder, imgs[i]), os.path.join(img_train, imgs[i]))
            i += 1

        if i <= n_train_images:
            i = 0

        while i < n_imgs:
            shutil.copyfile(os.path.join(img_folder, imgs[i]), os.path.join(img_test, imgs[i]))
            i += 1



        # break
        # print(len(imgs))





# print(len(folder_list))
# print(folder_list[1])