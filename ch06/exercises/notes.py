#files
import json  #string format, not file format
# def main():
#     file_pointer=open("assets/ideas.txt","r") #write "w"
#     file_pointer.write("Hello World")
#     file_pointer.write("/n")
#     file_pointer.close()
#     ideas=file_pointer.read()
#     # idea=input("Enter an idea: ")
#     # ideas=[]
#     # ideas.append(idea)
#     ideas=file_pointer.readline()
#     print(ideas)
#     print(ideas[1])
#     file_pointer.write(i+'/n')

# main()

def main():
    filename="assets/ideas.txt"
    fptr=open(filename,"r")
    accumalator=0
    for ch in fptr.read():
        if in ch.isalum():
            accumalator+=1
    fptr.close()

    fptr=open(filename+".dat","w")
    fptr.write(accumalator)
    fptr.write(data)
    fptr.close()

main()

json_string=json.dumps(data)
print(json_string,type (json__string))
json_data=json.loads(json_string)

for k,v in json_data.items():
    print(k,v)

fptr=open("assets/ideas.json","w") .read()
data=json.loads.type(fptr)
print(data,type(data))




def main():
    idea=input("enter an idea: ")
    idea=