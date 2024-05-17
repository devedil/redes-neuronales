"""" Importamos numpy y librerias  """

import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model

"""validamos las imagenes"""
longitud, altura = 150, 150
modelo = './modelo/modelo.h5'
pesos_modelo = './modelo/pesos.h5'
cnn = load_model(modelo)
cnn.load_weights(pesos_modelo)

"""Predecimos"""

def predict(file):
  x = load_img(file, target_size=(longitud, altura))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = cnn.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("pred: nefrolitiasis")
  elif answer == 1:
    print("pred: riñon sano")

  return answer

"""FALTA APARTADO DE SIMULACION!! SOLO ESTAMOS VALIDANDO Y PREDICIENDO. AUN FALTA ENTRENAR PARA MEDIR Y SIMULAR"""

