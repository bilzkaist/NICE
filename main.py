import os
import cv2
import numpy as np
import pandas as pd
from keras.applications.xception import Xception, preprocess_input
import tensorflow as tf
from keras.preprocessing import image
from keras.layers import Input
from keras.backend import reshape
from sklearn.neighbors import NearestNeighbors
import matplotlib.pyplot as plt
import time


images_dir = 'input/crypto-coven/witch_images/witch_images'

def get_image_paths(path):
    """
    function to combine directory path with individual image paths
    """
    image_names = []
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            if 'os.png' in filename:  # choose only the OpeaSea image
                fullpath = os.path.join(dirname, filename)
                image_names.append(fullpath)
    return image_names


def preprocess_img(img_path):
    dsize = (225, 225)
    new_image = cv2.imread(img_path)
    new_image = cv2.resize(new_image, dsize, interpolation=cv2.INTER_NEAREST)  
    new_image = np.expand_dims(new_image, axis=0)
    new_image = preprocess_input(new_image)
    return new_image


def model():
    model = Xception(weights='imagenet', include_top=False)
    for layer in model.layers:
        layer.trainable=False
        #model.summary()
    return model


def feature_extraction(image_data, model):
    features = model.predict(image_data)
    features = np.array(features)
    features = features.flatten()
    return features


def result_vector_cosine(model, feature_vector, new_img, n_results):
    new_feature = model.predict(new_img)
    new_feature = np.array(new_feature)
    new_feature = new_feature.flatten()
    nbrs = NearestNeighbors(n_neighbors=n_results, metric="cosine").fit(feature_vector)
    distances, indices = nbrs.kneighbors([new_feature])
    return (indices)


def show_query_image(data):
    plt.title("Query Image")
    plt.imshow(data)
    plt.xticks([])
    plt.yticks([])


# 12 is hardcoded for now
def show_result(data, result):
    fig = plt.figure(figsize=(12,8))
    for i in range(0,12):
        index_result = result[0][i]
        plt.subplot(3, 4, i+1)
        plt.imshow(cv2.imread(data[index_result]))
        plt.xticks([])
        plt.yticks([])
    plt.show()


def run(q=1, ds=9000, resImages=12):
    print("Running...")
    images = get_image_paths(images_dir)
    #n = 5
    #for i in range(n):
    #    print(images[i])
    #%%time
    # extract features for each image
    features = []
    main_model = model()

    for i in images[:ds]:  # only extract the frist 1000 to save time, remove [:1000] as you see fit
        print("Running features at ",i,"/",ds)
        new_img = preprocess_img(i)
        features.append(feature_extraction(new_img, main_model))

    feature_vec = np.array(features)

    # change the number to try different query image

    try:
        query_image = images[q]
    except:
        print("Custom Error-> IndexError: list index out of range")

    # print query image name
    print(query_image)

    # result are the index numbers for the 12 most similar images
    top_similar_image_indexes = result_vector_cosine(main_model, feature_vec, preprocess_img(query_image), 12)

    # print result image names
    for i in range(0,resImages):
        j = top_similar_image_indexes[0][i]
        print(images[j])

    show_query_image(cv2.imread(query_image))
    show_result(images, top_similar_image_indexes)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def print_bye(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Bye, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(' Bilal Dastagir')
    absolute_path = os.path.abspath(__file__)
    print("Full path: " + absolute_path)
    print("Directory Path: " + os.path.dirname(absolute_path))
    start_time = time.time()
    run()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))
    print_bye('Bilal Dastagir')