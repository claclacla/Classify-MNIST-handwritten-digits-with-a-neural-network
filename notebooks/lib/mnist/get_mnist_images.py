import struct

def get_mnist_images(images_name):
    
    #returns an array of flattened images
    
    f = open(images_name, "rb")
    mnist_images = []
    
    #Let's read the head of the file encoded in 32-bit integers in big-endian(4 bytes)
    
    mw_32bit = f.read(4) #magic word
    n_numbers_32bit = f.read(4) #number of images
    n_rows_32bit = f.read(4) #number of rows of each image
    n_columns_32bit = f.read(4) #number of columns of each image

    #convert it to integers ; '>i' for big endian encoding
    
    mw = struct.unpack('>i',mw_32bit)[0]
    n_numbers = struct.unpack('>i',n_numbers_32bit)[0]
    n_rows = struct.unpack('>i',n_rows_32bit)[0]
    n_columns = struct.unpack('>i',n_columns_32bit)[0]

    for i in range(n_numbers):
        image = []

        for r in range(n_rows):
            for l in range(n_columns):
                byte = f.read(1)
                pixel = struct.unpack('B',byte)[0]
                image.append(pixel)
                mnist_images.append(image)

    f.close()
        
    return mnist_images