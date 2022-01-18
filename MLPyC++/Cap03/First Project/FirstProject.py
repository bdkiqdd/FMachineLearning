# Project 1 - Text classification with Supervised Learn

# Packages
from numpy.typing import _256Bit
import praw
import re
import config
import numpy as np
from sklearn import decomposition
from sklearn.metrics.pairwise import pairwise_distances_argmin_min
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import seaborn as sns

## Data load

# Subjects that we want to search
subs = ['datascience', 'machinelearning', 'physics', 'astrology', 'conspiracy']

# Def modules

def data_load():

    # Auth to reddit api, has all information on Praw Doc
    reddit = praw.Reddit(
                        client_id="cAUPn5eQK_S9sFv_YAj45g",
                        client_secret="xyEuWls60iyFPd-bL5bxEirEcRh5zQ",
                        user_agent="Kiqviana",
                        username="Kiqviana",
                        password="ECKiq3,8reddit")

    # Count char with RegEx
    char_count = lambda post: len(re.sub('\W|\d','',post.selftext))

    # Filter to posts with more than 100 char
    mask = lambda post: char_count(post) >=100

    # Lists to results
    data = []
    labels = []

    # Loop
    for i,sub in enumerate(subs):

        # Posts Extraction
        subreddit_data = reddit.subreddit(sub).new(limit=1000)

        # Posts filter
        posts = [post.selftext for post in filter(mask,subreddit_data)]

        # Posts consolidation 
        data.extend(posts)
        labels.extend([i] * len(posts))

        # Output
        print(f"Número de posts do assunto r/{sub}: {len(posts)}",
            f"\nUm dos posts extraídos: {posts[0][:600]}...\n",
            "_" * 80 + '\n')

    return data,labels

## End Data Load section

## Data Train and Test

# Const var to control
TEST_SIZE = .2
RANDOM_STATE = 0

# Def to split data
def split_data():
    
    print(f"Split {100 * TEST_SIZE}% dos dados serão utilizados para treinamento...")

    # Split of data
    X_train,X_test,Y_train,Y_test = train_test_split(data
                                                    ,labels
                                                    ,test_size=TEST_SIZE
                                                    ,random_state=RANDOM_STATE)
    # X = Var Input
    # Y = Var Output
      
    print(f"{len(Y_test)} amostras de teste.")

    return X_train,X_test,Y_train,Y_test

## End Data Train and Test section

## Data Pre-processing and attributes Extraction

# Const var to control
MIN_DOC_FREQ=1
N_COMPONENTS=1000
N_ITER = 30

# Pre-processing pipeline def 

def pprocessing_pipeline():
    
    # Remove Non alphabets chars
    pattern = r'\W|\d|http.*\s+|www.*\s+'
    preprocessor = lambda text: re.sub(pattern,' ',text)

    # TF-IDF vectorization
    vectorizer = TfidfVectorizer(preprocessor=preprocessor,stop_words='english',min_df=MIN_DOC_FREQ)

    # TF-IDF matrix dimensional redux
    decomposition = TruncatedSVD(n_components= N_COMPONENTS,n_iter=N_ITER)

    # Pipeline
    pipeline = [('tfidf',vectorizer),('svd',decomposition)]

    return pipeline

## End Data Pre-processing and attributes Extraction

## Model selection

# Const var to control

N_NEIGHBORS = 4
CV = 3

# Def to create some different models

def create_models():
    
    model1 = KNeighborsClassifier(n_neighbors= N_NEIGHBORS)
    model2 = RandomForestClassifier(random_state= RANDOM_STATE)
    model3 = LogisticRegressionCV(cv= CV, random_state= RANDOM_STATE)

    models = [("KNN",model1),("RandomForest",model2),("LogReg",model3)]

    return models

## End model selection

## Train and classification

# Def to train and classifier

def train_classifier(models,pipeline,X_train,X_test,Y_train,Y_test):

    results = []

    # Loop
    for name,model in models:

        # Pipeline
        pipe = Pipeline(pipeline + [(name,model)])

        # Train
        print(f"Treinando o modelo {name} com as informações passadas")
        pipe.fit(X_train,Y_train)

        # Prevision with data test results
        Y_pred = pipe.predict(X_test)


        # Metrics calc
        report = classification_report(Y_test, Y_pred)
        print("Relatório de Classificação\n",report)

        results.append([model,{'model': name,'prevision':Y_pred,'report':report,}])

    return results

## End train and classification

## Pipeline exec

if __name__ == '__main__':

    # Data Load
    data,labels = data_load()

    # Division on test and train
    X_train,X_test,Y_train,Y_test = split_data()

    # Pre-processeing pipeline
    pipeline = pprocessing_pipeline()

    # Generate models
    all_models = create_models()

    # Train and classifier models
    results = train_classifier(all_models,pipeline,X_train,X_test,Y_train,Y_test)

print("All safe!")

## Result Viz

def plot_distribution():
    _,counts = np.unique(labels, return_counts= True)
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(15,6),dpi=120)
    plt.title("Number posts by subject")
    sns.barplot(x=subs, y=counts)
    plt.legend(''.join([f.title(),f"- {c} posts"]) for f,c in zip(subs,counts))
    plt.show()

def plot_confusion(result):
    print("Relatório de Classificação\n", result[-1]['report'])
    Y_pred = result[-1]['prevision']
    conf_matrix = confusion_matrix(Y_test,Y_pred)
    _,test_counts = np.unique(Y_test,return_counts= True)
    conf_matrix_percent = conf_matrix/test_counts.transpose()*100
    plt.figure(figsize=(9,8),dpi=120)
    plt.title(result[-1]['model'].upper() + "Resultados")
    plt.xlabel("Valor Real")
    plt.ylabel("Previsão do Modelo")
    ticklabels = [f"r/{sub}" for sub in subs]
    sns.heatmap(data=conf_matrix_percent,xticklabels= ticklabels,yticklabels=ticklabels,annot = True, fmt = '.2f')
    plt.show()

# Classification graph
plot_distribution()

# KNN results
plot_confusion(results[0])

# RandomForest results
plot_confusion(results[1])

# LogReg results
plot_confusion[results[2]]