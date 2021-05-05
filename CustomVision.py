from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials
import cv2
from PIL import Image, ImageDraw, ImageFont
import urllib


font                   = cv2.FONT_HERSHEY_SIMPLEX
#Tipo de letra
fontScale              = 0.7
fontColor              = (0,0,255)
lineType               = 2
credentials = ApiKeyCredentials(in_headers={"Prediction-key": "a35ef576706b43f187befdc66035b3f1"})
predictor = CustomVisionPredictionClient("https://southcentralus.api.cognitive.microsoft.com/", credentials)
url = "https://pbs.twimg.com/media/EPuFMgJUwAAFOzi.jpg"
#Colocamos el link a la imagen que queremos analiza
urllib.request.urlretrieve(url, "python.png")
#La guardamos como python.png
imagen=cv2.imread("python.png")
#Guardamos la imagen dentro de una variable
height, width, channels = imagen.shape
#Obtenemos sus dimensiones
Resultado = predictor.detect_image_url("10eaae63-b28c-4321-aaf4-14b690e9e2d1", "Iteration1", url) 

for prediction in Resultado.predictions:
        if prediction.probability > 0.4:
#Escogemos los resultados que tengan una predicción del más del 40%, pero la puedes cambiar a conveniencia.
                bbox = prediction.bounding_box
#Obtenemos los datos de las posiciones donde se encontraron los resultados.
                tag = prediction.tag_name
#Obtenemos el nombre de la etiqueta.
#Multiplicamos la probabilidad por 100 y la cambiamos a tipo entero para obtener un porcentaje múltiplo de 10.
                probabilidad= int(prediction.probability * 100)
#Dibujamos un rectángulo para mostrar los resultados multiplicando las dimensiones de la predicción por las dimensiones de la imagen original y le asignamos el color verde.
                result_image = cv2.rectangle(imagen, (int(bbox.left * width), int(bbox.top * height)), (int((bbox.left + bbox.width) * width), int((bbox.top + bbox.height) * height)), (0, 255, 0), 3)
#En una variable obtenemos la posición donde estará el texto de la etiqueta.
                bottomLeftCornerOfText = (int(bbox.left*width),int(((bbox.top*height)+(bbox.height*height))))
#Colocamos el texto en la imagen final.
                cv2.putText(result_image,str(probabilidad)+"% "+tag,
                bottomLeftCornerOfText, 
                font, 
                fontScale,
                fontColor,
                lineType)
#Guardamos la imagen como result.png
                cv2.imwrite('result.png', result_image)     
cv2.imshow('Resultado',result_image)
#Imprimimos la imagen
cv2.waitKey(0)
#Se cerrará cuando presionemos una tecla.


