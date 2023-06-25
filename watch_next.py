""""
This program illustrates the use of NLP similarity to recommend a movie.
It reads a file with movie descriptions and based on a target movie description,
it recommends a title of a movie to watch next by evaluating the similarity indexes
between the target movie description and the provided movie descriptions.
"""

# Importing spacy
import spacy  

# Define the target movie title and description
TARGET_MOVIE_TITLE = "Planet Hulk"
TARGET_MOVIE_DESCRIPTION = "Will he save their world or destroy it? " \
                "When the Hulk becomes too dangerous for the Earth, " \
                "the Illuminati trick Hulk into a shuttle and launch him " \
                "into spaces to a planet where the Hulk can live in peace. " \
                "Unfortunately, Hulk lands on the planet Sakkar where he is sold " \
                "into slavery and trained as a gladiator."

def read_file(filename: str):
    """It aksk the user to provide a file and reads the contents.
    
    Args:
        filename (string): the filename with the strings
    Returns: 
        lines (list): a list containing the lines of the file.

    Raises: 
        FileNotFoundError

    Notes:
    """

    # Define an empty list to store the file data
    lines = []

    while True:

        # Ask the user to provide the filename if filename is not provided
        if not filename:
            filename = input("Please provide the file path and name of your data file: ")
        
        # Define a try-except block to Read the file, store it in "lines" and return it
        try:
            # Open tthe file with a contect manager
            with open(filename, 'r') as file:
                lines = file.readlines()
                return lines
            
        # If file does not exist display an error message
        except FileNotFoundError:
            print("I am sorry but no such file or directory exist. Please try again.")


def movie_to_recommend(target_description, movies):
    """It recommends to a user which movie title would watch if they have watched 
        the given movie description.
    
    Args:
        target_description (spacy.tokens.Doc): the description of the target movie
        movies (dict): a dictionary of (key: str, value: nlp object) pairs

    Returns: 
        title (string): the title of the most similar movie to the target movie.

    Raises: 
        ValueError: If no movies are provided

    Notes:
    """

    if not movies:
        raise ValueError("Error: No movies found.")

    # Define a list that will hold tuples of (movie title, similararity index)
    movie_similarities = []

    # Iterate over the movies items
    for movie_title, movie_description in movies.items():

        # Get the similarity index comparing the target decription NLP object
        # with each movie description NLP object
        similarity = target_description.similarity(movie_description)
        
        # Display the similarity index for each movie 
        #print(movie_title + " - ", similarity)
        
        # Append each (title, similarity) tuple to the movie_similarities list
        movie_similarities.append((movie_title,similarity))

    # Get the tuple with the maximum similarity index.
    # We use the max() function and we apply the similarity index
    # using a lambda function
    max_tuple = max(movie_similarities, key=lambda x: x[1])
    
    # Display the tuple with the maximum similarity index
    #print(max_tuple)

    return max_tuple[0]


def main():

    # Define the NLP model we want to use. 
    nlp = spacy.load('en_core_web_md') 

    # Define a dictionary where we will store the movies from the file
    movie_dict = {}

    # Read the file and store the content in list 'movie_list'
    movie_list = read_file('movies.txt')

    # Iterate over the movie_list
    for movie in movie_list:

        # Split the movie to get the title and description
        title, description = movie.split(":")
            
        # Store the movie in the dictionary using title as key and 
        # description as value
        movie_dict[title] = nlp(description.strip())

    # Get the next movie to watch
    next_movie = movie_to_recommend(nlp(TARGET_MOVIE_DESCRIPTION), movie_dict)

    # Display the recommended movie to watch next 
    print(f"Based on the movie {TARGET_MOVIE_TITLE} the reccomendation is "
           f"to watch next {next_movie}")

if __name__ == "__main__":
    main()