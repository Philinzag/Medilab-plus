
import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 150, 150
model_path = './models/model.h5'
model_weights_path = './models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  if answer == 0:
    print("Label: Acne vulgaris")
  elif answer == 1:
    print("Label: Atopic Dermatitis")
  elif answer == 2:
    print("Label: scabies")
  return answer

Acne_t = 0
Acne_f = 0
Atopic_t = 0
Atopic_f = 0
scabies_t = 0
scabies_f = 0

for i, ret in enumerate(os.walk('./test-data/Acne')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Acne vulgaris")
    result = predict(ret[0] + '/' + filename)
    if result == 0:
      Acne_t += 1
    else:
      Acne_f += 1

for i, ret in enumerate(os.walk('./test-data/Atopic')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Atopic Dermatitis")
    result = predict(ret[0] + '/' + filename)
    if result == 1:
      Atopic_t += 1
    else:
      Atopic_f += 1

for i, ret in enumerate(os.walk('./test-data/scabies')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: scabies")
    result = predict(ret[0] + '/' + filename)
    if result == 2:
      print(ret[0] + '/' + filename)
      scabies_t += 1
    else:
      scabies_f += 1

"""
Check metrics
"""
print("True Acne vulgaris: ", Acne_t)
print("False Acne vulgaris: ", Acne_f)
print("True Atopic Dermatitis: ", Atopic_t)
print("False Atopic Dermatitis: ", Atopic_f)
print("True scabies: ", scabies_t)
print("False scabies: ", scabies_f)
