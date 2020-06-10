import spacy


if __name__ == "__main__" :
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("i am a cat")

    for word in doc:
        print(word)