# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Strg+F8 to toggle the breakpoint.







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




def calculate(level):
    print("start")
    print(len(befehlsspeicher[0]))
    i = 0
    j = 0
    for step in range(len(befehlsspeicher)):
        currentStep = befehlsspeicher[step]
        if (interuptLevel < level):
            calculate(interuptLevel)
        if (currentStep==None):
            break
        currentChache1 = speicher[currentStep[1]]
        currentChache2 = speicher[currentStep[2]]
        if(currentStep[0]=="add"):
            result[j] = currentChache1 + currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1])+ "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "+" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "sub"):
            result[j] = currentChache1 - currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "-" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "mul"):
            result[j] = currentChache1 * currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "X" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "div"):
            result[j] = currentChache1 / currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "/" + str(currentChache2) + "=" + str(result[j]))
        elif (currentStep[0] == "div"):
            result[j] = currentChache1 / currentChache2
            print("Step: " + str(j) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(
                currentChache1) + "/" + str(currentChache2) + "=" + str(result[j]))

        j += 1



def addProgram():





# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    interuptLevel = 0


    befehlsspeicher = [None] * 32
    speicher = random.sample(range(100),32)
    print(speicher)
    result = [0 for i in range(100)]
    programs = [[["add", 1 , 2], ["mul", 3 , 4],["add" , 5, 3] , ["add", 1 , 6] , [ "sub", 7 , 4], ["div", 7 , 8] ,["sub", 7 , 4] ,["mul", 7 , 8]],[["add", 11 , 9], ["mul", 13 , 10],["add" , 15, 13] , ["add", 11 , 16] , [ "sub", 13 , 9], ["div", 13 , 16] ,["sub", 11 , 9] ,["mul", 11 , 12]]]
    print(befehlsspeicher)


    update_comands(programs, 3)

    calculate()

    print("finish")
    print(befehlsspeicher)







# See PyCharm help at https://www.jetbrains.com/help/pycharm/
