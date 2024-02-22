# import nltk
# from nltk.corpus import brown
# from gensim.models import Word2Vec

# nltk.download('brown')

# # .sents() creates the corpus as a list of sentences
# data = brown.sents()

# w2v_model = Word2Vec(min_count=5,
#                      window=5,
#                      sg=0,
#                      sample=6e-5,
#                      negative=20)

# w2v_model.build_vocab(data)
# w2v_model.train(data, total_examples=w2v_model.corpus_count, epochs=15)

# # Access the trained embeddings
# word_embeddings = w2v_model.wv

# # Use most_similar through the wv attribute
# similar_words = word_embeddings.most_similar('university', topn=5)

# Print the results
# print("Similar words to 'university':")
# for word, score in similar_words:
    # print(f"{word}: {score}")


# similarity_score = word_embeddings.similarity('jazz', 'music')
# print(similarity_score)
# d_match = w2v_model.doesnt_match(['pine', 'fir', 'coconut'])
# print(d_match)

# import gensim.downloader as api

# glove_model = api.load('glove-twitter-25')

# most_similar = glove_model.most_similar(positive=['woman', 'king'], negative=['man'], topn=3)
# print(most_similar)

# import fasttext
# model = fasttext.train_unsupervised("brown_text.txt", epoch=3, minn=2, maxn=4, dim=128)

# import numpy as np
# from nltk.tokenize import word_tokenize
# from nltk import FreqDist


# def one_hot_encoding(sentence):
#     tokens = word_tokenize(sentence)

#     freq_dist = FreqDist(tokens)

#     unique_words = list(freq_dist.keys())

#     one_hot_matrix = np.eye(len(unique_words))

#     word_index = {word: i for i, word in enumerate(unique_words)}

#     sentence_matrix = np.zeros((len(tokens), len(unique_words)))

#     for i, token in enumerate(tokens):
#         sentence_matrix[i, word_index[token]] = 1

#     return sentence_matrix


# path = 'data/dataset/input.txt'

# with open(path, 'r') as file:
#     sentence = file.read()

# output_matrix = one_hot_encoding(sentence)

print(output_matrix)

from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

dataset = ["So no one told you life was gonna be this way",
           "Your job's a joke, you're broke",
           "Your love life's DOA",
           "It's like you're always stuck in second gear",
           "When it hasn't been your day, your week, your month",
           "Or even your year, but",
           "I'll be there for you"]


vectorizer = TfidfVectorizer(input='content', use_idf=True, lowercase=True,
                             analyzer='word', ngram_range=(1, 1), stop_words=None, vocabulary=None, min_df=0.01, max_df=0.60)

tfidf_matrix = vectorizer.fit_transform(dataset)

print(f"Matrix dimension: {tfidf_matrix.shape}")
# print(tfidf_matrix)
print(tfidf_matrix[6])
