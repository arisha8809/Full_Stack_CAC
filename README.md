```markdown
# Movie, TV Show, and Celebrity Management API

This API allows you to manage movies, TV shows, and celebrities. You can add, update, delete, and search for them. You can also manage reviews for movies and TV shows.

## Endpoints

### View Data

- **Movies, TV Shows, Celebrities**  
  **Endpoint:** `/movies`, `/tv_shows`, `/celebrities`  
  **Method:** `GET`  
  **Description:** Get a list of all movies, TV shows, or celebrities.

### Add Data

- **Add Movie, TV Show, Celebrity**  
  **Endpoint:** `/add_movie`, `/add_tv_show`, `/add_celebrity`  
  **Method:** `POST`  
  **Description:** Add a new movie, TV show, or celebrity.

### Search Data

- **Search Movie, TV Show, Celebrity**  
  **Endpoint:** `/search_movie/<title>`, `/search_tv_show/<title>`, `/search_celebrity/<name>`  
  **Method:** `GET`  
  **Description:** Search for a movie, TV show, or celebrity by name.

### Update Data

- **Update Movie, TV Show, Celebrity**  
  **Endpoint:** `/update_movie/<title>`, `/update_tv_show/<title>`, `/update_celebrity/<name>`  
  **Method:** `PUT`  
  **Description:** Update a movie, TV show, or celebrity.

### Delete Data

- **Delete Movie, TV Show, Celebrity**  
  **Endpoint:** `/delete_movie/<title>`, `/delete_tv_show/<title>`, `/delete_celebrity/<name>`  
  **Method:** `DELETE`  
  **Description:** Delete a movie, TV show, or celebrity.

### Reviews

- **Add Review to Movie/TV Show**  
  **Endpoint:** `/add_movie_review/<title>`, `/add_tv_show_review/<title>`  
  **Method:** `POST`  
  **Description:** Add a review for a movie or TV show.

- **View Reviews for Movie/TV Show**  
  **Endpoint:** `/view_movie_reviews/<title>`, `/view_tv_show_reviews/<title>`  
  **Method:** `GET`  
  **Description:** Get all reviews for a movie or TV show.

### Data by Platform or Genre

- **Movies/TV Shows on a Platform**  
  **Endpoint:** `/movies_on_platform/<platform>`, `/tv_shows_on_platform/<platform>`  
  **Method:** `GET`  
  **Description:** Get all movies or TV shows available on a specific platform.

- **Movies/TV Shows by Genre**  
  **Endpoint:** `/movies_by_genre/<genre>`, `/tv_shows_by_genre/<genre>`  
  **Method:** `GET`  
  **Description:** Get movies or TV shows by genre.

### Data by Celebrity

- **Movies/TV Shows of a Celebrity**  
  **Endpoint:** `/movies_of_celebrity/<name>`, `/tv_shows_of_celebrity/<name>`  
  **Method:** `GET`  
  **Description:** Get all movies or TV shows featuring a specific celebrity.

## File Structure

- `entertainment.py` - Flask application file.
- `data.json` - JSON file with movie, TV show, and celebrity data.
```

