def entro():
    print("Follow the Path")
    choosePath = input("which path will you choose? (Left/Right): ")
    if choosePath == 'Left':
        print("Left")
        print("Left")
    elif choosePath == 'Right':  
        print("Right") 

print()
print()
print("    ##################")
print("    #                #")
print("    # Advanture Game #")
print("    #                #")
print("    ##################")
print()
print()
print()
print("Lets start game Enter the Forest ")
StartGame = input("Do want to to Enter the Forest? (Y/N): ")
if StartGame== 'n' or StartGame== 'N':
    print("may be next time")
elif StartGame== 'y' or StartGame== 'Y':
    entro()