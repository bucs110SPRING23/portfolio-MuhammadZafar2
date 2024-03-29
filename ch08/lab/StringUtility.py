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
        Encrypts or decrypts a message using the Caesar cipher technique.

        args:
            text:str = the message to encrypt or decrypt
            shift:int = the number of positions to shift each letter
        return:
            :str = the encrypted or decrypted message
        """

        result = ""
        size=len(self.string)
        for char in self.string:
            if char.isalpha():
                # Determine the case of the character
                start = ord('A') if char.isupper() else ord('a')
                # Calculate the new position of the character after the shift
                new_pos = (ord(char) - start + size) % 26
                # Convert the new position back to a character
                char = chr(start + new_pos)
            result += char
        return result




















































