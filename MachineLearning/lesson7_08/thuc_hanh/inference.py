import pickle
# Load the model using a binary read context
with open('/Users/mac/Downloads/AI_Engineer/MachineLearning/lesson7/thuc_hanh/my_model.pkl', 'rb') as file:
    model, scaler = pickle.load(file)
    print(model)
    print(scaler)
fake_input = [[2, 200, 70, 20, 100, 29.3, 0.5, 35]]
fake_input = scaler.transform(fake_input)
print(model.predict(fake_input))