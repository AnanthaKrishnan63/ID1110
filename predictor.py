def pneumonia(filename):
    import tensorflow as tf
    import keras 

    class LocalResponseNormalisation(tf.keras.layers.Layer):
            def _init_(self, **kwargs):
                super(local_response_Normalisation, self)._init_(**kwargs)

            def call(self, M):
                return tf.nn.local_response_normalization(M)
    class ConcatLayer(tf.keras.layers.Layer):
        def __init__(self, **kwargs):
            super(ConcatLayer, self).__init__(**kwargs)

        def call(self, inputs):
            return tf.concat(inputs, axis=3)

    model = tf.keras.models.load_model("pnuemonia_2.h5",custom_objects={"LocalResponseNormalisation": LocalResponseNormalisation,"ConcatLayer":ConcatLayer})

    # #TO RESIZE THE I
    from PIL import Image 

    def imgresize():
    #Create an Image Object from an Image"C:\Users\mades\Desktop\wine.jpg"
        im = Image.open(filename)
        x=im.size[0]
        y=im.size[1]
        mf0=224/x
        mf1=224/y
        resized_im = im.resize((round(im.size[0]*mf0), round(im.size[1]*mf1)))
        #Save the cropped image
        resized_im.save(f"{filename.split('.')[0]}_resized.{filename.split('.')[1]}")

    imgresize()

    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    import numpy as np

    # Load the image
    img_path = f"{filename.split('.')[0]}_resized.{filename.split('.')[1]}"

    img = load_img(img_path, target_size=(224, 224)) # Adjust target_size as needed

    # Convert the image to a NumPy array
    img_array = img_to_array(img)

    # Expand dimensions to match the model's expected input shape
    # Assuming the model expects a 4D tensor with shape [batch_size, height, width, channels]
    img_array = np.expand_dims(img_array, axis=0)

    # Now you can pass img_array to model.predict
    predictions = model.predict(img_array)
    
    return predictions

def braintumor(filename):
    import tensorflow as tf
    import keras 

    class LocalResponseNormalisation(tf.keras.layers.Layer):
            def _init_(self, **kwargs):
                super(local_response_Normalisation, self)._init_(**kwargs)

            def call(self, M):
                return tf.nn.local_response_normalization(M)
    class ConcatLayer(tf.keras.layers.Layer):
        def __init__(self, **kwargs):
            super(ConcatLayer, self).__init__(**kwargs)

        def call(self, inputs):
            return tf.concat(inputs, axis=3)

    model = tf.keras.models.load_model("fully_trained_brain_tumour.h5",custom_objects={"LocalResponseNormalisation": LocalResponseNormalisation,"ConcatLayer":ConcatLayer})

    # #TO RESIZE THE I
    from PIL import Image 

    def imgresize():
    #Create an Image Object from an Image"C:\Users\mades\Desktop\wine.jpg"
        im = Image.open(filename)
        x=im.size[0]
        y=im.size[1]
        mf0=224/x
        mf1=224/y
        resized_im = im.resize((round(im.size[0]*mf0), round(im.size[1]*mf1)))
        #Save the cropped image
        resized_im.save(f"{filename.split('.')[0]}_resized.{filename.split('.')[1]}")

    imgresize()

    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    import numpy as np

    # Load the image
    img_path = f"{filename.split('.')[0]}_resized.{filename.split('.')[1]}"

    img = load_img(img_path, target_size=(224, 224)) # Adjust target_size as needed

    # Convert the image to a NumPy array
    img_array = img_to_array(img)

    # Expand dimensions to match the model's expected input shape
    # Assuming the model expects a 4D tensor with shape [batch_size, height, width, channels]
    img_array = np.expand_dims(img_array, axis=0)

    # Now you can pass img_array to model.predict
    predictions = model.predict(img_array)
    
    return predictions