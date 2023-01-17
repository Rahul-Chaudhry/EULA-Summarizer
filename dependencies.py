import numpy as np
import pandas as pd
import nltk
import re
import wget
from zipfile import ZipFile 
from nltk.corpus import stopwords
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import sent_tokenize
import networkx as node
nltk.download('punkt')