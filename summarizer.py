import spacy
spacy.load('en_core_web_sm')
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from collections import Counter
from heapq import nlargest

class Summarizer:

    def __init__(self):
        self.summary = None

    def spacy_summarize(self, text):
        self.summary = ""
        
        nlp = spacy.load('en_core_web_sm')
        doc = nlp(text)

        keyword = []
        stopwords = list(STOP_WORDS)
        pos_tag = ["PROPN", "ADJ", "NOUN", "VERB"]
        for token in doc:
            if token.text in stopwords or token.text in punctuation:
                continue
            if token.pos_ in pos_tag:
                keyword.append(token.text)

        word_count = Counter(keyword)

        max_count = Counter(keyword).most_common(1)[0][1]
        for word in word_count.keys():
            word_count[word] = (word_count[word] / max_count)
        
        sent_score = {}
        for sent in doc.sents:
            for word in sent:
                if word.text in word_count.keys():
                    if sent in sent_score.keys():
                        sent_score[sent] += word_count[word.text]
                    else:
                        sent_score[sent] = word_count[word.text]

        summarized_sents = nlargest(3, sent_score, key=sent_score.get)
        final_sents = [w.text for w in summarized_sents]
        
        self.summary = " ".join(final_sents)
        return self.summary