#get initial image
# ask user and get image into the inital image directory in the same folder
import io
import os
# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types
import user_scraper
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\vision.json"
label_list = []

def starter_image(imgDest):
        client = vision.ImageAnnotatorClient()
        #dir = "C:\\Users\\chinm\\PycharmProjects\\NwHacksTest1\\InitalPic"
        list = os.listdir(dir)  # dir is your directory path
        numFiles = len(list)
        file_name = os.path.abspath(imgDest)

        with io.open(file_name, 'rb') as image_file:
            content = image_file.read()

        image = types.Image(content=content)
        response = client.label_detection(image=image)
        labels = response.label_annotations
        client = vision.ImageAnnotatorClient()
        objects = client.object_localization(image=image).localized_object_annotations

        for object_ in objects:
            print(object_.name)
            label_list.append(object_)

        print('Labels:')
        for label in labels:
            print(label.description)
            label_list.append(label.description)

        print("-----------------------------------------------------------------------------------------------------------------------------")



# starter_image()
extra_labels=[]
for i in label_list:
    extra_labels.append(user_scraper.get_users_by_tag(i))

print(extra_labels)