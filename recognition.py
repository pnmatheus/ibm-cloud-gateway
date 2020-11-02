import json
from watson_developer_cloud import VisualRecognitionV3
import urllib.request
import os

url_image = 'https://firebasestorage.googleapis.com/v0/b/ford-project-9ccb2.appspot.com/o/pictures' \
            '%2Ftemp_motor6.jpeg?alt=media&token=ff8cb74b-711d-46a1-8109-f0500c0334a1'

urllib.request.urlretrieve(url_image, './assets/images/image.png')

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    iam_apikey='')

with open('./assets/images/image.png', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file,
        threshold='0.6',
        classifier_ids='modelo_ford_teste2_1300691060').get_result()
    data = json.dumps(classes, indent=2)

json = json.loads(data)

for json in json['images']:
    for data in json['classifiers']:
        for classe in data['classes']:
            classe = classe['class']

print(f'This is the error: {classe}')

os.remove("./assets/images/image.png")
print("File Removed!")
