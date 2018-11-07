import requests
import json
import matplotlib.pyplot as plt
from PIL import Image
from matplotlib import patches
from io import BytesIO

class sendToAPI:
    def imgToAPI(path, filename):
        imgpath = path + filename
        subscription_key = "3f7378e524c1471c907ad9ddbea4ba88"
        assert subscription_key
        
        face_api_url = 'https://westus2.api.cognitive.microsoft.com/face/v1.0/detect'
        
        image_url = imgpath
        
        headers = {'Content-Type': 'application/octet-stream',
                   'Ocp-Apim-Subscription-Key': subscription_key}
        params = {
            'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
            'returnFaceAttributes': 'emotion'
        }

        data = open(image_url, 'rb')
        print('Ejecutando análisis...')
        response = requests.post(face_api_url, params=params, headers=headers, data=data)
        faces = response.json()
        try:
            for face in faces:
                fr = face["faceRectangle"]
                origin = (fr["left"], fr["top"])
                p = patches.Rectangle(
                    origin, fr["width"], fr["height"], fill=False, linewidth=2, color='b')
                plt.text(origin[0], origin[1], "%s, %d",
                         fontsize=20, weight="bold", va="bottom")
            _ = plt.axis("off")

            anger = faces[0]['faceAttributes']['emotion']['anger']
            contempt = faces[0]['faceAttributes']['emotion']['contempt']
            disgust = faces[0]['faceAttributes']['emotion']['disgust']
            fear = faces[0]['faceAttributes']['emotion']['fear']
            happiness = faces[0]['faceAttributes']['emotion']['happiness']
            neutral = faces[0]['faceAttributes']['emotion']['neutral']
            sadness = faces[0]['faceAttributes']['emotion']['sadness']
            surprise = faces[0]['faceAttributes']['emotion']['sadness']
            emotions = [anger, contempt, disgust, fear, happiness, neutral, sadness, surprise]

            output_file = open("response.json","a+")
            output_file.write("{\n\"keyframe\":{\n\"time\":" + filename[:-4] +  ",\n\"emotion\":")

            if max(emotions) == anger:
                strrp = "\"ira\",\n\"value\":" + str(anger * 100)
                print(anger)
            elif max(emotions) == contempt:
                strrp = "\"desprecio\",\n\"value\":" + str(contempt * 100)
                print(contempt)
            elif max(emotions) == disgust:
                strrp = "\"asco\",\n\"value\":" + str(disgust * 100)
                print(disgust)
            elif max(emotions) == fear:
                strrp = "\"miedo\",\n\"value\":" + str(fear * 100)
                print(fear)
            elif max(emotions) == happiness:
                strrp = "\"felicidad\",\n\"value\":" + str(happiness * 100)
                print(happiness)
            elif max(emotions) == neutral:
                strrp = "\"neutral\",\n\"value\":" + str(neutral * 100)
                print(neutral)
            elif max(emotions) == sadness:
                strrp = "\"tristeza\",\n\"value\":" + str(sadness * 100)
                print(sadness)
            elif max(emotions) == surprise:
                strrp = "\"sorpresa\",\n\"value\":" + str(surprise * 100)
                print(surprise)

            output_file.write(strrp + "}\n},\n")
            output_file.close()
        except:
            print("No identificado.\n\n")
