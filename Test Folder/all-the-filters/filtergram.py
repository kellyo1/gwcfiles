import filters

def main():
    filename = input("Enter the name image you want to edit: ")

    image = filters.load_img(filename)

    image.save(image, "editedImage.jpeg")

    image.show()

#must have for program to work, do NOT edit
if __name__ == "__main__":
        main()
