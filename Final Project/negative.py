import cv2
import numpy as np


def invert(image):
    reTimage = abs(255 - image)
    # cv2.imwrite(name, image)
    return reTimage


def inverte2(image, name):
    for x in np.nditer(image, op_flags=['readwrite']):
        x = abs(255-x)
    cv2.imwrite(name, image)

def quantize(image):
    reTimage = np.copy(image)
    for i in range (1,len(reTimage)):
        for j in range (1,len(reTimage[0])):
                reTimage[i][j] = reTimage[i][j] / 10 * 10 + 10/2
    return reTimage

def combineEdges(image, edgeImg):
    reTimage = np.copy(image) 
    for i in range (1,len(reTimage)):
        for j in range (1,len(reTimage[0])):
            if edgeImg[i][j] > 0 :
                reTimage[i][j] = [0,0,0]
    return reTimage

if __name__ == '__main__':
    image = cv2.imread("hamessy.jpg")
    #negative image

    # smoothImage = cv2.bilateralFilter(image,100, 50, 100)
    # cv2.imwrite("smoothImage.jpg", smoothImage)
    # smoothImage = cv2.imread("smoothImage.jpg")

    #median filter
    medImage = cv2.medianBlur(image, 7)
    cv2.imwrite("quant&med.jpg", medImage)

    #grayscale and gets canny edge
    gs_image = cv2.cvtColor(medImage, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gs_image,70,140)
    cv2.imwrite("edges.jpg", edges)
    kernel = np.ones((2,2), np.int)
    gradient = cv2.morphologyEx(edges, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite("gradient.jpg",gradient)



    smoothImage = cv2.bilateralFilter(medImage,20, 10, 20)
    for i in range(1, 13):
        smoothImage = cv2.bilateralFilter(smoothImage,20, 10, 20)
        cv2.imwrite("smoothImage1.jpg", smoothImage)

    mdImage = cv2.medianBlur(smoothImage, 7)


    
    #Quantize
    qImage = quantize(smoothImage)
    cv2.imwrite("qunt.jpg", qImage)


    #COMBINE EGES AND quantized IMAGE

    cImage = combineEdges(qImage, gradient)
    cv2.imwrite("cImage.jpg", cImage)

   
    # smoothImage2 = cv2.bilateralFilter(image,100, 50, 100)
    # cv2.imwrite("smoothImage2.jpg", smoothImage2)
    # inverte2(image, "invertida2.png")