from sys import stdin
import sys

def binary_convert(number, bits):
    '''Converts a numnber into binoary and masks it with "bits" bits'''
    if (number < 0):
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    
    binary_n = bin(number)

    if (len(binary_n) <= 10):

        return "0" * (bits - len(binary_n) + 2) + binary_n[2:]

    else:
        return binary_n[2:10]

def count_vars(line_list_0, len_list):
    """Counts the number of variables"""
    global i
    global offset
    vars = []

    if len_list == 0:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    
    line_cur = line_list_0[0].strip().split()

    while (line_cur[0] == "var" and i < len_list):
        if (len(line_cur) != 2):
            print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
            sys.exit()
        if line_cur[1] in vars:
            print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
            sys.exit()
        vars.append(line_cur[1])
        i += 1
        offset += 1
        if i < len_list:
            line_cur = line_list_0[i].strip().split()
    return vars

def first_iter(line_list_0, len_list):
    ''' we are making labels dictionary, list of all the lines '''
    global i
    labels = {}
    line_list = []
    address = 0

    while i < len_list:

        # print(i)

        line_cur = line_list_0[i].strip().split()

        if (line_cur == []):

            pass

        elif line_cur[0][-1] == ":":

            # if (line[0][-1] == ":"):
            if line_cur[0][0:-1] in vars or line_cur[0][0:-1] in labels:
                print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
                sys.exit()
            labels[line_cur[0][0:-1]] = binary_convert(address, 8)

            if len(line_cur) > 1:

                line_list.append(line_cur[1:])
                address += 1

            # else:
            #     labels[line[0]] = binary_convert(address, 8)

            '''Error handling'''

        else:

            line_list.append(line_cur)
            address += 1
        
        i += 1

        # print("in loop bruh")

    return [labels, line_list, address]

def make_var_dic(vars, len_vars, len_line_list):
    var_dic = {}

    for i in range(len_vars):

        var_dic[vars[i]] = binary_convert(len_line_list + i, 8)
    
    return var_dic

def make_reg_dic(n):

    register_dic = {}

    for i in range(n - 1):

        register_dic["R" + str(i)] = binary_convert(i, 3)
        register_dic["r" + str(i)] = register_dic["R" + str(i)]
    
    register_dic["FLAGS"] = "111"
    return register_dic

