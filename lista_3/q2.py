import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

def preprocessing(filepath):
    # Carrega o conjunto de dados
    df = pd.read_csv(filepath, sep='\t', header=None, names=['label', 'sms'])
    
    # Converte as etiquetas para formato binário: "ham"= 0 e "spam"= 1
    df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    
    # Divide o conjunto de dados em treino (70%) e teste (30%)
    X_train, X_test, y_train, y_test = train_test_split(df['sms'], df['label'], test_size=0.3, random_state=42)
    
    # Utiliza o modelo de bag-of-words para transformar o texto das mensagens em representação numérica
    vectorizer = CountVectorizer()
    X_train_bow = vectorizer.fit_transform(X_train)
    X_test_bow = vectorizer.transform(X_test)
    
    return X_train_bow, X_test_bow, y_train, y_test

class NaiveBayesClassifier:
    def __init__(self):
        self.word_probs_ham = {}
        self.word_probs_spam = {}
        self.p_ham = 0
        self.p_spam = 0
        self.vocab_size = 0
    
    def train(self, X_train, y_train):
        # Conta a quantidade total de mensagens ham e spam
        num_ham = np.sum(y_train == 0)
        num_spam = np.sum(y_train == 1)

        # Calcula a probabilidade das classes
        self.p_ham = num_ham / len(y_train)
        self.p_spam = num_spam / len(y_train)
        
        # Total de palavras em cada classe
        ham_word_counts = np.zeros(X_train.shape[1])
        spam_word_counts = np.zeros(X_train.shape[1])
        
        # Soma as ocorrências de palavras em cada classe
        for i in range(X_train.shape[0]):
            if y_train.iloc[i] == 0:
                ham_word_counts += X_train[i].toarray().flatten()
            else:
                spam_word_counts += X_train[i].toarray().flatten()
        
        # Suavização de Laplace para cada palavra
        self.vocab_size = X_train.shape[1]
        self.word_probs_ham = (ham_word_counts + 1) / (ham_word_counts.sum() + self.vocab_size)
        self.word_probs_spam = (spam_word_counts + 1) / (spam_word_counts.sum() + self.vocab_size)

    def predict(self, sms_vector):
        # Calcula a probabilidade logarítmica de cada classe
        p_ham_given_sms = np.log(self.p_ham)
        p_spam_given_sms = np.log(self.p_spam)
        
        # Converte a mensagem em uma matriz densa para multiplicação
        sms_vector = sms_vector.toarray().flatten()
        
        # Calcula as probabilidades logarítmicas de cada classe
        p_ham_given_sms += np.sum(np.log(self.word_probs_ham) * sms_vector)
        p_spam_given_sms += np.sum(np.log(self.word_probs_spam) * sms_vector)
        
        # Retorna a classe com a maior probabilidade
        return 0 if p_ham_given_sms > p_spam_given_sms else 1

    def predict_batch(self, X):
        return [self.predict(X[i]) for i in range(X.shape[0])]
    

def calculate_metrics(classifier, X_test, y_test):
    # Obter as previsões do conjunto de teste
    predictions = classifier.predict_batch(X_test)
    
    # Inicializar contadores
    true_positive = false_positive = true_negative = false_negative = 0
    
    for pred, true in zip(predictions, y_test):
        if pred == 1 and true == 1:
            true_positive += 1
        elif pred == 1 and true == 0:
            false_positive += 1
        elif pred == 0 and true == 0:
            true_negative += 1
        elif pred == 0 and true == 1:
            false_negative += 1
    
    # Calcular métricas
    accuracy = (true_positive + true_negative) / len(y_test)
    precision = true_positive / (true_positive + false_positive) if (true_positive + false_positive) > 0 else 0
    recall = true_positive / (true_positive + false_negative) if (true_positive + false_negative) > 0 else 0
    f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
    
    # Retornar as métricas como um dicionário
    return {
        'accuracy': accuracy,
        'precision': precision,
        'recall': recall,
        'f1_score': f1_score
    }



if __name__ == '__main__':
    X_train, X_test, y_train, y_test = preprocessing('lista_3/SMSSpamCollection')

    # Treina o classificador Naive Bayes
    classifier = NaiveBayesClassifier()
    classifier.train(X_train, y_train)

    # Calcula as métricas do classificador
    metrics = calculate_metrics(classifier, X_test, y_test)
    print(metrics)