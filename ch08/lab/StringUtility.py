class StringUtility:
    def __init__(self, string):
        self.string=string


    def __str__(self):
        return self.string
    

    def vowels(self):
        size=len(self.string)
        count=0
        for i in range(0,size):
            if self.string[i] is "a","e","i","o","u":
                count+=1
            
        if count>=5:
            return "many"
        else:
            return count
        
    def bothEnds(self):
        size=len(self.string)
        new_word=self.string[0]+self.string[1]+self.string[size-1]+ self.string[size]
        if size<=2:
            return ""
        else:
            return new_word
        
    def fixStart(self):
        first_letter=self.string[0]
        size=len(self.string)
        for i in range(1,size):
            if first_letter == self.string[i]:
                new_word=self.string[i].replace("*")
        if size<=1:
            return self.string
        else:
            return new_word
        
         
            