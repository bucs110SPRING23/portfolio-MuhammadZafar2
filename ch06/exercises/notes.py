#files
import json  #string format, not file format
def main():
    file_pointer=open("assets/ideas.txt","r") #write "w"
    ideas=file_pointer.read()
    # idea=input("Enter an idea: ")
    # ideas=[]
    # ideas.append(idea)
    ideas=file_pointer.readline()
    print(ideas)
    print(ideas[1])
    file_pointer.write(i+'/n')

main()
