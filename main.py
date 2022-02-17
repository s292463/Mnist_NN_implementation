import random
import matplotlib.image as mpimg

class Perceptron:
    
    def __init__(self, number_of_neurons=None) -> None:
        
        self.activation_value = random.random()
        self.weight = [random.random() for _ in range(number_of_neurons)] if number_of_neurons else None
        self.bias = random.random()
            

    def __str__(self) -> str:
        print(f"w: {self.weight}, activation_value: {self.activation_value}")
        print(f"Number of links: {len(self.links)}")


class NN:

    def __init__(self, neurons_layers) -> None:
    
        self.layers = dict()
        for i, value in enumerate(neurons_layers):
            self.layers["layer_"+str(i)] = [Perceptron(neurons_layers[i+1]) for _ in range(value)] if i+1 < len(neurons_layers) else [Perceptron() for _ in range(value)]

    def leaky_RELU(self, data):
        return max(0,1*data, data)
    
    def RELU(self, data):
        return max(0, data)

        
nn = NN([10,3,10])

img = mpimg.imread('H:\\Projects\\Mnist_NN_implementation\\MNIST Dataset JPG format\\MNIST Dataset JPG format\\MNIST - JPG - testing\\0\\3.jpg')
print()



