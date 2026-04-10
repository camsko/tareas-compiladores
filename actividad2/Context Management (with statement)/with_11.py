class Manager:
    
    def __init__(self, content: str) -> None:
        self.content = content
        
    def __enter__(self):
        print("Begginning Process")
        return self.content
    
    def __exit__(self, exc_type, exc, tb):
        print("Ending Process")
        
with open('note1.txt', 'r') as file1:
    with Manager("In Process") as content:
        text1 = file1.read()
        print(text1)
        print(content)