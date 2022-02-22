import random
import sys

from matplotlib.font_manager import _Weight

class Node:
    
    def __init__(self, layer_num, id) -> None:
        self.layer = layer_num
        self.id = id
        
        self.activation_value = 0 if id!=-1 else 1
        self.forward_links = dict()
        self.backward_links = dict()
    
    def add_link(self, dest_node):
        w = random.random()
        self.forward_links[dest_node] = w
        dest_node.backward_links[self] = w

    def compute_activation(self, activation_function):
        s=0
        for node, weight in self.backward_links.items():
            s += weight * node.activation_value
        
        self.activation_value = activation_function(s)
            

    def __str__(self) -> str:
        print(f"Layer: {self.layer}, Id: {self.id}")
        print(f"Activation_value: {self.activation_value}")

        print(f"Number of Forward links: {len(self.links)}")
        for linked_node, weight in self.forward_links.items():
            print(f"Layer: {linked_node.layer}, Id: {linked_node.id}, W: {weight}")

        print(f"Number of Bakcward links: {len(self.links)}")
        for linked_node, weight in self.backward_links.items():
            print(f"Layer: {linked_node.layer}, Id: {linked_node.id}, W: {weight}")



class Model:

    def __init__(self, neurons_layers:tuple) -> None:
    
        self.layers = dict()
        # Creation of nodes
        for layer, num_nodes in enumerate(neurons_layers):
            self.layers["layer_" + str(layer)] = {"node_"+str(node_id):Node(layer, node_id) for node_id in range(num_nodes)}
            self.layers["layer_" + str(layer)]["bias"] = Node(layer, -1)

        # Connection of nodes
        for layer in range(len(neurons_layers)-1):
            for node in self.layers["layer_" + str(layer)].values():
                for next_node in self.layers["layer_" + str(layer + 1)].values():
                    node.add_link(next_node)

    def giveInput(self, data:list):
        """Given the input, make all the forward passages to the output"""
        # Load first layer
        if len(data) != len(self.layers["layer_0"])-1:
            print("Error: data lenght must be equals to t he first layer lenght")
            sys.exit()
        
        for data_idx, node in enumerate(self.layers["layer_0"].values()):
            node.activation_value = data[data_idx]

        return self


    def forward(self):
        for layer in range(1, len(self.layers)):
            for node in self.layers["layer_"+str(layer)].values():
                node.compute_activation(self.RELU)

        return self

    def compute_loss(self):
        return self
    def compute_gradient(self):
        return self
    def backpropagate(self):
        pass

    def leaky_RELU(self, value):
        return max(0,1 * value, value)
    
    def RELU(self, value):
        return max(0, value)

train = False
nn = Model(neurons_layers=(10,3,10))
if train:
    nn.giveInput().forward().compute_loss().compute_gradient().backpropagate()

print()

