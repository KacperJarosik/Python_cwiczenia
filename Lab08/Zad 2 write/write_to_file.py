zoo = ["lion", "elephant", "monkey"]

if __name__ == "__main__":
    f = open("output.txt", 'w')  #'add modifier a'

    for i in zoo:
        f.write(i+'\n')          #add the whole zoo to the output.txt
    #f.write(zoo)
    f.close()                    #close the file