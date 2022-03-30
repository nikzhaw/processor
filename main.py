# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.





# scheduler
# updates the command queue with all currently running programs

# var programs = array with all running programs
# var tasks = how many commands will be executed per period

def update_comands(programs, tasks):
    length = sum(len(x) for x in programs)
    i = 0
    currentProgram = 0
    programPoint = [0]*len(programs)

    for step in range(length):
   #     print(programs[currentProgram][programPoint[currentProgram]-1])
        print(programs[currentProgram][programPoint[currentProgram]-1])
        befehlsspeicher[i] = programs[currentProgram][programPoint[currentProgram]-1]

        print((i + 1) % tasks)
        if ((i+1) % tasks==0):

            if (currentProgram<len(programs)-1):
                currentProgram+=1
            else:
                currentProgram=0
        programPoint[currentProgram]+=1
        print(befehlsspeicher)
        i+=1




# scheduler
# updates the command queue with all currently running programs

# var programs = array with all running programs
# var tasks = how many commands will be executed per period

def update_comands(programs, tasks):
    length = sum(len(x) for x in programs)
    i = 0
    currentProgram = 0
    programPoint = [0]*len(programs)

    for step in range(length):
        print(programs[currentProgram][programPoint[currentProgram]-1])
        befehlsspeicher[i] = programs[currentProgram][programPoint[currentProgram]-1]

        print((i + 1) % tasks)
        if ((i+1) % tasks==0):

            if (currentProgram<len(programs)-1):
                currentProgram+=1
            else:
                currentProgram=0
        programPoint[currentProgram]+=1
        print(befehlsspeicher)
        i+=1






class Program:
  def __init__(self, content , interuptLevel = 0):
    self.program = content
    self.programPointer = 0
    self.interuptLevel  = interuptLevel





def calculate(level):
    print("start")
    print(len(befehlsspeicher[0]))
    i = 0
    j = 0
  #  for step in range(len(befehlsspeicher)):
    while i < len(befehlsspeicher):
        time.sleep(0.3)
        # currentStep = befehlsspeicher[step]
        currentStep = befehlsspeicher[j]
        if (interuptLevel < level):
            calculate(interuptLevel)
        if (currentStep==None):
            break
        currentChache1 = speicher[currentStep[1]]
        currentChache2 = speicher[currentStep[2]]
        if(currentStep[0]=="add"):
            result[j] = currentChache1 + currentChache2
            print("Step: " + str(j) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1])+ "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "+" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "sub"):
            result[j] = currentChache1 - currentChache2
            print("Step: " + str(j) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "-" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "mul"):
            result[j] = currentChache1 * currentChache2
            print("Step: " + str(j) +  "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "X" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "div"):
            result[j] = currentChache1 / currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "/" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "jump"):
            result[j] = "jump to " + str(currentChache1)
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  to program position = " + str(currentChache1) + " from memory position= " + str(currentStep[1]))
            j = currentStep[1]-1

        j += 1



def addProgram(program, programCounter):
    if len(program[0])==3:
        k = 0
        for step in program:
                step.append(programCounter)
                program
                step.append(k)
                k += 1
                print(step)
    programs.append(program)
    programCounter = programCounter + 1
    return programCounter




def initProcess():
    global interuptLevel
    interuptLevel = 0
    global befehlsspeicher
    befehlsspeicher = [None] * 32
    global speicher
    speicher = random.sample(range(100), 32)
    print(speicher)
    global result
    result = [0 for i in range(100)]
    programCounter = 0
    global programs
    programs = []
    # programs = [[["add", 1 , 2], ["mul", 3 , 4],["add" , 5, 3] , ["add", 1 , 6] , [ "sub", 7 , 4], ["div", 7 , 8] ,["sub", 7 , 4] ,["mul", 7 , 8]],[["add", 11 , 9], ["mul", 13 , 10],["add" , 15, 13] , ["add", 11 , 16] , [ "sub", 13 , 9], ["div", 13 , 16] ,["sub", 11 , 9] ,["mul", 11 , 12]]]
    program1 = [["add", 1, 2], ["mul", 3, 4], ["add", 5, 3], ["add", 1, 6], ["sub", 7, 4], ["div", 7, 8], ["sub", 7, 4],
                ["mul", 7, 8]]
    program2 = [["add", 11, 9], ["mul", 13, 10], ["add", 15, 13], ["add", 11, 16], ["sub", 13, 9], ["div", 13, 16],
                ["sub", 11, 9], ["jump", 0, 0], ["mul", 11, 12]]
    #   programs.append(program1)
    #  programs.append(program2)
    # programs.append(program1)
    programCounter = addProgram(program1, programCounter)
    print(programCounter)
    programCounter = addProgram(program2, programCounter)
    print(programCounter)
    programCounter = addProgram(program1, programCounter)
    print(programCounter)

    print(befehlsspeicher)

    update_comands(programs, 3)

    calculate(0)

    print("finish")
    print(befehlsspeicher)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    initProcess()







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
