import spacy

# Load the language model
nlp = spacy.load("en_core_web_md")

#---------------------------Single Words-----------------------
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

#---------------------------Word Vectors-----------------------
# I included also the dog, meat and fish words.
tokens = nlp('cat apple monkey banana fish meat dog')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

tokens_new = nlp("tree bird sky leaf flower sun")

for token1 in tokens_new:
    for token2 in tokens_new:
        print(token1.text, token2.text, token1.similarity(token2))

#-----------------------Working with Sentences-------------------
sentence_to_compare = "Why is my cat on the car"

sentences = ["Where did my dog go",
             "Hello there is my car",
             "I\'ve lost my car in my car",
             "I\'d like my boat back",
             "I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

#-----------------------------Notes------------------------------

# ---------------------------Note 1------------------------------
# Word vectors results
"""
cat apple 0.20368057489395142
cat monkey 0.5929929614067078
cat banana 0.2235882580280304
cat fish 0.3198717534542084
cat meat 0.2846548855304718
cat dog 0.8220816850662231
monkey cat 0.5929929614067078
monkey apple 0.2342509627342224
monkey banana 0.4041501581668854
monkey fish 0.31199339032173157
monkey meat 0.24929700791835785
monkey dog 0.4771559536457062
dog cat 0.8220816850662231
dog apple 0.22881001234054565
dog monkey 0.4771559536457062
dog banana 0.2090904861688614
dog fish 0.3187839686870575
dog meat 0.3119393289089203
meat banana 0.46547049283981323
meat fish 0.6178809404373169
"""
# - The dog-cat pair has the stronger similarity (0.82) followed by the 
#   cat-monkey (0.59) and the dog-monkey (0.47). So spacy does a pretty good job
# - If we would ask spacy to predict what food dog, cat and monkey likes then
#   dog would prefer fish (0.318), cat would prefer fish (0.319) and monkey 
#   would prefer banana (0.40). So I would argue that spacy fail to predict 
#   corectly what the dog would like to eat, since meat is the preferable choice.
# - Meat has stronger similarity to fish than banana, since banana is a fruit. 
"""
music dance 0.6672372221946716
music art 0.5534184575080872
music theater 0.5026883482933044
music poetry 0.5588147640228271
music book 0.30195698142051697
music film 0.45269593596458435
dance music 0.6672372221946716
dance art 0.4565719962120056
dance theater 0.5208985805511475
dance poetry 0.39445000886917114
dance book 0.14082582294940948
dance film 0.28824734687805176
art music 0.5534184575080872
art dance 0.4565719962120056
art theater 0.44748732447624207
art poetry 0.5480574369430542
art book 0.3366203010082245
art film 0.3151766359806061
theater music 0.5026883482933044
theater dance 0.5208985805511475
theater art 0.44748732447624207
theater poetry 0.29311808943748474
theater book 0.17347002029418945
theater film 0.4769991338253021
poetry music 0.5588147640228271
poetry dance 0.39445000886917114
poetry art 0.5480574369430542
poetry theater 0.29311808943748474
poetry book 0.5824213027954102
poetry film 0.3808210492134094
book music 0.30195698142051697
book dance 0.14082582294940948
book art 0.3366203010082245
book theater 0.17347002029418945
book poetry 0.5824213027954102
book film 0.42285090684890747
film music 0.45269593596458435
film dance 0.28824734687805176
film art 0.3151766359806061
film theater 0.4769991338253021
film poetry 0.3808210492134094
film book 0.4228509068489
"""
# - The highest similarity is between music nad dance and this is true since 
#   both of them are strongly correlated.
# - Art has stronger similarity to music and poetry than the other forms of art, 
#   theater, film, and dance. Interestingly film has the lowest similarity with art.
# - Poetry has significant similarities with book (0.58), music (0.55) and 
#   art (0.54) which is a valid point.
# - No sigifcant similarities between book-theater and book-dance. I would expect
#   book-poetry to have stronger similarity like book and film (0.42). 

# ---------------------------Note 2------------------------------
# First of all when running the example.py with the en_core_web_sm language model 
# the following warning shows up that has to do with the available word vectors 
# of the model. 
"""
UserWarning: [W007] The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, 
parser and NER, which may not give useful similarity judgements. 
This may happen if you're using one of the small models, 
e.g. `en_core_web_sm`, which don't ship with word vectors and 
only use context-sensitive tensors. You can always add your own word vectors, 
or use one of the larger models instead if available.
"""

# I have run the example.py with both en_core_web_md and en_core_web_sm 
# language models and stored the similarity indexes in teh file similarity.txt
# Let's see visualise the similarity indexes of the two models

import matplotlib.pyplot as plt

# Read the file similarity.txt. The file contains the similarity indexes of 
# both the en_core_web_sm and the en_core_web_md models. The first line is
# the indexes of the en_core_web_sm model and the second line the indexes 
# of the en_core_web_md model.
with open("similarity.txt", "r") as file:
    file_content  = file.read()

# Get the two similarity indexes
sm_similarity_str, md_similarity_str = file_content.strip().split('\n')

# Convert the string to a list 
sm_similaritiy_numbers = list(map(float, sm_similarity_str.split(",")))
#print(len(sm_similaritiy_numbers))

# Convert the string to a list
md_similarity_numbers = list(map(float, md_similarity_str.split(",")))
#print(len(md_similarity_numbers))

md_sm_diff = [((x - y)/x)*100 for x, y in zip(md_similarity_numbers, sm_similaritiy_numbers)]

# Create a list of indices for x-axis
x = list(range(len(md_similarity_numbers)))

# Plotting the lists
plt.plot(x, md_similarity_numbers, label='MD Model Similarity')
plt.plot(x, sm_similaritiy_numbers, label='SM Model Similarity')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('MD Model vs SM Model')

# Adding a legend
plt.legend()

# Displaying the plot
plt.show()

# Examnining the similarities we observe that the SM model evaluates the sentences 
# with lower similarity indexes which is in concert with the warning about the 
# available word vectors.