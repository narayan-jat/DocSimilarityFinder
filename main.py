"""
This script implements functions for computing the similarity between two documents
based on cosine similarity and ranks the top similar pairs of documents. It can be
used to find and rank document pairs that are most similar to each other in a given dataset.

Author: Narayan Jat
Date: 22 April 2024
"""

# Importing required modules.
import math
import heapq
import time
import os
from tokenizer import tokenize

# Path of folder where all the documents are stored. Change this variable if document directory is changed.
FOLDER_PATH = 'YOUR FOLDER DIRECTORY HERE'


def create_doc_ids_dic():
    """
    Creates a dictionary mapping document numbers to document IDs based on the contents of a folder.

    Returns:
        dict: A dictionary where keys are document IDs and values are document numbers.
    """
    folder_contents = os.listdir(FOLDER_PATH)        # Name of document which are basically doc numbers.
    return {i+1: n for i, n in enumerate(folder_contents)}     # Creating doc number doc id dictionary.


def doc_tokens_dic():
    """
    Tokenizes the content of each document in the folder and stores the tokens in a dictionary.

    Returns:
        dict: A dictionary where keys are document numbers and values are dictionary of tokens for particular document.
    """
    d = create_doc_ids_dic()
    for i in d:
        with open(f'{FOLDER_PATH}/{d[i]}', 'r') as file:
            content = file.read()
            document_tokens[i] = tokenize(content)      # Tokenizing content of each document.


def compute_idf():
    """
    Computes the inverse document frequency (IDF) of a token in a collection of documents.
    """
    for i_d in document_tokens:
        for t in document_tokens[i_d]:
            df = 0                       # Document frequency
            n = 0                        # Total documents counter.
            if t not in tokens_idf:
                for d in document_tokens:
                    tokens = document_tokens[d]
                    if t in tokens:
                        df += 1
                    n += 1
                tokens_idf[t] = math.log(n / df)


def create_normalised_doc_vec(d):
    """
    Creates a normalized vector representation for a document with the given document ID.

    Returns:
        dict: A normalized vector representation for the document, where tokens are keys and weights are values.
    """
    tokens = document_tokens[d]
    tt = tokens.pop("TOTAL_TOKENS")
    w_square_sum = 0        # Sum of squares of individual weights.
    for token in tokens:
        tf = (tokens[token] / tt)
        weight = tf * tokens_idf[token]
        tokens[token] = weight
        w_square_sum += weight ** 2
    norm = math.sqrt(w_square_sum)      # Computing norm of vector by taking square root.
    # Dividing every weight by norm.
    for token in tokens:
        tokens[token] = tokens[token] / norm
    return tokens


def dot_product(v1, v2):
    """
    Computes the dot product of two vectors.

    Args:
        v1 (dict): The first vector.
        v2 (dict): The second vector.

    Returns:
        float: The dot product of the two vectors.
    """
    product = 0
    for token in v1:
        if token in v2:
            product += v1[token] * v2[token]
    return product


def compute_pairwise_similarity():
    """
    Computes the pairwise similarity between documents using a max heap.

    Returns:
        list: A list representing a max heap of similarity values along with the corresponding document IDs.
              Each element in the list is a tuple containing (-similarity_value, doc_id_1, doc_id_2).
    """

    pq = []     # Initializing heap
    dic = create_doc_ids_dic()
    document_vectors = {doc_id: create_normalised_doc_vec(doc_id) for doc_id in range(1, 133)}
    for d in range(1, 132):
        doc1_vect = document_vectors[d]
        for j in range(d+1, 133):
            doc2_vect = document_vectors[j]
            similarity_value = dot_product(doc1_vect, doc2_vect)
            # Multiplying similarity value of negative to maintain a max heap.
            heapq.heappush(pq, (-similarity_value, dic[d], dic[j]))
    return pq


def rank_top_similar_doc():
    """
    Ranks the top fifty similar documents based on pairwise similarity values.

    Prints the document IDs and similarity scores of the top fifty similar documents.
    """
    rank_list = compute_pairwise_similarity()
    print("Here are the top FIFTY similar documents for given dataset: \n ")
    for _ in range(50):
        item = heapq.heappop(rank_list)
        print(f"Document ID1: {item[1]}, Document ID2: {item[2]}, Similarity score: {round(-item[0] * 100, 2)} %")


# Main
if __name__ == '__main__':
    tokens_idf = {}         # Token as key and there idf value as the value.
    document_tokens = {}    # Document id as key and tokens as value
    try:
        doc_tokens_dic()        # Creating dictionary for tokens of individual documents.
        compute_idf()
        rank_top_similar_doc()
    except FileNotFoundError:
        print("\n \t \t  \t !! Knock Knock !! \n Please Check the directory you have entered for the documents dataset \n \t \t     For help Please Refer Readme.md")
