with open("a.txt","r") as file:
    data= file.readlines()
    for a in data:
        word= a.split()
        print(word)