# Gets all functions and memory addresses and prints them to console and file in the same directory as exe.
#@author 0x MATIJA BENSA
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 
#@runtime Jython


import os


print("Hello, world!")

# setupe folder and file name
program = getCurrentProgram()
program_location = program.getExecutablePath() 
program_directory = os.path.dirname(program_location)
program_name = program.getName() 
file_name = program_name + "_function_list.txt" 
file_name_full = os.path.join(program_directory, file_name)
# get functions
funcManager = currentProgram.getFunctionManager()
funcs = funcManager.getFunctions(True)
with open(file_name_full, "w") as file:
    for func in funcs: 
        output = "Function: 0x{} :: {:<40} ==> {:<40} \n".format(func.getEntryPoint(), func.getName(), func.getSignature())
        print(output)
        file.write(output) 
print("File written: ",file_name_full)

