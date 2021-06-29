
import os
import argparse
import pandas as pd
from get_data import read_params
from sklearn.preprocessing import LabelEncoder


def DataTransformation07(config_path):
    config = read_params(config_path)
    data_path = config["Stage7_preprocess"]["train_path"]
    resultant_df_path = config["Stage8_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    # So We will Use Label Encoder for Encoding Technique as we have text in our columns.

    encoder = LabelEncoder()
    data_train["Route_1"] = encoder.fit_transform(data_train['Route_1'])
    data_train["Route_2"] = encoder.fit_transform(data_train['Route_2'])
    data_train["Route_3"] = encoder.fit_transform(data_train['Route_3'])
    data_train["Route_4"] = encoder.fit_transform(data_train['Route_4'])
    data_train["Route_5"] = encoder.fit_transform(data_train['Route_5'])
    data_train = data_train.drop(
        ['Journey_Year', 'Additional_Info', 'Duration_minutes', 'departure_Min', 'Arr_Hour', 'Arr_Min', 'Route_1',
         'Route_2', 'Route_3', 'Route_4', 'Route_5'], axis=1)



    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation07(config_path=parsed_args.config)