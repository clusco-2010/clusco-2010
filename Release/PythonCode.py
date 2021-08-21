import re
import string
import collections





def Histogram():
    
        # Open both the read and the write files
    with open('frequency.dat', "w") as wp:    
        # Same code as in "ItemCounter" to store the values as a dictionary
        with open('CS210_P3.txt') as fp:
            counts = collections.Counter(line.strip() for line in fp)
        # Write the item and counts to the output file
        for key in counts:
            wp.write('%s %d\n' % (key, counts[key]))
    # If the file was properly closed, tell the user
    if wp.closed:
        print('Success')
        

def printsomething():
    

    # Open file use collections module to store the values as a dictionary
    with open('CS210_P3.txt') as fp:
        counts = collections.Counter(line.strip() for line in fp)
    # For every key (item name), print the item and the amount sold
    for key in counts:
        print('%s %d' % (key, counts[key]))
        
def veggielist():
    print("Vegtables to choose from:\n")

    # Open file use collections module to store the values as a dictionary
    with open('CS210_P3.txt') as fp:
        counts = collections.Counter(line.strip() for line in fp)
    # For every key (item name), print the item and the amount sold
    
    for key in sorted(counts):
        print(key)

def PrintMe(v):
    
    
            # Open file use collections module to store the values as a dictionary
        with open('CS210_P3.txt') as fp:
            counts = collections.Counter(line.strip() for line in fp)
        # For every key (item name), print the item and the amount sold
        for key in counts:
            counts[key]= counts.get(key,0)   #calculating frequency
        if v in counts:  #if given item is present in the string
            print("There were ", counts[v]," ", v , " sold today","\n") 
        return 0
       