def typeA(line_arr,dic_type_a,reg_dic, line_address, offset, i):
    if len(line_arr) != 4:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    if line_arr[0] in dic_type_a:
        print(dic_type_a[line_arr[0]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in instruction name")
        sys.exit()

    print("00",end='')

    if line_arr[1] in reg_dic:
        if (line_arr[1] == "FLAGS"):
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        else:
            print(reg_dic[line_arr[1]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()

    if line_arr[2] in reg_dic:
        if (line_arr[2] == "FLAGS"):
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        else:
            print(reg_dic[line_arr[2]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()
    
    if line_arr[3] in reg_dic:
        if line_arr[3] == "FLAGS":
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        else:
            print(reg_dic[line_arr[3]])

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()

def typeC(line_arr,dic_type_c,reg_dic, line_address, offset, i):


    if len(line_arr) != 3:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    if line_arr[0] in dic_type_c:
        print(dic_type_c[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        sys.exit()

    print("00000",end='')

    if line_arr[1] in reg_dic:
        print(reg_dic[line_arr[1]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()
    

    if line_arr[2] in reg_dic:
        if line_arr[2] == "FLAGS":
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        else:
            print(reg_dic[line_arr[2]])

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()

def typeB(line_arr,reg_dic,dic_type_b, line_address, offset, i):

    if len(line_arr) != 3:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    if line_arr[0] in dic_type_b:
        print(dic_type_b[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        sys.exit()
    
    if line_arr[1] in reg_dic:
        if line_arr[1] == "FLAGS":
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        print(reg_dic[line_arr[1]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()    
    
    if line_arr[2][0]=="$":
        try:
            temp = int(line_arr[2][1:])
        except:
            print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
            sys.exit()
        if (int(line_arr[2][1:]) >= 256):
            print(f"\nError in line {line_address[i + offset] + 1}:\nIllegal immediate values (more than 8 bits)")
            sys.exit()
        else:
            print(binary_convert(int(line_arr[2][1:]),8))
    
    else:
        print("Wrong syntax of immediate value")
        sys.exit()

def typeD(line_arr,label_dic,dic_type_d,reg_dic, line_address, offset, i):
    if len(line_arr) != 3:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    if line_arr[0] in dic_type_d:
        print(dic_type_d[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        sys.exit()

    if line_arr[1] in reg_dic:
        if (line_arr[1] == "FLAGS"):
            print(f"\nError in line {line_address[offset + i] + 1}:\nIllegal use of FLAGS register")
            sys.exit()
        else:
            print(reg_dic[line_arr[1]],end='')

    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in register name")
        sys.exit()

    if line_arr[2] in label_dic:
        print(label_dic[line_arr[2]])
    
    elif line_arr[2] in labels:
        print(f"\nError in line {line_address[i + offset] + 1}:\nMisuse of lables as variables")
        sys.exit()
    
    else:
        print(f"\nError in line {line_address[i + offset] + 1}:\nUse of undefined variables")
        sys.exit()

def typeE(line_arr,label_dic,dic_type_e, line_address, offset, i):

    if len(line_arr) != 2:
        print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
        sys.exit()
    if line_arr[0] in dic_type_e:
        print(dic_type_e[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        sys.exit()

    print("000",end='')

    if line_arr[1] in label_dic:
        print(label_dic[line_arr[1]])
    
    elif line_arr[1] in var_dic:
        print(f"\nError in line {line_address[i + offset] + 1}:\nMisuse of variables as lables")
        sys.exit()
    
    else:
        print(f"\nError in line {line_address[i + offset] + 1}\nUse of undefined labels")
        sys.exit()

def typeF():
    print("0101000000000000")
    return

# with open("test_text.txt", "r") as file:
#     line_string = file.read()
try:
    line_list_0 = []
    hlt = False
    line_no = 0
    line_address = []
    for line in stdin:

        if line != "":
            line_address.append(line_no)
            line_list_0.append(line)
        
        line_no += 1

    # line_list_0 = line_string.split("\n")

    len_line_list_0 = len(line_list_0)
    i = 0
    offset = 0
    vars = count_vars(line_list_0, len_line_list_0)
    len_vars = len(vars)

    if i >= len_line_list_0:
        print(f"\nError:\nMissing hlt instruction")
        sys.exit()

    # print(vars)
    # print(line_list_0)

    temp_list = first_iter(line_list_0, len_line_list_0)
    labels = temp_list[0]
    line_list = temp_list[1]
    len_line_list = temp_list[2]

    # print(labels)
    # print(line_list)

    var_dic = make_var_dic(vars, len_vars, len_line_list)

    # print(var_dic)

    register_dic = make_reg_dic(8)

    # print(register_dic)

    TypeA = {'add':"10000" , 'sub':"10001" , 'mul':"10110" , 'xor':"11010" , 'or':"11011" , 'and':"11100" }
    TypeB = {'mov':"10010" , 'ls':"11001" ,'rs':"11000" }
    TypeC = {'mov':"10011" , 'div':"10111" , 'not':"11101" , 'cmp':"11110" }
    TypeD = {'ld':"10100" , 'st':"10101" }
    TypeE = {'jmp':"11111" , 'jlt':"01100" , 'jgt':"01101" , 'je':"01111" }
    TypeF = {'hlt':"01010" }

    # print(line_list)
    # print(var_dic)
    # print(register_dic)
    # print(labels)
    # print(line_address)
    # print(offset)

    if (len_line_list + len_vars > 256):
        print(f"\nError:\nNot enough Memory")
        sys.exit()

    for i in range(len_line_list):
        if (hlt == True):
            print(f"\nError in line {line_address[i + offset] + 1}:\nhlt is not the last instruction")
            sys.exit()
        if (line_list[i][0] in TypeA):
            typeA(line_list[i], TypeA, register_dic, line_address, offset, i)
        
        elif (line_list[i][0] in TypeB):

            if (line_list[i][0] == "mov"):

                if (line_list[i][-1][0] == "$"):
                    typeB(line_list[i], register_dic, TypeB, line_address, offset, i)
                
                else:
                    typeC(line_list[i], TypeC, register_dic, line_address, offset, i)
                
            else:
                typeB(line_list[i], register_dic, TypeB, line_address, offset, i)
            
        elif (line_list[i][0] in TypeC):
            typeC(line_list[i], TypeC, register_dic, line_address, offset, i)

        elif (line_list[i][0] in TypeD):
            typeD(line_list[i], var_dic, TypeD, register_dic, line_address, offset, i)

        elif (line_list[i][0] in TypeE):
            typeE(line_list[i], labels, TypeE, line_address, offset, i)

        elif (line_list[i][0] in TypeF):
            if len(line_list[i]) != 1:
                print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
                sys.exit()
            hlt = True
            typeF()
        
        elif (line_list[i][0] == "var"):
            print(f"\nError in line {line_address[i + offset] + 1}:\nVariables not declared at the beginning")
            sys.exit()
        else:
            print(f"\nError in line {line_address[i + offset] + 1}:\nTypos in instruction name")
            sys.exit()
    if (hlt == False):
        print(f"\nError:\nMissing hlt instruction")
        sys.exit()
except SystemExit:
    pass
except:
    print(f"\nError in line {line_address[i + offset] + 1}:\nGeneral Syntax Error")
    sys.exit()

#C:\Users\adish\OneDrive\Desktop\desktop\CSE112-22-Assignment-SimpleAssemblerSimulator-main\CSE112-22-Assignment-SimpleAssemblerSimulator-main\Assembler-Simulator_4_Simple_RISC\Simple-Assembler\SimpleAssembler.py
