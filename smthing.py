age = []
ava = 0
age_limiter = []
anti_limiter = []
Name = input ("Enter username ")
print(f"greetings {Name}")
NGNL = input("Have you watched No Game No Life y/n ")
while True:
    if NGNL == "y":
        age.append(13)
        age.append(50)
    elif NGNL == "n":
        age.append(0)
        age.append(13)
        age.append(51)
        age.append(100)
    else:
        print("False input")
        break
    PK = input("Have you watched Pokemon y/n ")
    if PK == "y":
        age.append(15)
        age.append(60)
    elif PK == "n":
        age.append(0)
        age.append(16)
        age.append(61)
        age.append(100)
    else:
        print("False input")
        break
    PC = input("Did you get pc last year y/n ")
    if PC == "y":
        age.append(10)
        age.append(13)
    elif PC == "n":
        age.append(0)
        age.append(9)
        age.append(14)
        age.append(100)
    else:
        print("False input")
        break
    M = input("Did you get married this year y/n ")
    if M == "y":
        age.append(25)
        age.append(35)
    elif M == "n":
        age.append(0)
        age.append(24)
        age.append(36)
        age.append(100)
    else:
        print("False input")
        break
    FI = input("Do you live in Finland y/n ")
    if FI == "y":
        age.append(40)
        age.append(44)
    elif FI == "n":
        age.append(0)
        age.append(39)
        age.append(45)
        age.append(100)
    V = input("Did you lose your virginity within a year y/n ")
    if V == "y":
        age.append(15)
        age.append(20)
    elif V == "n":
        age.append(0)
        age.append(14)
        age.append(21)
        age.append(100)
    SM = input(f"Have you started smoking within a year y/n ")
    if SM == "y":
        age.append(13)
        age.append(18)
    elif SM == "n":
        age.append(0)
        age.append(12)
        age.append(19)
        age.append(100)
    else:
        print("False input")
        break
    CO = input("Are you in lukio or amis y/n ")
    if CO == "y":
        age_limiter.append(16)
        age_limiter.append(21)
    elif CO == "n":
        anti_limiter.append(16)
        anti_limiter.append(21)
    else:
        print("False input")
        break
    for i in range(0,len(age),2):
        ava += (age[i-1] + age[i]) / 2
    av = ava/(len(age)/2)
    if len(age_limiter) > 0:
        if av > age_limiter[1] or av < age_limiter[0]:
            if av > age_limiter[1]:
                print(f"Your age is about {age_limiter[1]} years but your soul is about {av} years old ")
            else:
                print(f"Your age is about {age_limiter[0]} years but your soul is about {av} years old ")
        else:
            print(f"Your age is about {av} years ")
    elif len(anti_limiter) > 0:
        if av > anti_limiter[1] or av < anti_limiter[0]:
            if av > anti_limiter[1]:
                print(f"Your age is about {av} years ")
            else:
                print(f"Your age is about {av} years ")
        else:
            print(f"Your age is less than 16 or more than 21 but your soul is like an collage student ")
    break