p = input("Please enter words you like ")
def frame(words):
    size =len(max(words,key=len))
    print('*' *(size + 4))
    for word in words:
        print(f'*{word}*')
    print('*' * (size + 4))
frame(p.split(" "))        