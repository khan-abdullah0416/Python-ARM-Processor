class Processor:


    def run_program(self, instructions, initial_registers):
        
        if len(instructions) > 256:
            return -2
        
        register_dict = {
            "A": initial_registers[0],
            "B": initial_registers[1],
            "C": initial_registers[2],
            "D": initial_registers[3],
        }
        
        
        def swap(register1, register2):
            register_dict[register1], register_dict[register2] = register_dict[register2], register_dict[register1]
            
            
        def compare(register1, register2):
            if register_dict[register1] > register_dict[register1]:
                register_dict["D"] = register_dict[register1] - register_dict[register2]
            else:
                register_dict["D"] = 0
                
        
        def add(register1, register2):
            register_dict["D"] = register_dict[register1] + register_dict[register2]
            
            
        def subtract(register1, register2):
            register_dict["D"] = register_dict[register1] - register_dict[register2]
            
            
        def jump_pos(register1):
            if register_dict["D"] == 0:
                for i in range(register1 - 1, len(instructions)):
                    inst_whole = instructions[register1 - 1]
                    inst = inst_whole[:3]
                    
                    if inst == "SWP":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            swap(register1, register2)
                            
                    elif inst == "CMP":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            compare(register1, register2)
                            
                    elif inst == "ADD":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            add(register1, register2)
                        
                    elif inst == "SUB":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            subtract(register1, register2)
                            
                    elif inst == "JMP":
                        register1 = int(inst_whole[4])
                        
                        if register1 == "":
                            return -2
                        else:
                            jump_pos(register1)
                            
                    elif inst == "JNZ":
                        register1 = int(inst_whole[4])
                        
                        if register1 == "":
                            return -2
                        else:
                            jump_neg(register1)
          
        
        def jump_neg(register1):
            if register_dict["D"] != 0:
                for i in range(register1 - 1, len(instructions)):
                    inst_whole =  instructions[i]
                    inst = inst_whole[:3]
                    
                    if inst == "SWP":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            swap(register1, register2)
                            
                    elif inst == "CMP":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            compare(register1, register2)
                        
                    elif inst == "ADD":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            add(register1, register2)
                
                    elif inst == "SUB":
                        register1 = inst_whole[4:5]
                        register2 = inst_whole[6:]
                        
                        if register2 == "":
                            return -2
                        elif register1 == "":
                            return -2
                        else:
                            subtract(register1, register2)
                        
                    elif inst == "JMP":
                        register1 = int(inst_whole[4])
                        
                        if register1 == "":
                            return -2
                        else:
                            jump_pos(register1)
                            
                    elif inst == "JNZ":
                        register1 = int(inst_whole[4])
                        
                        if register1 == "":
                            return -2
                        else:
                            jump_neg(register1)
                        


        if True:
            for i in range(len(instructions)):
                
                inst_whole = instructions[i] 
                inst = inst_whole[:3]
                
                if inst == "SWP":
                    register1 = inst_whole[4:5]
                    register2 = inst_whole[6:]
                    
                    if register2 == "":
                        return -2
                    elif register1 == "":
                        return -2
                    else:
                        swap(register1, register2)
                        
                elif inst == "CMP":
                    register1 = inst_whole[4:5]
                    register2 = inst_whole[6:]
                    
                    if register2 == "":
                        return -2
                    elif register1 == "":
                        return -2
                    else:
                        compare(register1, register2)
                        
                elif inst == "ADD":
                    register1 = inst_whole[4:5]
                    register2 = inst_whole[6:]
                    
                    if register2 == "":
                        return -2
                    elif register1 == "":
                        return -2
                    else:
                        add(register1, register2)
                        
                elif inst == "SUB":
                    register1 = inst_whole[4:5]
                    register2 = inst_whole[6:]
                    
                    if register2 == "":
                        return -2
                    elif register1 == "":
                        return -2
                    else:
                        subtract(register1, register2)
                        
                elif inst == "JMP":
                    register1 = int(inst_whole[4])
                    
                    if register1 == "":
                        return -2
                    else:
                        jump_pos(register1)
                        
                elif inst == "JNZ":
                    register1 = int(inst_whole[4])
                    
                    if register1 == "":
                        return -2
                    else:
                        jump_neg(register1)
        
        
        return register_dict["D"]
