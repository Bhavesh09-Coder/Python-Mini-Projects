## Food-recommendation system:

"""
recipes.csv:
recipe_id,recipe_name,ingredients,dietary_restrictions
1,Spaghetti Bolognese,spaghetti,tomato,beef,onion,garlic,gluten
2,Vegetable Stir Fry,rice,carrot,broccoli,soy sauce,garlic,vegetarian,vegan
3,Chicken Salad,chicken,lettuce,tomato,cucumber,dairy-free
4,Beef Tacos,beef,tortilla,cheese,tomato,lettuce,gluten
5,Tofu Curry,tofu,coconut milk,curry paste,spinach,vegetarian,vegan
"""

"""
user_preferences.csv:
user_id,preferred_ingredients,disliked_ingredients,dietary_restrictions
1,tomato,garlic,gluten
2,broccoli,onion,vegetarian
3,lettuce,beef,dairy-free
"""

## Recommendation System Code
import pandas as pd

class FoodRecommendationSystem:
    def __init__(self, recipes_file, user_prefs_file):
        self.recipes = pd.read_csv(recipes_file)
        self.user_prefs = pd.read_csv(user_prefs_file)
    
    def get_recommendations(self, user_id):
        user_pref = self.user_prefs[self.user_prefs['user_id'] == user_id]
        if user_pref.empty:
            print(f"No preferences found for user ID: {user_id}")
            return []
        
        preferred_ingredients = user_pref['preferred_ingredients'].values[0].split(',')
        disliked_ingredients = user_pref['disliked_ingredients'].values[0].split(',')
        dietary_restrictions = user_pref['dietary_restrictions'].values[0].split(',')
        
        def filter_recipes(row):
            ingredients = row['ingredients'].split(',')
            restrictions = row['dietary_restrictions'].split(',')
            
            # Check if any disliked ingredients are in the recipe
            if any(ingredient in ingredients for ingredient in disliked_ingredients):
                return False
            
            # Check dietary restrictions
            if not all(restriction in restrictions for restriction in dietary_restrictions):
                return False
            
            # Check if any preferred ingredients are in the recipe
            if any(ingredient in ingredients for ingredient in preferred_ingredients):
                return True
            
            return False
        
        recommended_recipes = self.recipes[self.recipes.apply(filter_recipes, axis=1)]
        
        return recommended_recipes
    
    def display_recommendations(self, user_id):
        recommendations = self.get_recommendations(user_id)
        if recommendations.empty:
            print("No recommendations available.")
        else:
            print(f"Recommendations for User {user_id}:")
            for idx, row in recommendations.iterrows():
                print(f"- {row['recipe_name']}")

if __name__ == "__main__":
    recommender = FoodRecommendationSystem('recipes.csv', 'user_preferences.csv')
    user_id = int(input("Enter User ID: "))
    recommender.display_recommendations(user_id)
