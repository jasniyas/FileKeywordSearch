import os, re
import matplotlib.pyplot as plt
import numpy as npy

#user prompt input
root_dir = raw_input("Enter root directory:")
keyword = raw_input("Enter keyword to search:")

#initialize key:value array (directory)
output = {}
#search through all files in given directory
def SearchFile(curr_dir, exp):
    #initialize count
    count = 0
    #list all files directory
    for filename in os.listdir(curr_dir):
        #check to make sure it is a file
        fname = os.path.join(curr_dir, filename)         
        if os.path.isfile(fname):
            #open file, check for matches
            with open(fname) as f:
                for line in f:
                    searchobj = re.search(exp, line, re.M|re.I)
                    if searchobj:
                        count +=1
    return count

#recursively walk through all dirs & call FileSearch for each subdir
for root, dirs, files in os.walk(root_dir):
    output[os.path.basename(root)] = SearchFile(root, keyword)
    #output[root] = SearchFile(root, keyword)
    
#output array of all the data
print output

#output bar graph using matplotlib
graph= npy.arange(len(output))
plt.bar(graph, output.values())
plt.xticks(graph, output.keys())
plt.ylim(0, max(output.values())+2)

plt.title("Distribution of keywords")
plt.xlabel("Subdirectory Names")
plt.ylabel("Count values")
plt.show()