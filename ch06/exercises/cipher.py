
# list=[1,2,3,4,5]
# print(list[1:])
# print(list[:2])

def cipher():
    text=input("phrase: ")
    alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    size=len(text)
    shift=3
    new_word=""
    for i in range(size):
        new_letter=alpha_list[alpha_list.index(text[i].upper())+shift %26]
        

        new_word+=new_letter
    
    return new_word
    
        
    
        
#%26=

print(cipher())