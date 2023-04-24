class StringUtility:
    def __init__(self, string):
        self.string=string


    def __str__(self):
        
        return self.string
    

    def vowels(self):
        """
        Count the number of vowels in the string and return the result as a string
        
        """
        size=len(self.string)
        count=0
        for i in range(0,size):
            if self.string[i] in ["a","e","i","o","u"]:
                count+=1
            
        if count>=5:
            return "many"
        else:
            return str(count)
        
    def bothEnds(self):
        """
        return a string made of the first 2 and last 2 characters of the original string,
        However, if the string length is less than or equal to 2, return an empty string instead.
        
        """
        size=len(self.string)
        if size<=2:
            return ""
        new_word = self.string[:2]+self.string[-2:]
        
        return new_word
        
    def fixStart(self):
        """
        return a string where all occurrences of the first character have been changed to '*'
        """
        size=len(self.string)
        if size<=1:
            return self.string
        first_letter=self.string[0]
        
        
        new_word=self.string[1:].replace(first_letter,"*")
        new_word=first_letter+new_word
        return new_word
        
    def asciiSum(self):
        """
        return an int that contains the sum of all ascii values in the string.
        """
        acii_value=0
        for i in self.string:
            acii_value+=ord(i)

        return acii_value
    
    def cipher(self):
        """
        return an encoded string by incrementing all letters by the length of the string.
        """
        
        alpha_list=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 
                    'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        size=len(self.string)
        shift=11
        new_word=""
        for i in range(size):
            idx = (alpha_list.index(self.string[i].upper())+shift) %26

            
            new_letter=alpha_list[idx]
            

            new_word+=new_letter
        
        return new_word.lower()
            