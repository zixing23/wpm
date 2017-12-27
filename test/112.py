import pickle
with open('athletes.pickle','rb') as f:
    data = pickle.load(f)
print(data)