import os, re, mmap
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
    results = {}
    count = 0
    #list all files directory
    for filename in os.listdir(curr_dir):
        #check to make sure it is a file
        fname = os.path.join(curr_dir, filename)         
        if os.path.isfile(fname):
            #open file, check for matches
            with open(fname) as f:
                ans = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
                #increment count if match found
                if ans.find(exp) != -1:
                    count +=1
    results[curr_dir] = count
    return results[curr_dir]

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
plt.ylim(0, max(output.values())+3)

plt.title("Distribution of keywords")
plt.xlabel("Subdirectory Names")
plt.ylabel("Count values")
plt.show()