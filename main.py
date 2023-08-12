import os

if __name__ == '__main__':
    print("Welcome Rac's Robospeaker")
    while True:
        x = input("Enter script: ")
        if x == "q":
            os.system("espeak 'by by'")
            break
        command = f"espeak {x}"
        os.system(command)
