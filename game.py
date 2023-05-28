import numpy as np


Capital = 10

# Function to simulate the game
def gameA():
    toss = np.random.randint(1,201)
    if toss <=101:
        return -1
    else:
        return +1

def gameB():
    if Capital%3 == 0:
        toss = np.random.randint(1,11)
        if toss <=9:
            return -1
        else:
            return +1
    else:
        toss = np.random.randint(1,5)
        if toss<=3:
            return +1
        else:
            return -1


if __name__ == "__main__":
    for i in range(10):
        print(" Current Capital: ", Capital)
        choice = input("Enter A for Game A and B for Game B: ")
        if choice == 'A' or choice == 'a':
            Capital += gameA()
        elif choice == 'B' or choice == 'b':
            Capital += gameB()
        else:
            print("Invalid choice")
            break
    print("Final Capital: ", Capital)
    