from __future__ import division, print_function
from unittest import result

import numpy as np


from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import load_img, img_to_array


labels= { 0: 'Apple black rot',
    1: 'Apple healthy',
    2: 'Apple scab',
    3: 'Potato early blight',
    4: 'Potato healthy',
    5: 'Potato late blight'}

## loading the saved model
model= load_model("diseaseDetects.h5")

def model_predict(new_scr):
    img = load_img(str(new_scr), target_size=(224, 224))
    # plt.imshow(img)
    img = img_to_array(img)
    # img = img / 255
    # print(img, img.shape)

    img = img.reshape(1, 224, 224, 3)
    result = model.predict(img)
    print(result)
    preds1 = np.argmax(result, axis=1)
    print(preds1)
    if preds1 == 0:
        preds1 = "Apple black rot"

    elif preds1 == 1:
        preds1 = "Apple healthy"

    elif preds1 == 2:
        preds1 = "Apple scab"

    elif preds1 == 3:
        preds1 = "Potato early blight"

    elif preds1 == 4:
        preds1 = "Potato healthy"

    elif preds1 == 5:
        preds1 = "Potato late blight "



    return preds1




