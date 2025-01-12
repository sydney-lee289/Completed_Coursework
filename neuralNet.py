import random
import math

class LinearNode:
    def __init__(self, dimension):
        #self.weights = [random.random() for i in range(dimension)]
        #self.bias = random.random()
        
        self.weights = [0.5 for i in range(dimension)]
        self.bias = 0
        
    def forward(self, inputs):
        if len(inputs) != len(self.weights):
            return False
        else:
            output = 0
            for i in range(len(self.weights)):
                output += inputs[i]*self.weights[i]
            output += self.bias
            return output
        
class NonLinearNode:
    def forward(self, input):
        output = math.log(1+math.exp(input))
        return output
    
class NeuralNet:
    def __init__(self, inputShape, hiddenLayerNodes):
        self.HiddenLayerCount = len(hiddenLayerNodes)
        
        self.layers = []
        for i in range(self.HiddenLayerCount):
            if i == 0:
                inputDimension = inputShape
            else:
                inputDimension = hiddenLayerNodes[i-1]
            linearNodes = []
            nonLinearNodes = []
            for j in range(hiddenLayerNodes[i]):
                linearNodes.append(LinearNode(inputDimension))
                nonLinearNodes.append(NonLinearNode())
            self.layers.append([linearNodes, nonLinearNodes])
            
        
    def forwardPropagation(self, input):
        currentInput = input
        for i in range(len(self.layers)):
            layer = self.layers[i]
            intermediateOutput = []
            sizeOfLayer = len(layer[0])
            for j in range(sizeOfLayer):
                temp = layer[0][j].forward(currentInput)
                output = layer[1][j].forward(temp)
                intermediateOutput.append(output)
            print(currentInput, intermediateOutput)
            currentInput = intermediateOutput
  
        return currentInput
            

nn = NeuralNet(2, [3, 2, 3])
print(nn.forwardPropagation([1, 1]))

        
        
