from flask import Flask, request
import json

app = Flask(__name__)

file = open('data.json')
data = json.load(file)

def save_data():
    with open('data.json', 'w') as f:
        json.dump(data, f)

# 1. Display movies
@app.route('/movies', methods=['GET'])
def get_movies():
    return data[0]

# 2. Display tv shows
@app.route('/tv_shows', methods=['GET'])
def get_tv_shows():
    return data[1]

# 3. Display celebrities
@app.route('/celebrities', methods=['GET'])
def get_celebrities():
    return data[2]

# 4. Add a movie
@app.route('/add_movie', methods=['POST'])
def add_movie():
    new_movie = request.json
    data[0].append(new_movie)
    save_data()
    return "Movie added successfully!"

# 5. Add a TV show
@app.route('/add_tv_show', methods=['POST'])
def add_tv_show():
    new_show = request.json
    data[1].append(new_show)
    save_data()
    return "TV Show added successfully!"

# 6. Add a celebrity
@app.route('/add_celebrity', methods=['POST'])
def add_celebrity():
    new_celeb = request.json
    data[2].append(new_celeb)
    save_data()
    return "Celebrity added successfully!"

# 7. Search for a movie by title
@app.route('/search_movie/<title>', methods=['GET'])
def search_movie(title):
    for movie in data[0]:
        if movie['title'] == title:
            return {"Movie details": movie}
    return "Movie not found"

# 8. Search for a TV show by title
@app.route('/search_tv_show/<title>', methods=['GET'])
def search_tv_show(title):
    for show in data[1]:
        if show['title'] == title:
            return {"TV Show details": show}
    return "TV Show not found"

# 9. Search for a celebrity by name
@app.route('/search_celebrity/<name>', methods=['GET'])
def search_celebrity(name):
    for celeb in data[2]:
        if celeb['name'] == name:
            return {"Celebrity details": celeb}
    return "Celebrity not found"

# 10. Update a movie details
@app.route('/update_movie/<title>', methods=['PUT'])
def update_movie(title):
    update_data = request.json
    for movie in data[0]:
        if movie['title'] == title:
            movie.update(update_data)
            save_data()
            return "Movie updated successfully!"
    return "Movie not found"

# 11. Update a TV show details
@app.route('/update_tv_show/<title>', methods=['PUT'])
def update_tv_show(title):
    update_data = request.json
    for show in data[1]:
        if show['title'] == title:
            show.update(update_data)
            save_data()
            return "TV Show updated successfully!"
    return "TV Show not found"

# 12. Update a celebrity details
@app.route('/update_celebrity/<name>', methods=['PUT'])
def update_celebrity(name):
    update_data = request.json
    for celeb in data[2]:
        if celeb['name'] == name:
            celeb.update(update_data)
            save_data()
            return "Celebrity updated successfully!"
    return "Celebrity not found"

# 13. Delete a movie
@app.route('/delete_movie/<title>', methods=['DELETE'])
def delete_movie(title):
    for movie in data[0]:
        if movie['title'] == title:
            data[0].remove(movie)
            save_data()
            return "Movie deleted successfully!"
    return "Movie not found"

# 14. Delete a TV show
@app.route('/delete_tv_show/<title>', methods=['DELETE'])
def delete_tv_show(title):
    for show in data[1]:
        if show['title'] == title:
            data[1].remove(show)
            save_data()
            return "TV Show deleted successfully!"
    return "TV Show not found"

# 15. Delete a celebrity
@app.route('/delete_celebrity/<name>', methods=['DELETE'])
def delete_celebrity(name):
    for celeb in data[2]:
        if celeb['name'] == name:
            data[2].remove(celeb)
            save_data()
            return "Celebrity deleted successfully!"
    return "Celebrity not found"

# 16. Add a review to a movie
@app.route('/add_movie_review/<title>', methods=['POST'])
def add_movie_review(title):
    review = request.json
    for movie in data[0]:
        if movie['title'] == title:
            if 'reviews' not in movie:
                movie['reviews'] = []
            movie['reviews'].append(review)
            save_data()
            return "Review added successfully!"
    return "Movie not found"

