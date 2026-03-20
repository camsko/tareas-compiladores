class Manager:
    
    def __enter__(self):
        print("Begginning Process")
    
    def __exit__(self, exc_type, exc, tb):
        print("Ending Process")

with (
    open('note1.txt', 'r') as file1,
    Manager(),
):
    text1 = file1.read()
    print(text1)