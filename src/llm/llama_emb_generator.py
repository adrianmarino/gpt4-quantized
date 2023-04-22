from llama_cpp import Llama
from langchain.embeddings import LlamaCppEmbeddings
import numpy as np


class LlamaEmbeddingGenerator:
    def __init__(self, model_path):
       self.model = LlamaCppEmbeddings(model_path=model_path)
    
    def embed(self, prompt):
        return np.array(self.model.embed_query(prompt))