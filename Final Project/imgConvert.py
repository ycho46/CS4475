import cv2
import numpy as np


def invert(image):
    retImage = abs(255 - image)
    cv2.imwrite("invert.jpg", image)
    return retImage

def medianFilter(image) :
    retImage = cv2.medianBlur(image, 5)
    cv2.imwrite("median.jpg", retImage)
    return retImage

def getEdges(image) :
    gs_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gs_image,70,140)
    # cv2.imwrite("edges.jpg", edges)
    kernel = np.ones((2,2), np.int)
    gradient = cv2.morphologyEx(edges, cv2.MORPH_GRADIENT, kernel)
    cv2.imwrite("edges.jpg",gradient)
    return gradient

def smoothImage(image) :
    retImage = cv2.bilateralFilter(image,20, 10, 20)
    for i in range(1, 5):
        retImage = cv2.bilateralFilter(retImage,20, 10, 20)
    cv2.imwrite("bilateral.jpg", retImage)
    return retImage

def quantize(image):
    retImage = np.copy(image)
    for i in range (1,len(retImage)):
        for j in range (1,len(retImage[0])):
                retImage[i][j] = retImage[i][j] / 10 * 10 + 10/2
    cv2.imwrite("quantized.jpg", retImage)
    return retImage


def combineEdges(image, edgeImg):
    retImage = np.copy(image) 
    for i in range (1,len(retImage)):
        for j in range (1,len(retImage[0])):
            if edgeImg[i][j] > 0 :
                retImage[i][j] = [0,0,0]
    return retImage

def convertToon(image) :
    img = np.copy(image)
    retImage = medianFilter(img)
    edges = getEdges(retImage)
    retImage = smoothImage(retImage)
    retImage = medianFilter(retImage)
    retImage = quantize(retImage)
    retImage = combineEdges(retImage, edges)
    return retImage
    # cv2.imwrite("caricature.jpg",retImage)

# if __name__ == '__main__':
#     image = cv2.imread("1.jpg")
#     img1 = caricature(image)
#     cv2.imwrite("c1.jpg",img1)
#     #negative image

#     # smoothImage = cv2.bilateralFilter(image,100, 50, 100)
#     # cv2.imwrite("smoothImage.jpg", smoothImage)
#     # smoothImage = cv2.imread("smoothImage.jpg")

#     #median filter
#     medImage = cv2.medianBlur(image, 7)
#     cv2.imwrite("quant&med.jpg", medImage)

#     #grayscale and gets canny edge
#     gs_image = cv2.cvtColor(medImage, cv2.COLOR_BGR2GRAY)
#     edges = cv2.Canny(gs_image,70,140)
#     cv2.imwrite("edges.jpg", edges)
#     kernel = np.ones((2,2), np.int)
#     gradient = cv2.morphologyEx(edges, cv2.MORPH_GRADIENT, kernel)
#     cv2.imwrite("gradient.jpg",gradient)



#     smoothImage = cv2.bilateralFilter(medImage,20, 10, 20)
#     for i in range(1, 13):
#         smoothImage = cv2.bilateralFilter(smoothImage,20, 10, 20)
#         cv2.imwrite("smoothImage1.jpg", smoothImage)

#     mdImage = cv2.medianBlur(smoothImage, 7)


    
#     #Quantize
#     qImage = quantize(smoothImage)
#     cv2.imwrite("qunt.jpg", qImage)


#     #COMBINE EGES AND quantized IMAGE

#     cImage = combineEdges(qImage, gradient)
#     cv2.imwrite("cImage.jpg", cImage)

   
#     # smoothImage2 = cv2.bilateralFilter(image,100, 50, 100)
#     # cv2.imwrite("smoothImage2.jpg", smoothImage2)
#     # inverte2(image, "invertida2.png")