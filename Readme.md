# Automated Document Similarity Analysis using TF-IDF and Cosine Similarity

This project is designed to compute and rank document similarity based on cosine similarity, a popular technique in Natural Language Processing (NLP). Given a folder of text documents, this script tokenizes and vectorizes each document, calculates TF-IDF weights for each word, and ranks document pairs based on cosine similarity. This approach is useful in fields like plagiarism detection, document clustering, and recommendation systems.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Setup and Installation](#setup-and-installation)
4. [Usage](#usage)
5. [Example Output](#example-output)
6. [Technical Details](#technical-details)
7. [Troubleshooting](#troubleshooting)

---

### Project Overview
The script accepts a directory of text documents, tokenizes each document, computes TF-IDF values, and normalizes document vectors. By calculating pairwise cosine similarity, it identifies the most similar document pairs and outputs the top-ranking pairs with their similarity scores.

### Features
- **Custom Tokenization**: Parses and tokenizes documents without using third-party libraries.
- **TF-IDF Calculation**: Computes term frequencies and inverse document frequencies for accurate weighting.
- **Cosine Similarity Ranking**: Uses cosine similarity to assess and rank document similarity.
- **Max-Heap Storage**: Ranks and retrieves the top 50 similar document pairs using a max-heap.

### Setup and Installation
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-repo/document-similarity-ranking.git
   cd document-similarity-ranking
   ```
   
2. **Set Document Directory**  
   In the script, set the `FOLDER_PATH` variable to the directory containing your text documents.

3. **Run the Script**
   Execute the script with:
   ```bash
   python document_similarity.py
   ```

### Usage
1. Place all text documents in a single directory. Each document should be a text file.
2. Set the path of the directory in the `FOLDER_PATH` variable within the script.
3. Run the script to output the top 50 similar document pairs with similarity scores.

### Example Output
```
Here are the top FIFTY similar documents for given dataset: 

Document ID1: doc1.txt, Document ID2: doc2.txt, Similarity Score: 85.23%
Document ID1: doc3.txt, Document ID2: doc4.txt, Similarity Score: 83.76%
...
```

### Technical Details
- **TF-IDF Calculation**: The script calculates term frequency (TF) and inverse document frequency (IDF) values for each word in a document. The resulting document vectors are normalized for cosine similarity.
- **Cosine Similarity**: Using the dot product of two normalized vectors, cosine similarity is computed to determine document closeness.
- **Max-Heap Ranking**: The script maintains a max-heap to efficiently store and retrieve the top 50 most similar document pairs.

### Troubleshooting
- **File Not Found Error**: If you encounter a "File Not Found" error, ensure that the `FOLDER_PATH` is set to the correct directory containing your text documents.
- **Document Count Limitations**: This script is optimized for datasets with a manageable number of documents. For larger datasets, memory optimization or batching may be necessary.

