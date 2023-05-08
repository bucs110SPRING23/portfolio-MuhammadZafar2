
import requests
import json
import pprint


class MealAPI:

    def __init__(self):
        self.url = f'https://www.themealdb.com/api/json/v1/1/categories.php'
        """
        Initialize the url
        
        
        """
    def get(self):
        """
        Get it into json dictionary
        
        return: (String) get the desired values
        
        """
        info = requests.get(self.url)
        #response is just a json dictonary of values after .json() call
        response = json.loads(info.text)
        pprint.pprint(response)
        category=response['categories']
        for d in category:
     
    
            strCategory=d['strCategory']
            print(strCategory)
        
        #check to make sure I got the categories
        if response.get(strCategory):
            return strCategory
        else:
            return None


















