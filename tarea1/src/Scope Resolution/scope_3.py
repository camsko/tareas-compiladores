list = [1, 2, 3]

print("Built-in len:", len(list)) 

def len(list):
    return 42

print("Local len:", len(list)) 