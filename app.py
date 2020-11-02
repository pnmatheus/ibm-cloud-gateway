from flask import Flask, request
import os
from watson_developer_cloud import VisualRecognitionV3
import urllib.request

app = Flask(__name__)


@app.route('/', methods=['POST'])
def index():
    import json
    req_data = request.get_json()

    url = req_data['url']

    urllib.request.urlretrieve(url, './assets/images/image.png')

    visual_recognition = VisualRecognitionV3(
        '2018-03-19',
        iam_apikey='')

    try:
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

        response = {"class": classe}

        return response

    except:
        print('deu ruim')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
