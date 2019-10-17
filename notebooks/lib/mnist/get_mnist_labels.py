import struct

def get_mnist_labels(labels_name):
    
    #returns an array of labels
    
    f = open(labels_name, "rb")
    mnist_labels = []
    
    #Let's read the head of the file encoded in 32-bit integers in big-endian(4 bytes)
    
    mw_32bit = f.read(4) #magic word
    n_numbers_32bit = f.read(4) #number of labels

    #convert it to integers ; '>i' for big endian encoding
    
    mw = struct.unpack('>i',mw_32bit)[0]
    n_numbers = struct.unpack('>i',n_numbers_32bit)[0]

    for i in range(n_numbers):
        byte = f.read(1)
        label = struct.unpack('B',byte)[0]
        mnist_labels.append(label)

    f.close()
    
    return mnist_labels