import numpy as np

theta = 1
epochs = 5

class Perceptrons:
    def __init__(self, no_of_inputs, lr = 0.2):
        self.lr = lr
        self.weights = np.zeros(no_of_inputs + 1)

    def predict(self, inputs):
        return np.dot(self.weights[1:],inputs) + self.weights[0]

    def train(self, train_inputs, labels):
        for input, label in zip(train_inputs, labels):
            net_in = self.predict(input)

            if net_in > theta : y_out =  1
            elif net_in < -1 : y_out = -1
            else : y_out =  0
            print(f'Weights updated {self.weights} --> ', end="")
            if y_out != label:
                self.weights[1:] += self.lr*label*input
                self.weights[0] += self.lr * label
            print(self.weights)

training_inputs = []
training_inputs.append(np.array([-1,-1]))
training_inputs.append(np.array([-1,1]))
training_inputs.append(np.array([1,-1]))
training_inputs.append(np.array([1,1]))

t = np.array([-1,1,1,1])

perceptrons = Perceptrons(2)

for i in range(epochs):
    print(f'Epoch: {i}')
    perceptrons.train(training_inputs, t)