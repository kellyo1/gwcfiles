# Add commands to import modules here.
from PIL import Image

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(filename):
    imageObject = Image.open(filename)
    return imageObject

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(filename):
    imageObject.show()

# # Define your save_img() function here.
# #       Parameters: The image object to save, the name to save the file as (string)
# #       Returns: nothing.
def save_img(imageObject, filename):
    imageObject.save(newdownload, "jpeg")
    show_img(imageObject)
#
# # Define your obamicon() function here.
# #       Parameters: The image object to apply the filter to.
# #       Returns: A New Image object with the filter applied.
# def obamicon():
#
#     PIL.Image.open(filename)
#
#     darkBlue = (0, 51, 76)
#     red = (217, 26, 33)
#     lightBlue = (112, 150, 158)
#     yellow = (252, 227, 166)
#
#     recolored = []
#     for pixel in image_list:
#
#         intensity = pixel[0] + pixel[1] + pixel[2]
#
#         if intensity < 182:
#             recolored.append(darkBlue)
#
#         elif intensity >= 182 and intensity < 364:
#             recolored.append(red)
#
#         elif intensity >= 364 and intensity < 546:
#             recolored.append(lightBlue)
#
#         elif intensity >=546:
#             recolored.append(yellow)
