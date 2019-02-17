import os
import pandas as pd
import wordcloud


def generate_wordclouds(file_path):
    df_data = pd.read_json(file_path)

    text = " ".join([" ".join(lemma_contrib) for lemma_contrib in
                     df_data["lemmatizedValue"]])

    # I have some remaining stop words, that were apparently no filtered by spaCy, look into that
    remaining_stop_words = set(["le", "de", "ce", "ne", "yu", "que"])

    # Create and generate a word cloud image for the whole file:
    wc = wordcloud.WordCloud(stopwords=remaining_stop_words, max_words=150,
                             background_color="white").generate(text)

    os.makedirs("img", exist_ok=True)
    wc.to_file("img/" + os.path.basename(file_path) + "_150words.png")

    question_groups = df_data[["lemmatizedValue", "questionId", "questionTitle"]].groupby("questionId")
    for q_id, group in question_groups:
        text = " ".join([" ".join(lemma_contrib) for lemma_contrib in
                         group["lemmatizedValue"]])

        # Create and generate a word cloud image for each question
        wc = wordcloud.WordCloud(stopwords=remaining_stop_words, max_words=150,
                                 background_color="white").generate(text)

        wc.to_file("img/" + str(q_id) + "_" + os.path.basename(file_path) + "_150words.png")


if __name__ == "__main__":
    # Remplacer data_dir par votre dossier contenant les fichiers json
    data_dir = r"D:\Documents\data\grand_debat"
    datafiles = ["response_lemmatized_LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES.json",
                 "response_lemmatized_DEMOCRATIE_ET_CITOYENNETE.json",
                 "response_lemmatized_LA_TRANSITION_ECOLOGIQUE.json",
                 "response_lemmatized_ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.json"]

    for file in datafiles:
        generate_wordclouds(os.path.join(data_dir, file))