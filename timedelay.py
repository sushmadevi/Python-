import time
s1 = "You have two options:"
s2 = "Welcome to 'The Enchanted Forest'!"
time.sleep(1)
#loops trough to the end of the sentence1
l1=s1.split()
l2=s2.split()
#print(l1)
#print(l2)

def m1():
    for w in l1:
        print(w)
        time.sleep(2)
m1()

def m2():
    for w in l2:
        print(w)
        time.sleep(2)
m2()    
#for x in range (0,len(l1)):
    #print(l1)
    #time.sleep(2)


#for w in l1
    #print(w\)
    #time.sleep(2)

#for x in sentence1:
#for x in range (0,len(sentence1)):
    # if a space is found print the letter
