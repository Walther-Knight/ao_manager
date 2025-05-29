
def convert_encountered(input):
#quick convert for source file
    #input = "Unarmed,M,1/4/4,5d4,2,1d4MK,0|Bite,M,1/2/6,5d4,2,1d4+1MK,0"
    array = input.split("|")
    output = []
    workingFile = []
    for each in array:
        workingFile = each.split(",")
        del workingFile[3]
        workingFile[0] = "Name: " + workingFile[0]
        workingFile[1] = "Type: " + workingFile[1]
        workingFile[2] = "R/M/E: " + workingFile[2]
        workingFile[3] = "SPL: " + workingFile[3]
        workingFile[4] = "Damage: " + workingFile[4]
        workingFile[5] = "Mod: " + workingFile[5]
        if len(workingFile) == 7: 
            workingFile[6] = "Notes: " + workingFile[6]
        else: 
            workingFile.append("Notes: ")
        output.append(",".join(workingFile))
    print(output)