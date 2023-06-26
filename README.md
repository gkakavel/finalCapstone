# finalCapstone

## Description

## Table of contents
* [Installation](#installation)
* [Usage](#usage)
* [Features](#features)
* [Contributing](#contributing)
* [Licence](#licence)
* [Contact](#contact)

## Installation

1. Make sure you have Python installed on your system. You can download Python from the official website: [Python.org](https://www.python.org/downloads/).

2. Install the required library, `spacy`, by running the following command in your command prompt or terminal:

   ```
   pip install spacy
   ```

3. Download the English language model for spaCy by executing the following command:

   ```
   python -m spacy download en_core_web_md
   ```

4. Once the installation is complete, you can now proceed to run the script.

## Usage

1. Ensure that you have the following files in the same directory:

   - `movies.txt` (the file containing movie titles and descriptions)
   - The script file with the provided code (e.g., `watch_next.py`)

2. Open the script file (`watch_next.py`) in a text editor.

3. In the script, you can customize the target movie by modifying the following variables:

   ```python
   TARGET_MOVIE_TITLE = "Planet Hulk"
   TARGET_MOVIE_DESCRIPTION = "Will he save their world or destroy it? " \
               "When the Hulk becomes too dangerous for the Earth, " \
               "the Illuminati trick Hulk into a shuttle and launch him " \
               "into spaces to a planet where the Hulk can live in peace. " \
               "Unfortunately, Hulk lands on the planet Sakkar where he is sold " \
               "into slavery and trained as a gladiator."
   ```

   Update `TARGET_MOVIE_TITLE` and `TARGET_MOVIE_DESCRIPTION` with the desired values.

4. Save the changes made to the script file.

5. Open a command prompt or terminal and navigate to the directory where the script file is located.

6. Run the script by executing the following command:

   ```
   python watch_next.py
   ```

   The script will read the movie descriptions from the `movies.txt` file, compare them to the target movie description, and recommend the most similar movie title to watch next based on the similarity indexes.

7. The recommended movie title will be displayed in the console output.

## Features

- Reads a file (`movies.txt`) containing movie titles and descriptions.
- Recommends a movie title to watch next based on the similarity between the target movie description and the provided movie descriptions.
- Uses the `spacy` library for natural language processing (NLP) and similarity calculation.
- Allows customization of the target movie by modifying the `TARGET_MOVIE_TITLE` and `TARGET_MOVIE_DESCRIPTION` variables in the script.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please create an issue or submit a pull request.

## Licence
This project is licensed under the MIT Licence. See the LICENSE file for more details.

## Contact
If you have any questions or want to reach out, feel free to contact Georgios Kakavelakis at gekakavelakis@gmail.com.