# 17. Add a review to a TV show
@app.route('/add_tv_show_review/<title>', methods=['POST'])
def add_tv_show_review(title):
    review = request.json
    for show in data[1]:
        if show['title'] == title:
            if 'reviews' not in show:
                show['reviews'] = []
            show['reviews'].append(review)
            save_data()
            return "Review added successfully!"
    return "TV Show not found"

# 18. List all reviews for a movie
@app.route('/view_movie_reviews/<title>', methods=['GET'])
def view_movie_reviews(title):
    for movie in data[0]:
        if movie['title'] == title:
            return {"Reviews": movie.get('reviews', [])}
    return "Movie not found"

# 19. List all reviews for a TV show
@app.route('/view_tv_show_reviews/<title>', methods=['GET'])
def view_tv_show_reviews(title):
    for show in data[1]:
        if show['title'] == title:
            return {"Reviews": show.get('reviews', [])}
    return "TV Show not found"

# 20. Display movies from a particular streaming platform
@app.route('/movies_on_platform/<platform>', methods=['GET'])
def movies_on_platform(platform):
    available_movies = []
    for movie in data[0]['movies']:  
        if platform in movie.get('streaming_platforms', []):
            available_movies.append(movie)
    return {"Movies on " + platform: available_movies}

# 21. Display Tv shows from a particular streaming platform
@app.route('/tv_shows_on_platform/<platform>', methods=['GET'])
def tv_shows_on_platform(platform):
    available_shows = []
    for show in data[1]['tv_shows']:  
        if platform in show.get('streaming_platforms', []):
            available_shows.append(show)
    return {"TV Shows on " + platform: available_shows}

# 22. Display all movies of a specific celebrity
@app.route('/movies_of_celebrity/<name>', methods=['GET'])
def movies_of_celebrity(name):
    movies = []
    for celeb in data[2]['celebrities']: 
        if celeb['name'].lower() == name.lower():
            for movie_id in celeb.get('movies', []):
                for movie in data[0]['movies']:
                    if movie['id'] == movie_id:
                        movies.append(movie)
    if movies:
        return {"Movies": movies}
    return "Celebrity not found"

# 23. Display all TV shows of a specific celebrity
@app.route('/tv_shows_of_celebrity/<name>', methods=['GET'])
def tv_shows_of_celebrity(name):
    tv_shows = []
    for celeb in data[2]['celebrities']:
        if celeb['name'].lower() == name.lower():
            for show_id in celeb.get('tv_shows', []):
                for show in data[1]['tv_shows']:
                    if show['id'] == show_id:
                        tv_shows.append(show)
    if tv_shows:
        return {"TV Shows": tv_shows}
    return "Celebrity not found"

# 24. Get movies by genre
@app.route('/movies_by_genre/<genre>', methods=['GET'])
def movies_by_genre(genre):
    filtered_movies = []
    for movie in data[0]['movies']:
        if genre.lower() in movie.get('genre', '').lower():
            filtered_movies.append(movie)
    return {"Movies in genre " + genre: filtered_movies}

# 25. Get TV shows by genre
@app.route('/tv_shows_by_genre/<genre>', methods=['GET'])
def tv_shows_by_genre(genre):
    filtered_shows = []
    for show in data[1]['tv_shows']:  
        if genre.lower() in show.get('genre', '').lower():
            filtered_shows.append(show)
    return {"TV Shows in genre " + genre: filtered_shows}

# 26. Get movie details by movie ID
@app.route('/movie_details/<movie_id>', methods=['GET'])
def movie_details(movie_id):
    for movie in data[0]['movies']: 
        if str(movie['id']) == movie_id:
            return movie
    return "Movie not found"

# 27. Get TV show details by show ID
@app.route('/tv_show_details/<show_id>', methods=['GET'])
def tv_show_details(show_id):
    for show in data[1]['tv_shows']:  
        if str(show['id']) == show_id:
            return show
    return "TV Show not found"


if __name__ == "__main__":
    app.run(debug = True)
