from PIL import Image
import text_to_image


# ascii characters used to build the output text
ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

# resize image according to a new width
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height/width
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = "".join([ASCII_CHARS[pixel//25] for pixel in pixels])
    return(characters)    

def main():
    # attempt to open image from user-input
    path = (input("Image path:\n>"))
    try:
        image = Image.open(path)
    except Exception:
        print(f'{path} is not a valid pathname to an image.')
        return
  
    # convert image to ascii    
    new_width=100
    new_image_data = pixels_to_ascii(grayify(resize_image(image, new_width)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open(f'{path[:-4]}.txt', "w") as f:
        f.write(ascii_image)

    encoded_image_path = text_to_image.encode_file(f'{path[:-4]}.txt', f'ASCII_{path[:-4]}')

 
# run program
if __name__ == "__main__":
    main()