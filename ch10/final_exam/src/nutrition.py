import requests
import json
import pprint




class Category_API:

    def __init__(self):
        """
        Initialize the url
        
        
        """
        self.url = f'https://www.themealdb.com/api/json/v1/1/search.php?f=a'

    def get(self):
        """
        Get it into json dictionary
        
        return: (String) get the desired values
        
        """
        info = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = json.loads(info.text)
        pprint.pprint(response)
        meals=response['meals']
        for d in meals:
     
    
            strMeal=d['strMeal']
            print(strMeal)
       
        #check to make sure I got meals values
        if response.get('meals'):
            return strMeal
        else:
            return None


