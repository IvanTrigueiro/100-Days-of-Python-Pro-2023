#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

with open("./Input/Letters/starting_letter.txt") as starting_lines:
    starting_letter = starting_lines.read()

with open("./Input/Names/invited_names.txt") as names:
    names_list = names.readlines()

for name_index in range(0, len(names_list)):
    names_list[name_index] = names_list[name_index].replace("\n", "").strip()
    name = names_list[name_index]
    ready_letter = starting_letter.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode="w") as letter_to_write:
        letter_to_write.write(ready_letter)


    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp