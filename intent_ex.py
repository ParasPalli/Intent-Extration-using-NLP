import re
import joblib
import nltk
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sen = SentimentIntensityAnalyzer()
np_clf = joblib.load(r"./model/n_p_classifier.joblib")


def intents(rv):

    intent = []
    pos_tagged = nltk.pos_tag(nltk.word_tokenize(rv))

    for word, pos in pos_tagged:

        if pos.startswith("N"):
            intent.append(word)

    return intent


# Review
# review_list = []
# review_list.append("""Paras Is a good boy....""")

def Start_Extraction(review, file):

    if review != "":

        neg_intents = []
        pos_intents = []

        review_split = re.split("; | , | but | also | and | &", re.sub("[.]+", " & ", review))

        for rv in review_split:

            if len(rv) is not 0 and not rv.isspace():

                prediction = np_clf.predict([rv.strip()])
                sem_prediction = sen.polarity_scores(rv.strip())

                if sem_prediction["compound"] == 0:

                    pass

                elif prediction == "pos":

                    pos_intents.append(intents(rv.strip()))

                else:

                    neg_intents.append(intents(rv.strip()))

        pos = ", ".join([wd for ls in pos_intents for wd in ls])
        neg = ", ".join([wd for ls in neg_intents for wd in ls])

        print("pos")
        print(pos, "\n")
        print("neg")
        print(neg, "\n")

        overall_prediction = np_clf.predict([review])[0]

        print("Overall Review is:", overall_prediction, "\n")

        data = {
            'Review': review,
            'Positive Keywords': pos,
            'Negative Keywords': neg,
            "Overall Review": np_clf.predict([review])
        }

        df = pd.DataFrame(data)
        df.to_csv('final output.csv', mode='a', index=False, header=False)

        print("Output Saved")

        if (file == False):
            return(f"{pos}:{neg}:{overall_prediction}")

    else:

        print("Write the Review...")


