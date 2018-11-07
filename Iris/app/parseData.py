import json
import os
from pprint import pprint
from app.graph import graph

class parseData:
    def printData():
        times = []
        emotions = []
        values = []

        with open('response.json') as f:
            data = json.load(f)
            for i in data:
                times.append(i['keyframe']['time'])
                emotions.append(i['keyframe']['emotion'])
                values.append(i['keyframe']['value'])

        graph.graphData(times, emotions, values)
