
list=[1,2,3,4,5]
print(list[1:])
print(list[:2])

def cipher(text):
    alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letter_dict={}
    shift=3
    for i in range(26):
        new_letter=alpha_list[i+shift]
        letter_dict.append(new_letter)
    
        
#%26=

cipher(hyyhyhyh)