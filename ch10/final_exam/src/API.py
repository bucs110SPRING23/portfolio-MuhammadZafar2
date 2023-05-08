import random
from src.meal import MealAPI
from src.nutrition import Category_API



def main():
    
    """
    This function would combine the two APIs into a string
    
    return: (String) The combined statement
    
    """
    
    
    #Proxy Class
    mapi =MealAPI()
    napi=Category_API()
    results_Meal = mapi.get()
   
    results_Nutrition=napi.get()
    
    for o in results_Nutrition:
        #combine the incorrect and corrects into a single array
        if results_Nutrition!='Ayam Percik':
            answer= results_Meal['Dessert']
            answers = 'This food is called ' + results_Nutrition + ", and one of the types could be  "+ answer
        else:
            answer=results_Meal['Chicken']
            answers = 'This food is called ' + results_Nutrition + ", and one of the types could be  "+ answer
            
            #shuffle the array for random order
            random.shuffle(answers)
            
            print(answers)
            
        
        
        
main()

