
import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation06(config_path):
    config = read_params(config_path)
    data_path = config["Stage6_preprocess"]["train_path"]
    resultant_df_path = config["Stage7_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    # apply OneHotEncoding::
    dummies = pd.get_dummies(data_train.Airline)
    dummies_Source = pd.get_dummies(data_train.Source)
    data_train = pd.concat([data_train, dummies_Source], axis='columns')
    dummies_Destination = pd.get_dummies(data_train.Destination)
    data_train = pd.concat([data_train, dummies_Destination], axis='columns')

    data_train = data_train.drop(['Airline', 'Source', 'Destination'], axis=1)


    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation06(config_path=parsed_args.config)