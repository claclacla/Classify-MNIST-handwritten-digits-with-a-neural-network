from .get_mnist_images import get_mnist_images
from .get_mnist_labels import get_mnist_labels

def get_mnist_data(mnist_dataset):
    mnist_images = get_mnist_images(mnist_dataset["images"])
    mnist_labels = get_mnist_labels(mnist_dataset["labels"])
    
    return list(zip(mnist_images, mnist_labels))