import math

print("Your Query is related to : \n")
print("1 - ISA and Instructions \n")
print("2 - System Enhancement \n")
q_type=int(input("Kindly enter the query type : "))

def Log2(x):
    return (math.log10(x) /math.log10(2))
    

if (q_type==1):
    memory_size=input("Enter the space in memory : ").split()
    memory_type=str(input("Enter the memory addressing type : "))
    L_inst=int(input("Enter the length of one instruction : "))
    L_reg=int(input("Enter the length of register : "))

    if(memory_type=="Bit"):
        a=int(memory_size[0])
        b=memory_size[1]
        c=memory_size[2]
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
       
        powera=(math.ceil(Log2(int(a))))

        power=power+powera
        b_opcode=int(L_inst-(L_reg+power))
        b_filler=L_inst-((2*L_reg)+b_opcode)
        max_inst=2**b_opcode
        max_reg=(2**L_reg)
        print("Minimum bits needed to represent an address in this architecture : ",power)
        print("Number of bits needed by opcode :                                  ",b_opcode)
        print("Number of filler bits in Instruction type 2 :                      ",b_filler)
        print("Maximum numbers of instructions this ISA can support :             ",max_inst)
        print("Maximum number of registers this ISA can support :                 ",max_reg)

    elif(memory_type=="Nibble"):
        a=int(memory_size[0])
        b=memory_size[1]
        c=memory_size[2]
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/4)
       
        powera=(math.ceil(Log2(int(a))))

        power=power+powera
        b_opcode=int(L_inst-(L_reg+power))
        b_filler=L_inst-((2*L_reg)+b_opcode)
        max_inst=2**b_opcode
        max_reg=(2**L_reg)
        print("Minimum bits needed to represent an address in this architecture : ",power)
        print("Number of bits needed by opcode :                                  ",b_opcode)
        print("Number of filler bits in Instruction type 2 :                      ",b_filler)
        print("Maximum numbers of instructions this ISA can support :             ",max_inst)
        print("Maximum number of registers this ISA can support :                 ",max_reg)

    elif(memory_type=="Byte"):
        a=int(memory_size[0])
        b=memory_size[1]
        c=memory_size[2]
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/8)
        
        powera=(math.ceil(Log2(int(a))))

        power=power+powera
        b_opcode=int(L_inst-(L_reg+power))
        b_filler=L_inst-((2*L_reg)+b_opcode)
        max_inst=2**b_opcode
        max_reg=(2**L_reg)
        print("Minimum bits needed to represent an address in this architecture : ",power)
        print("Number of bits needed by opcode :                                  ",b_opcode)
        print("Number of filler bits in Instruction type 2 :                      ",b_filler)
        print("Maximum numbers of instructions this ISA can support :             ",max_inst)
        print("Maximum number of registers this ISA can support :                 ",max_reg)

    elif(memory_type=="Word"):
        size=int(input("Word Size : "))
        a=memory_size[0]
        b=memory_size[1]
        c=memory_type[2]
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/size)
        
        powera=(math.ceil(Log2(int(a))))

        power=power+powera
        b_opcode=int(L_inst-(L_reg+power))
        b_filler=L_inst-((2*L_reg)+b_opcode)
        max_inst=2**b_opcode
        max_reg=(2**L_reg)

        print("Minimum bits needed to represent an address in this architecture : ",power)
        print("Number of bits needed by opcode :                                  ",b_opcode)
        print("Number of filler bits in Instruction type 2 :                      ",b_filler)
        print("Maximum numbers of instructions this ISA can support :             ",max_inst)
        print("Maximum number of registers this ISA can support :                 ",max_reg)

    else:
        print("ERROR : Kindly enter a valid type")


elif (q_type==2):
    def bit(a,b,c):
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
       
        powera=(math.ceil(Log2(int(a))))

        power=power+powera
        return power

    def nibble(a,b,c):
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/4)
       
        powera=(math.ceil(Log2(int(a))))
        power=power+powera
        return power
    
    def byte(a,b,c):
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/8)
        powera=(math.ceil(Log2(int(a))))
        power=power+powera
        return power
    def word(a,b,c,s):
        power=0
        if(b=="K"):
            power=10
        elif(b=="M"):
            power=20
        elif(b=="G"):
            power=40  
        if(c=="B"):
            a=a*8
        a=int(a/s)
        
        powera=(math.ceil(Log2(int(a))))
        power=power+powera
        return power


    print("SELECT ONE")
    print("TYPE A")
    print("TYPE B")
    stype=input("Enter the type : ")
    if (stype=="A"):
        memory_size=input("Enter the space in memory : ").split()
        memory_type=str(input("Enter the memory addressing type : "))
        L_cpu=int(input("How many bits the cpu is : "))
        L_mode=input("How you would want to change the current addressable memory : ")
        x=int(memory_size[0])
        y=memory_size[1]
        z=memory_size[2]
        if(memory_type=="Bit"):
            out1=bit(x,y,z)
        elif(memory_type=="Nibble"):
            out1=nibble(x,y,z)
        elif(memory_type=="Byte"):
            out1=byte(x,y,z)
        elif(memory_type=="Word"):
            out1=word(x,y,z,L_cpu)
            
        if(L_mode=="Bit"):
            out2=bit(x,y,z)
        elif(L_mode=="Nibble"):
            out2=nibble(x,y,z)
        elif(L_mode=="Byte"):
            out2=byte(x,y,z)
        elif(L_mode=="Word"):
            out2=word(x,y,z,L_cpu)
        print(out2-out1)

    elif (stype=="B"):
        L_cpu=int(input("How many bits the cpu is : "))
        L_pin=int(input("No of address pins : "))
        L_mode=input("Type of addressable memory : ")
        if(L_mode=="Bit"):
            ans=(2**L_pin)
            ans=ans/8
            ans=(math.ceil(Log2(int(ans))))
            ans=ans-30
            ans=2**ans
            print(ans,"GB")
        elif(L_mode=="Nibble"):
            ans=(2**L_pin)*4
            ans=ans/8
            ans=(math.ceil(Log2(int(ans))))
            ans=ans-30
            ans=2**ans
            print(ans,"GB")
        elif(L_mode=="Byte"):
            ans=(2**L_pin)*8
            ans=ans/8
            ans=(math.ceil(Log2(int(ans))))
            ans=ans-30
            ans=2**ans
            print(ans,"GB")

        elif(L_mode=="Word"):
            ans=(2**L_pin)*L_cpu
            ans=ans/8
            ans=(math.ceil(Log2(int(ans))))
            ans=ans-30
            ans=2**ans
            print(ans,"GB")
