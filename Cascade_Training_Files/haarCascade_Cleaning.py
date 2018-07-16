from six.moves import urllib
import cv2
import numpy as np
import os

def store_raw_images():
    pos_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n08242223"
    #neg_images_link = "http://image-net.org/api/text/imagenet.synset.geturls?wnid=n04285008"
    pos_image_urls = urllib.request.urlopen(pos_images_link).read().strip()

    if not os.path.exists('pos'):
        os.makedirs('pos')

    pic_num = 1

    for i in pos_image_urls.split('\n'):
        try:
            print(i)
            urllib.request.urlretrieve(i, "pos/" + str(pic_num) + '.jpg')
            img = cv2.imread("pos/" + str(pic_num) + '.jpg', cv2.IMREAD_GRAYSCALE)
            resized_image = cv2.resize(img, (100, 100))
            cv2.imwrite("pos/" + str(pic_num) + '.jpg', resized_image)
            pic_num += 1

        except Exception as e:
            print(str(e))

#store_raw_images()


def find_undesirables():
    for file_type in ['pos']:
        for img in os.listdir(file_type):
            for uglyFile in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type) + '/' + str(img)
                    uglyFile = cv2.imread('uglies/' + str(uglyFile))
                    question = cv2.imread(current_image_path)

                    if uglyFile.shape == question.shape and not(np.bitwise_xor(uglyFile, question).any()):
                        print("ugly b***h")
                        os.remove(current_image_path)

                except Exception as e:
                    print(str(e))

#find_undesirables()


def create_pos_n_neg_files():
    for file_type in ['neg']:

        for img in os.listdir(file_type):
            if file_type == 'neg':
                line = file_type + '/' + img + '\n'
                with open('bg.txt', 'a') as f:
                    f.write(line)

create_pos_n_neg_files()
