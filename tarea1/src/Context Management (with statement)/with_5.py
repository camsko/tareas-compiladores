class Manager:
    
    def __enter__(self):
        print("Begginning Process")
    
    def __exit__(self, exc_type, exc, tb):
        print("Ending Process")
       

with Manager():
    print("In Process")