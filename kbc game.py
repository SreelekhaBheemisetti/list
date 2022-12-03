
print("------------------Welcome To KBC----------------------")
Name=input("enter your name:")
print("welcome come",Name)
start=int(input("press 1 to start game:"))
if start!=1:
    quit()
count=0
Life_line=input("do you want to choose life line:")
if Life_line=="yes":
    count+=1
    print('''B.rajasthan
             D.delhi''')
capital=input("1.what is the capital of india?")  
print('''
      A.chandighar
      B.rajasthan
      C.bhopal
      D.delhi''')
if capital!="D":
    print("you lost the game")
    quit()
else:
    print("correct")
Life_line=input("do you want to choose life line:")
if Life_line=="yes":
    if count==1:
        print("you already used your lifeline")
    else:
        print('''A.yogi
            B.modi''')
print('''
      A.yogi
      B.modi
      C.pikachu
      D.kejrival''')
prime_minister=input("2.who is the prime minister of india?")
if prime_minister!="B":
    print("you lost the game")
    quit()
else:
    print("correct")
Life_line=input("do you want to choose life line:")
if Life_line=="yes":
    if count==1:
        print("you already used your lifeline")
    else:
        print('''A.amaravathi
             B.guntur''')
print('''
      A.amaravathi
      B.guntur
      C.hyderabad
      D.vizag''')
ap_capital=input("what is the capital of andra pradesh?")
if ap_capital!="A":
    print("you lost the game")
    quit()
else:
    print("correct")
print("Great!!! You won the game")
print("CONGRATUALATIONS!!!!")
