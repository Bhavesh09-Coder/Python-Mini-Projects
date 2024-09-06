# Project Title : Movie Recommendation System

import pandas as pd

# Sample dataset: 50 movies with genres and average ratings
data = {
    'Movie': [
        'The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'The Lord of the Rings: The Return of the King',
        'Forrest Gump', 'Inception', 'Fight Club', 'The Matrix', 'The Empire Strikes Back',
        'The Godfather Part II', 'The Silence of the Lambs', 'Se7en', 'The Usual Suspects', 'Schindler\'s List',
        'The Departed', 'Gladiator', 'Braveheart', 'The Green Mile', 'The Prestige',
        'Memento', 'Interstellar', 'Goodfellas', 'The Lion King', 'The Intouchables',
        'Parasite', 'Joker', 'Once Upon a Time in Hollywood', 'The Grand Budapest Hotel', 'The Revenant',
        'The Shining', 'A Beautiful Mind', 'WALL·E', 'The Social Network', '12 Angry Men',
        'Whiplash', 'The Dark Knight Rises', 'The Wolf of Wall Street', 'Django Unchained', 'The Big Lebowski',
        'Inglourious Basterds', 'The Terminator', 'The Truman Show', 'The Witch', 'Her',
        'La La Land', 'Spotlight', 'Moonlight', 'The Shape of Water', 'Get Out'
    ],
    'Genre': [
        'Drama', 'Crime', 'Action', 'Crime', 'Adventure',
        'Drama', 'Sci-Fi', 'Drama', 'Sci-Fi', 'Action',
        'Crime', 'Thriller', 'Crime', 'Crime', 'Drama',
        'Crime', 'Action', 'Biography', 'Drama', 'Drama',
        'Mystery', 'Sci-Fi', 'Crime', 'Animation', 'Comedy',
        'Thriller', 'Drama', 'Adventure', 'Comedy', 'Drama',
        'Horror', 'Biography', 'Animation', 'Drama', 'Drama',
        'Drama', 'Action', 'Drama', 'Western', 'Comedy',
        'Drama', 'Action', 'Comedy', 'Drama', 'Comedy',
        'Fantasy', 'Romance', 'Drama', 'Thriller', 'Drama'
    ],
    'Rating': [
        9.3, 9.2, 9.0, 8.9, 8.9,
        8.8, 8.8, 8.8, 8.7, 8.7,
        8.7, 8.6, 8.6, 8.5, 8.5,
        8.5, 8.5, 8.4, 8.4, 8.4,
        8.4, 8.3, 8.3, 8.3, 8.2,
        8.2, 8.2, 8.1, 8.1, 8.1,
        8.1, 8.0, 8.0, 8.0, 8.0,
        8.0, 8.0, 7.9, 7.9, 7.9,
        7.9, 7.9, 7.8, 7.8, 7.8
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print("Movie Dataset:")
print(df)

# Function to recommend movies based on genre and rating
def recommend_movies(genre, min_rating=8.0):
    recommendations = df[(df['Genre'] == genre) & (df['Rating'] >= min_rating)]
    return recommendations

# Example Usage
user_genre = 'Drama'
print(f"\nRecommended {user_genre} Movies with rating >= 8.0:")
print(recommend_movies(user_genre))
