# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random
import threading
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
   #     print(programs[currentProgram][programPoint[currentProgram]-1])
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

def scheduler(programs, tasks):
  #  length = sum(len(x) for x in programs)
    i = 0
    currentProgram = 0

    while(True):
        for prog in programs:
                for step in prog.program:
                    calculate(step, 0)
                    prog.pointer += 1
                    if ((i + 1) % tasks == 0):
                        if (currentProgram < len(programs) - 1):
                             currentProgram += 1
                        else:
                          currentProgram = 0
                    i += 1










class Program:
  def __init__(self, content , interuptLevel = 0):
    self.program = content
    self.pointer = 0
    self.interuptLevel  = interuptLevel






def calculate(currentStep, level):
        global cycle
        if (interuptLevel < level):
            calculate(interuptLevel)
        if (currentStep==None):
            return
        currentChache1 = speicher[currentStep[1]]
        currentChache2 = speicher[currentStep[2]]
        if(currentStep[0]=="add"):
            result.append(currentChache1 + currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1])+ "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "+" + str(currentChache2) + "=" + str(result[cycle]))
        elif (currentStep[0] == "sub"):
            result.append(currentChache1 - currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "-" + str(currentChache2) + "=" + str(result[cycle]))
        elif (currentStep[0] == "mul"):
            result.append(currentChache1 * currentChache2)
            print("Step: " + str(cycle) +  "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "X" + str(currentChache2) + "=" + str(result[cycle]))
        elif (currentStep[0] == "div"):
            result.append(currentChache1 / currentChache2)
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  Value 1 = " + str(currentChache1) + " from memory position= " + str(currentStep[1]) + "  Value 2 = " + str(currentChache2) + " from memory position = " + str(currentStep[2]) + "  operation = " + str(currentChache1) + "/" + str(currentChache2) + "=" + str(result[cycle]))
        elif (currentStep[0] == "jump"):
            result.append("jump to " + str(currentChache1))
            print("Step: " + str(cycle) + "   Program Number: " + str(currentStep[3]) + "   Program step: " + str(currentStep[2]) + "   Imput: opration = " + currentStep[0] + "  to program position = " + str(currentChache1) + " from memory position= " + str(currentStep[1]))
        time.sleep(0.3)
        cycle += 1
        #
            # j = currentStep[1]-1





def addProgram(program):
    if len(program[0])==3:
        k = 0
        for step in program:
            step.append(len(programs))
            step.append(k)
            k += 1
    programs.append(Program(program))
    return program




def initProcess():
    global cycle
    cycle = 0
    global interuptLevel
    interuptLevel = 0
    global befehlsspeicher
    befehlsspeicher = [None] * 32
    global speicher
    speicher = random.sample(range(100), 32)
    print(speicher)
    global result
    result = []
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
    programCounter = addProgram(program1)
    print(programCounter)
    programCounter = addProgram(program2)
    print(programCounter)
    programCounter = addProgram(program1)
    print(programCounter)

    print(befehlsspeicher)

    scheduler(programs, 3)

    calculate(0)

    print("finish")
    print(befehlsspeicher)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    cpu = threading.Thread(target=initProcess())
  #  pic = threading.Thread(target=interrupt_controller_thread)

    cpu.start()
  #  pic.start()
  #  initProcess()














def interrupt_controller_thread():
  while True:
    global interrupt
    time.sleep(interrupt_interval)
    print("Triggering interrupt")
    interrupt=True

def cpu_handle_interrupt():
    global interrupt

    if interrupt == True:
      print("Woah I got an interrupt")
      # now act on the interrupt...
      interrupt = False

def cpu_thread():
  while True:
    # Read, Eval, (optional: Print), Loop
    print("I am reading the next instruction")
    print("I am evaluating the instruction")
    time.sleep(1) # python threading doesn't really work
    cpu_handle_interrupt()

cpu = threading.Thread( target = cpu_thread )
pic = threading.Thread( target = interrupt_controller_thread )

cpu.start()
pic.start()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
