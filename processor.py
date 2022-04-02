#!/usr/bin/python3

import random
import threading
import time






color = [None] * 16
color[15] = '\033[34m' # blue
color[14] = '\033[31m' # red
color[13] = '\033[32m' # green
color[12] = '\033[30m' # blue
color[11] = '\033[35m' # purple
color[0] = '\033[0m' # white (normal)
white = '\033[0m'  # white (normal)











# checks if there is a interupt in the queue with a higher interput level than the current task
# if there is one it wil be excudet without schedule
# except another interupt will be triggered with a higher level

def interruptController(currentLevel):
    level = currentLevel
    i = 0
    for program in programs:
        if(program.interuptLevel > level):
            level = program.interuptLevel
            programNumber = i
        i += 1
    # start interupt, if found a higher interupt
    if (level>currentLevel):
        for steps in programs[programNumber].program:
            calculate(steps, level)
            programs[programNumber].pointer += 1
        programs.remove(programs[programNumber])



# scheduler
# updates the command queue with all currently running programs

# var programs = array with all running programs
# var tasks = how many commands will be executed per period

def scheduler(programs, tasks):
  #  length = sum(len(x) for x in programs)
    i = 0
    global currentProgram
    currentProgram = 0
    while(True):
        if (len(programs)<1):
            calculate(["idle", 0 ,0 ,0 ,0], 0)
        while currentProgram < len(programs):
                while programs[currentProgram].pointer < len(programs[currentProgram].program):
                    calculate(programs[currentProgram].program[programs[currentProgram].pointer], 0)
                    programs[currentProgram].pointer += 1
                    if ((i + 1) % tasks == 0):
                        if (currentProgram < len(programs) - 1):
                            currentProgram += 1
                        else:
                          currentProgram = 0
                    i += 1
                if (programs[currentProgram].pointer == len(programs[currentProgram].program)):
                    programs.remove(programs[currentProgram])
                    if (currentProgram > 0):
                        currentProgram -= 1



# generates a program with "add", "sub", "mul", "div" according the length

def generateProgram(size):
    comands = ["add", "sub", "mul", "div"]
    program = []
    for step in range(size):
        step = []
        step.append(random.choice(list(comands)))
        step.append(random.randint(1, 31))
        step.append(random.randint(1, 31))
        program.append(step)
    return program





# class for programs

class Program:
  def __init__(self, content, interuptLevel = 0):
    self.program = content
    self.pointer = 0
    self.interuptLevel = interuptLevel





# cpu with commands "add", "sub", "mul", "div", "print", "jump", "start"

def calculate(currentStep, level):
        global cycle
        global currentProgram
        print(str(len(result))+ "   " + str(cycle) + "    " + currentStep[0])
        interruptController(level)
        if (currentStep==None):
            return
        if(type(currentStep[1]) == int):
            currentChache1 = speicher[currentStep[1]]
            currentChache2 = speicher[currentStep[2]]
        else:
            currentChache1 = currentStep[1]
            currentChache2 = currentStep[2]
        if(currentStep[0]=="add"):
            result.append(currentChache1 + currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1])+ "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "+" + str(currentChache2) + "=" + str(result[cycle]))
        elif (currentStep[0] == "sub"):
            result.append(currentChache1 - currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "-" + str(currentChache2) + "=" + str(currentChache1 - currentChache2))
        elif (currentStep[0] == "mul"):
            result.append(currentChache1 * currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "X" + str(currentChache2) + "=" + str(currentChache1 * currentChache2))
        elif (currentStep[0] == "div"):
            if (currentChache2 == 0):
                result.append("Error : div0")
                startProgram(1)
            else:
                result.append(currentChache1 / currentChache2)
                print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "/" + str(currentChache2) + "=" + str(currentChache1 / currentChache2))
        elif (currentStep[0] == "jump"):
            if (currentStep[1]+1 > len(programs[currentProgram].program)):
                result.append("jump to " + str(currentChache1) + " not possible")
                startProgram(2)
            else:
                result.append("jump to " + str(currentChache1))
                result.append("jump to " + str(currentChache1))
                print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  to program position = " + str(currentChache1) + " from memory position= " + str(currentStep[1]))
                programs[currentProgram].pointer = currentChache1
        elif (currentStep[0] == "print"):
            result.append("echo: " + currentChache1)
            print(color[level] + "Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  echo: " + currentChache1 + color[0])
        elif (currentStep[0] == "start"):
            if (currentChache1 < len(avaiblePrograms)):
                result.append("program number " + str(currentChache1) + "started")
                print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[4]) + "   Imput: opration = " + currentStep[0] + "  program number = " + str(currentChache1))
            else:
                result.append("Error : not avaible")
                startProgram(3)
        elif (currentStep[0] == "idle"):
            print("Step: " + str(0) + "   Processor Number: " + str(1) + "   is idle")
            cycle -= 1
        time.sleep(0.3)

        cycle += 1






