from sys import stdin

def b_d(bin):
    '''Converts binary to decimal'''

    assert type(bin) == str, "the input to b_d function is not a string"

    ans = 0
    bin = bin[::-1]

    for i in range(len(bin)):

        assert bin[i] == "0" or bin[i] == "1", "Wrong bin format"

        ans += 2 ** i * (int(bin[i]))

    return ans

def d_b(dec):
    '''Converts decimal to binary'''

    assert type(dec) == int, "The input to this funciton is not an integer"

    assert dec >= 0, "The input is negative"
    ans = ""

    while dec > 0:

        ans = ans + str(dec % 2)
        dec //= 2

    return ans[::-1]

def MEM(bit):
    assert type(bit) == int and bit >= 0 and bit < 256, "The input is not an integer between 0 (including 0) and 256 (excluding 256)"

    global memory

    return memory[bit]

def reg_value(bin):
    '''Function to get a value stored in a register'''

    global regs
    
    assert type(bin) == str and len(bin) == 3, "The input to this function is not a string of 3 characters"

    return b_d(regs[b_d(bin)])

def inc_pc():

    global new_pc
    global pc

    new_pc = pc + 1

    return

def add(instr):

    global regs
    global changed

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    reg3 = reg1 + reg2

    b_reg3 = d_b(reg3)
    
    if len(b_reg3) > 16:
        b_reg3 = b_reg3[-16:]
        regs[7] = "0" * 16
        regs[7] = regs[7][:-4] + "1" + regs[7][-3:]
        changed = True

    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def sub(instr):
    
    global regs
    global changed

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    reg3 = reg1 - reg2

    if reg3 < 0:

        b_reg3 = "0" * 16
        regs[7] = "0" * 16
        regs[7] = regs[7][:-4] + "1" + regs[7][-3:]
        changed = True
    
    else:

        b_reg3 = d_b(reg3)
    
    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def mov_B(instr):

    global regs

    reg1_b = "0" * 8 + instr[-8:]
    regs[b_d(instr[5:8])] = reg1_b

    inc_pc()

    return

def mov_C(instr):

    global regs

    regs[b_d(instr[13:])] = regs[b_d(instr[10:13])]

    inc_pc()

    return

def ld(instr):

    global regs

    regs[b_d(instr[5:8])] = MEM(b_d(instr[8:]))

    inc_pc()
    
    return

def st(instr):

    global regs
    global memory

    memory[b_d(instr[8:])] = regs[b_d(instr[5:8])]

    inc_pc()

    return

