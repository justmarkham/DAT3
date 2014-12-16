import pickle

with open('links_list.pkl', 'rb') as f:
    new_list = pickle.load(f)

print new_list