def addProgram(program, interupt = 0):
    if len(program[0])==3:
        k = 0
        for step in program:
            step.append(len(programs))
            step.append(k)
            k += 1
    pg = Program(program, interupt)
    avaiblePrograms.append(pg)
    if (interupt < 1):
        programs.append(pg)
    return pg


def startProgram(number):
    pg = avaiblePrograms[number]
    for step in pg.program:
        step[3] = len(programs)
    programs.append(pg)









def startSystem():
    global cycle
    cycle = 0
    global interuptLevel
    interuptLevel = 0
    global speicher
    speicher = random.sample(range(100), 32)
    global result
    result = []
#    programCounter = 0
    global programs
    programs = []
    global avaiblePrograms
    avaiblePrograms = []

    # load interupts

    isr1 = [["print","Fatel Error",0],["print","BlueScreen",0],["print","!!!!!!!!!",0]]
    addProgram(isr1, 15)
    isr2 = [["print", "Program tries division with 0",0],["print", "Division with 0 is not allowed", 0],["print","Process killed", 0],["print","!!!!!!!!!",0]]
    addProgram(isr2, 14)
    isr3 = [["print", "Jump adress is out of range", 0],["print", "Jump will not be executed", 0],["print", "Process is continue", 0],["print", "!!!!!!!!!", 0]]
    addProgram(isr3, 13)
    isr4 = [["print", "Program is not avaible", 0],["print", "Program has to be loaded", 0],["print", "Process is continue", 0],["print", "!!!!!!!!!", 0]]
    addProgram(isr4, 12)
    isr5 = generateProgram(10)
    addProgram(isr5, 11)

    # start scheduler
    scheduler(programs, 3)




def runPrograms():
    program1 = generateProgram(10)
    addProgram(program1)
    time.sleep(1.5)
    program2 = generateProgram(10)
    addProgram(program2)
    time.sleep(8)
    program3 = generateProgram(30)
    addProgram(program3)
    time.sleep(1.5)
    startProgram(1)
    time.sleep(1)
    program4 = [["add", 1, 2], ["mul", 3, 4], ["add", 5, 3], ["add", 1, 6], ["sub", 7, 4], ["div", 7, 8], ["sub", 7, 4],["mul", 7, 8]] #,["start", 6, 0],["start", 16, 0]]
    addProgram(program4)
    time.sleep(1)
    program5 = [["add", 11, 9], ["mul", 13, 10], ["add", 15, 13], ["add", 11, 16], ["sub", 13, 9], ["div", 13, 16],["sub", 11, 9], ["jump", 16, 0], ["mul", 11, 12]]
    addProgram(program5)




def runPrograms3():
    time.sleep(2)
    program3 = generateProgram(16)
    addProgram(program3)
    time.sleep(2)
    startProgram(0)


















    generateProgram(16)

    # programs = [[["add", 1 , 2], ["mul", 3 , 4],["add" , 5, 3] , ["add", 1 , 6] , [ "sub", 7 , 4], ["div", 7 , 8] ,["sub", 7 , 4] ,["mul", 7 , 8]],[["add", 11 , 9], ["mul", 13 , 10],["add" , 15, 13] , ["add", 11 , 16] , [ "sub", 13 , 9], ["div", 13 , 16] ,["sub", 11 , 9] ,["mul", 11 , 12]]]


    program3 = generateProgram(10)



















# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # settings:
    global tasks
    # how many tasks the scheduler will execute before switching
    tasks = 3
    global clock
    # cpu clock in seconds
    clock = 0.3


    system = threading.Thread(target=startSystem)
    user = threading.Thread(target=runPrograms)
    system.start()
    time.sleep(0.5)

    # start user programs
    user.start()















