import operator
import numpy as np
import keras
from keras.preprocessing import image

class Fruit:
    def classify(self,testImageFile):
        from keras.models import model_from_json

        # read the json model
        file = open('my_model.json', 'r')
        data = file.read()
        #print(data)

        file.close()

        # classifier will load the model from the data
        # data -> contents of the my_model.json file
        classifier = model_from_json(data)

        # load waits
        classifier.load_weights('weights.h5')

        # load the test image
        from keras.preprocessing import image

        test_image = image.load_img(testImageFile, target_size=(64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)

        classifier.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        result = classifier.predict(test_image)
        prediction ={'Apple': result[0][0],
                     'Banana': result[0][1],
                         'Cherry': result[0][2],
                         'Custard_apple': result[0][3],
                         'Dragon_fruit': result[0][4],
                         'Guava': result[0][5],
                         'Lychee': result[0][6],
                         'Mango': result[0][7],
                         'Orange': result[0][8],
                         'Pineapple': result[0][9],
                         'Pomegranate': result[0][10],
                         'Strawberry': result[0][11],
                         'Watermelon': result[0][12]
                         }
        prediction = sorted(prediction.items(), key= operator.itemgetter(1), reverse= True)

        return (prediction)
