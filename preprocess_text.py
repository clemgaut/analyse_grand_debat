import json
import os
import pandas as pd
from spacy.lang.fr import French
import fr_core_news_md


def preprocess_file(file_path):
    json_data = []
    with open(file_path, encoding="utf8") as json_file:
        json_data = json.load(json_file)

    # Filters the question to only take into account the ones that have answers
    response_data = []
    for contrib in json_data:
        for response in contrib["responses"]:
            # Si on a une reponse non vide
            if response["value"] and response["formattedValue"]:
                # Flattens the responses and add it to the response data
                response_obj = dict(contrib)
                del response_obj["responses"]
                response_obj.update(response)
                response_data.append(response_obj)
    df_response_data = pd.DataFrame.from_records(response_data)

    df_response_data.to_json(os.path.join(data_dir, "response_" + os.path.basename(file_path)))

    # Loads the french model of spacy and adds some new stop words (could be extended)
    nlp = fr_core_news_md.load()
    tokenizer = French().Defaults.create_tokenizer(nlp)
    additional_stopwords = ["de", "le", "que", "ce", "l"]
    for stopword in additional_stopwords:
        nlp.Defaults.stop_words.add(stopword)

    # Creates a new column in the dataframe that contains each token lemma.
    # Punctuations, spaces and stopwords are removed
    df_response_data["lemmatizedValue"] = df_response_data["formattedValue"].\
        apply(lambda t: [token.lemma_ for token in tokenizer(t.lower()) if not token.is_stop and not token.is_punct and
                         not token.is_space])

    df_response_data.to_json(os.path.join(data_dir, "response_lemmatized_" + os.path.basename(file_path)))


if __name__ == "__main__":
    # Remplacer data_dir par votre dossier contenant les fichiers json
    data_dir = r"D:\Documents\data\grand_debat"
    datafiles = ["LA_FISCALITE_ET_LES_DEPENSES_PUBLIQUES.json", "DEMOCRATIE_ET_CITOYENNETE.json",
                 "LA_TRANSITION_ECOLOGIQUE.json", "ORGANISATION_DE_LETAT_ET_DES_SERVICES_PUBLICS.json"]

    for file in datafiles:
        preprocess_file(os.path.join(data_dir, file))