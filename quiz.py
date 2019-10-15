# questions :-
question=[["You should save your computer from?",
           "(a)Viruses  (b)Time bombs  (c)Worms  (d)All of the above","d"],

          ["Full form of WWW is?",
           "(a)Wip World Wide  (b)Wold wide web  (c)World Wide Web  (d)W3school","c"],

          ["What chip is used inside the apple new computers?",
           "(a)G3  (b)G4  (c)ATI  (d)MAC03","a"],

          ["Who is Father of computer?",
           "(a)Charles Newman  (b)Charles Babbage  (c)Henry Babbage  (d)Henry Luca","b"],

          ["Operating system used in which genretion of computer for first time?",
           "(a)1st gen.  (b)2nd gen.  (c)3rd gen.  (d)4th gen.","c"],

          ["Which is the most common type of computer?",
           "(a)Desktop  (b)Notebook  (c)Server  (d)Laptop","a"],

          ["Which is first computer in INDIA?",
           "(a)ENIAC  (b)HEC-2M  (c)SZ 40/42  (d)Harwell CADET","b"],

          ["____ are software which is used to do particular task?",
           "(a)OS  (b)Program  (c)Data  (d)Software","b"],

          ["How many genration of computer we have?",
           "(a)6  (b)7  (c)5  (d)4","c"],

          ["The term \'pentium\' is related to ?",
           "(a)DVD  (b)Hard Disk  (c)Microprocessor  (d)Mouse","c"]

        ]

# game :-
name=input("Enter your name: ")
name=name.upper()
print ("                           Hello "+name)
print ("lets start :-")
print ("""Read question and options.
          and enter the a,b,c,d according to your answer.""")
input("Press enter to continue....")
total=len(question)
score=0
for i in range(0,len(question)):
    print("-----------------------------------------------------")
    print("("+str(i+1)+") "+question[i][0])
    print("     "+question[i][1])
    a=input("Enter answer: ")
    a=a.lower()
    if(a=='a' or a=='b' or a=='c' or a=='d'):
        if(a==question[i][2]):
            score+=1
            print("             ======  right  ======")
        else:
            print("             ======  wrong  ======("+question[i][2]+")")
    else:
        print(" wrong input !")
# result :-
per=(score/total)*100
print("-----------------------------------------------\n")
print(name+" you got "+str(score)+"/"+str(total)+" marks.")
print("Your Brain level is "+str(per)+"%")
print("\n-----------------------------------------------")


        