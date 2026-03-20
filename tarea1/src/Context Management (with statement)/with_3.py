with open('note1.txt', 'r') as file1:
    with open('note2.txt', 'r') as file2:
        text1 = file1.read()
        text2 = file2.read()
        print(text1)
        print(text2)