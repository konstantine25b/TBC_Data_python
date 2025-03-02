from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_unixtime, year, avg, count, explode, split, desc

# Initialize Spark session
spark = SparkSession.builder.appName("MovieLensAnalysis").getOrCreate()

# Load datasets
movies = spark.read.csv("movies.csv", header=True, inferSchema=True)
ratings = spark.read.csv("ratings.csv", header=True, inferSchema=True)

# Convert timestamp to year
ratings = ratings.withColumn("year", year(from_unixtime(col("timestamp"))))

# Task 1: Movie Popularity by Year
popularity_by_year = (
    ratings.groupBy("year", "movieId")
    .count()
    .withColumnRenamed("count", "rating_count")
    .orderBy("year", desc("rating_count"))
)

most_rated_movies = (
    popularity_by_year.withColumnRenamed("rating_count", "max_count")
    .groupBy("year")
    .agg({"max_count": "max"})
    .withColumnRenamed("max(max_count)", "max_count")
    .join(popularity_by_year, ["year", "max_count"])
    .select("year", "movieId", "max_count")
)

# Task 2: Top Genres by Average Rating
movies_genres = movies.withColumn("genre", explode(split(col("genres"), "\\|")))
ratings_with_movies = ratings.join(movies_genres, "movieId")

avg_rating_by_genre = (
    ratings_with_movies.groupBy("genre")
    .agg(avg("rating").alias("average_rating"))
    .orderBy(desc("average_rating"))
    .limit(5)
)

# Task 3: Top-Rated Movies by Genre
movies_with_avg_ratings = (
    ratings.groupBy("movieId")
    .agg(avg("rating").alias("average_rating"), count("rating").alias("rating_count"))
    .filter(col("rating_count") >= 10)
)

movies_genres_with_ratings = movies_genres.join(movies_with_avg_ratings, "movieId")

top_rated_movies_by_genre = (
    movies_genres_with_ratings
    .groupBy("genre", "movieId", "title")
    .agg(avg("average_rating").alias("average_rating"))
    .orderBy("genre", desc("average_rating"))
    .limit(5)
)

# Show Results
print("Most Rated Movies by Year:")
most_rated_movies.show(truncate=False)

print("Top Genres by Average Rating:")
avg_rating_by_genre.show(truncate=False)

print("Top-Rated Movies by Genre:")
top_rated_movies_by_genre.show(truncate=False)

# Stop the Spark session
spark.stop()