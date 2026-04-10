class Manager:
    
    def __init__(self, content: str) -> None:
        self.content = content
        
    def __enter__(self):
        print("Begginning Process")
        return self.content
    
    def __exit__(self, exc_type, exc, tb):
        print("Ending Process")
       

with Manager("In Process") as content:
    print(content)