def mul(instr):
    
    global regs
    global changed

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    reg3 = reg1 * reg2

    b_reg3 = d_b(reg3)
    
    if len(b_reg3) > 16:
        b_reg3 = b_reg3[-16:]
        regs[7] = "0" * 16
        regs[7] = regs[7][:-4] + "1" + regs[7][-3:]
        changed = True

    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def div(instr):

    global regs

    reg3 = reg_value(instr[10:13])
    reg4 = reg_value(instr[13:])

    b_reg0 = d_b(reg3 // reg4)
    b_reg1 = d_b(reg3 % reg4)

    regs[0] = "0" * (16 - len(b_reg0)) + b_reg0
    regs[1] = "0" * (16 - len(b_reg1)) + b_reg1

    inc_pc()

    return

def rs(instr):

    global regs

    imm = b_d(instr[8:])

    if (imm < 16):
        regs[b_d(instr[5:8])] = "0" * imm + regs[b_d(instr[5:8])][:16 - imm]
    
    else:
        regs[b_d(instr[5:8])] = "0" * 16

    inc_pc()
    
    return

def ls(instr):

    global regs

    imm = b_d(instr[8:])

    if (imm < 16):
        regs[b_d(instr[5:8])] = regs[b_d(instr[5:8])][imm:] + "0" * imm
    
    else:
        regs[b_d(instr[5:8])] = "0" * 16

    inc_pc()
    
    return

def xor(instr):

    global regs

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    b_reg3 = d_b(reg1 ^ reg2)

    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def or_0(instr):

    global regs

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    b_reg3 = d_b(reg1 | reg2)

    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def and_0(instr):

    global regs

    reg1 = reg_value(instr[7:10])
    reg2 = reg_value(instr[10:13])

    b_reg3 = d_b(reg1 & reg2)

    regs[b_d(instr[13:])] = "0" * (16 - len(b_reg3)) + b_reg3

    inc_pc()

    return

def not_0(instr):

    global regs

    for i in range(16):

        if regs[b_d(instr[10:13])][i] == "0":
            regs[b_d(instr[13:])][i] = "1"

        else:
            regs[b_d(instr[13:])][i] = "0"

    inc_pc()
    
    return

def cmp(instr):

    global regs
    global changed

    reg1 = reg_value(instr[10:13])
    reg2 = reg_value(instr[13:])
    
    if reg1 < reg2:

        regs[7] = "0" * 16
        regs[7] = regs[7][:-3] + "1" + regs[7][-2:]
        changed = True
    
    elif reg1 > reg2:

        regs[7] = "0" * 16
        regs[7] = regs[7][:-2] + "1" + regs[7][-1:]
        changed = True
    
    else:

        regs[7] = "0" * 16
        regs[7] = regs[7][:-1] + "1"
        changed = True

    inc_pc()
    
    return

def jmp(instr):

    global new_pc

    new_pc = b_d(instr[8:])

    return

def jlt(instr):

    global new_pc
    global regs

    if regs[7][-3] == "1":

        new_pc = b_d(instr[8:])
    
    else:
        
        inc_pc()
    
    return

def jgt(instr):

    global new_pc
    global regs

    if regs[7][-2] == "1":

        new_pc = b_d(instr[8:])
    
    else:

        inc_pc()

    return

def je(instr):

    global new_pc
    global regs

    if regs[7][-1] == "1":

        new_pc = b_d(instr[8:])
    
    else:

        inc_pc()

    return

def hlt(instr):

    global halted

    halted = True

    inc_pc()

    return

def addf(instr):

    global regs
    global changed
    
    b_reg1 = regs[b_d(instr[7:10])][8:]
    b_reg2 = regs[b_d(instr[10:13])][8:]

    reg1 = b_d("1" + b_reg1[3:]) * (2 ** b_d(b_reg1[:3]))
    reg2 = b_d("1" + b_reg2[3:]) * (2 ** b_d(b_reg2[:3]))

    b_reg3_0 = d_b(reg1 + reg2)
    
    if len(b_reg3_0) > 13:
        regs[b_d(instr[13:])] = "0" * 8 + "1" * 8
        regs[7] = "0" * 12 + "1" + "0" * 3
        changed = True
    
    else:
        if len(b_reg3_0) < 7:
            exponent = "000"
        else:
            exponent = d_b(len(b_reg3_0) - 6)
        if (len(b_reg3_0) <= 6):

            regs[b_d(instr[13:])] = "0" * 8 + "0" * (3 - len(exponent)) + exponent + b_reg3_0[1:] + "0" * (6 - len(b_reg3_0))
        
        else:
            
            regs[b_d(instr[13:])] = "0" * 8 + "0" * (3 - len(exponent)) + exponent + b_reg3_0[1:6]
    
    inc_pc()
    
    return

def subf(instr):

    global regs
    global changed
    
    b_reg1 = regs[b_d(instr[7:10])][8:]
    b_reg2 = regs[b_d(instr[10:13])][8:]

    reg1 = b_d("1" + b_reg1[3:]) * (2 ** b_d(b_reg1[:3]))
    reg2 = b_d("1" + b_reg2[3:]) * (2 ** b_d(b_reg2[:3]))

    reg3 = reg1 - reg2

    if (reg3 < 32):
        regs[b_d(instr[13:])] = "0" * 16
        regs[7] = "0" * 12 + "1" + "0" * 3
        changed = True
    
    else:
        b_reg3_0 = d_b(reg3)
        exponent = d_b(len(b_reg3_0) - 6)
        regs[b_d(instr[13:])] = "0" * 8 + "0" * (3 - len(exponent)) + exponent + b_reg3_0[1:6]
    
    inc_pc()
    
    return

def movf(instr):

    regs[b_d(instr[5:8])] = "0" * 8 + instr[8:]

    inc_pc()

    return

def EE(pc):

    global regs
    global changed

    changed = False

    instr = MEM(pc)

    assert type(instr) == str, "The instruction is not a string"
    # if len(instr) != 16:
    #     print(instr)
    assert len(instr) == 16, f"Instruction is not a string of 16 characters, instruction is a{instr}a and length of it is a{instr}"

    opcode = instr[:5]

    if (opcode == "10000"):
        add(instr)
     
    elif (opcode == "10001"):
        sub(instr)
    
    elif (opcode == "10010"):
        mov_B(instr)
    
    elif (opcode == "10011"):
        mov_C(instr)
    
    elif (opcode == "10100"):
        ld(instr)
    
    elif (opcode == "10101"):
        st(instr)
    
    elif (opcode == "10110"):
        mul(instr)
    
    elif (opcode == "10111"):
        div(instr)
    
    elif (opcode == "11000"):
        rs(instr)
    
    elif (opcode == "11001"):
        ls(instr)
    
    elif (opcode == "11010"):
        xor(instr)
    
    elif (opcode == "11011"):
        or_0(instr)
    
    elif (opcode == "11100"):
        and_0(instr)
    
    elif (opcode == "11101"):
        not_0(instr)
    
    elif (opcode == "11110"):
        cmp(instr)
    
    elif (opcode == "11111"):
        jmp(instr)
    
    elif (opcode == "01100"):
        jlt(instr)
    
    elif (opcode == "01101"):
        jgt(instr)
    
    elif (opcode == "01111"):
        je(instr)
    
    elif (opcode == "01010"):
        hlt(instr)
    
    elif (opcode == "00000"):
        addf(instr)
    
    elif (opcode == "00001"):
        subf(instr)
    
    elif (opcode == "00010"):
        movf(instr)
    
    else:
        assert False, "Inavlid opcode"

    if (not (changed)):
        regs[7] = "0" * 16

def initialise_m():
    '''To create a list of memory with all values as 0'''

    x = []

    for i in range(256):

        x.append("0" * 16)

    return x

def dump_pc(pc):

    print(pc, end = " ")

    return

def dump_rf(rf):

    for i in range(7):
        print(rf["R" + str(i)], end = " ")
    
    print(rf["FLAGS"])

    return

def mem_dump(memory):

    for i in range(256):
        print(memory[i])
    
    return

changed = False     #A variable to know if FLAGS register has been changed in the current instruction

halted = False

regs = []

for i in range(8):
    regs.append("0" * 16)

memory = initialise_m()

i = 0

for line in stdin:

    if len(line) != 16:
        memory[i] = line[:-1]
        i += 1
    
    else:
        memory[i] = line
        i += 1

RF = {}

for i in range(7):

    RF["R" + str(i)] = "0" * 16

RF["FLAGS"] = "0" * 16

pc = 0
new_pc = 0

PC = "0" * 8

while not(halted):

    EE(pc)
    dump_pc(PC)

    for i in range(7):
        RF["R" + str(i)] = regs[i]
    
    RF["FLAGS"] = regs[7]

    dump_rf(RF)
    pc = new_pc
    PC = "0" * (8 - len(d_b(pc))) + d_b(pc)

mem_dump(memory)
