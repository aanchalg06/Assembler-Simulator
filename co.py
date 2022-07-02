
# line_arr means the line number passed to function in form of arr


def typeC(line_arr,dic_type_c,reg_dic):
    if line_arr[0] in dic_type_c:
        print(dic_type_c[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        quit()

    print("00",end='')

    if line_arr[1] in reg_dic:
        print(reg_dic[line_arr[1]],end='')

    else:
        print("Register not applicable")
        quit()

    if line_arr[2] in reg_dic:
        print(reg_dic[line_arr[1]],end='')

    else:
        print("Register not applicable")
        quit()


def typeB(line_arr,reg_dic,dic_type_b):
    if line_arr[0] in dic_type_b:
        print(dic_type_b[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        quit()
    
    if line_arr[1] in reg_dic:
        print(reg_dic[line_arr[1]],end='')

    else:
        print("Register not applicable")
        quit()    
    
    if line_arr[2][0]=="$":
        print(binary_convert(line_arr[2][1],8))
    
    else:
        print("Wrong syntax of immediate value")
        quit()

def typeD(line_arr,label_dic,dic_type_d,reg_dic):
    if line_arr[0] in dic_type_d:
        print(dic_type_d[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        quit()

    if line_arr[1] in reg_dic:
        print(reg_dic[line_arr[1]],end='')

    else:
        print("Register not applicable")
        quit()

    if line_arr[2] in label_dic:
        print(label_dic[line_arr[2]])
    
    else:
        print("no such label present in loop hence wrong memory address")
        quit()


def typeE(line_arr,label_dic,dic_type_e):
    if line_arr[0] in dic_type_e:
        print(dic_type_e[line_arr[0]],end='')

    else:
        print("Instruction invalid")
        quit()

    print("000",end='')

    if line_arr[2] in label_dic:
        print(label_dic[line_arr[2]])
    
    else:
        print("no such label present in loop hence wrong memory address")
        quit()


TypeA = {'add':"10000" , 'sub':"10001" , 'mul':"10110" , 'xor':"11010" , 'or':"11011" , 'and':"11100" }
TypeB = {'mov':"10010" , 'ls':"11001" ,'rs':"11000" }
TypeC = {'mov':"10011" , 'div':"10111" , 'not':"11101" , 'cmp':"11110" }
TypeD = {'ld':"10100" , 'st':"10101" }
TypeE = {'jmp':"11111" , 'jlt':"01100" , 'jgt':"01101" , 'je':"01111" }
TypeF = {'hlt':"01010" }
