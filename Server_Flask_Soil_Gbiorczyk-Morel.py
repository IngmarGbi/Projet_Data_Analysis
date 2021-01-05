from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json

app = Flask(__name__)
@app.route('/api/',methods=['POST'])

def makecalc():
    data = request.get_json()
    #Traitement Data ici pour extraire les données utilisées dans la prédiction
    indexes = [0,1,2,3,8,9,10,11,24,25,26,27,32,33,34,35]
    for index in sorted(indexes, reverse=True):
        del data[0][index]
    print(data)
    prediction = np.array2string(model.predict(data))
    return jsonify(prediction)


if __name__ == '__main__':
    modelfile = 'prediction_soil.pickle'
    model =  p.load(open(modelfile,'rb'))
    app.run(debug=False, host='0.0.0.0')
