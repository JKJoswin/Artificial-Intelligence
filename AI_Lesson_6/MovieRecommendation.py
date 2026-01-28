import pandas as pd
from textblob import TextBlob

df = pd.read_csv('IMDB_Dataset.csv')

df["combined features"] = df["Genre"].fillna("") + " " + df["Overview"].fillna("")

def get_genres(df):
    genres = []
    for g in df["Genre"].dropna():
        for item in g.split(","):
            genres.append(item.strip())
    return sorted(set(genres))

genres = get_genres(df)

def recommend_movies(genre,mood,min_rating=7.5,top_n=5):
    movies = df.copy()
    movies = movies[movies["Genre"].str.contains(genre, case=False, na=False)]
    movies = movies[movies["IMDB_Rating"] >= min_rating]
    recommendations = []
    user_sentiment = TextBlob(mood).sentiment.polarity

    for _, row in movies.iterrows():
        if pd.isna(row["Overview"]):
            continue
    
        movie_sentiment = TextBlob(row["Overview"]).sentiment.polarity

        if user_sentiment < 0 and movie_sentiment > 0:
            recommendations.append(
                (row["Series_Title"], row["Genre"], movie_sentiment)
            )
        elif user_sentiment >= 0:
            recommendations.append(
                (row["Series_Title"], row["Genre"], movie_sentiment)
            )
    
        if len(recommendations) == top_n:
            break

    return recommendations

#--- MAIN PROGRAM ---
print("🎬 Welcome to Movie Recommender")
print("\nAvailable Genres:")
for i, g in enumerate(genres, 1):
    print(i, g)

choice = int(input("\nChoose genre number: "))
genre = genres[choice - 1]
mood = input("How do you feel today? ")
rating = float(input("Minimum IMDb rating: "))
movies = recommend_movies(genre, mood, rating)
print("\n🍿 Recommended Movies:\n")

for i, (title, genre, polarity) in enumerate(movies, 1):
    mood_type = "Positive 😊" if polarity > 0 else "Negative 😞" if polarity < 0 else "Neutral 😐"
    print(f"{i}. {title}")
    print(f" Genre : {genre}")
    print(f" Polarity : {polarity:.2f} ({mood_type})\n")