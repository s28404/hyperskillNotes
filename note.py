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

import fasttext
model = fasttext.train_unsupervised("brown_text.txt", epoch=3, minn=2, maxn=4, dim=128)