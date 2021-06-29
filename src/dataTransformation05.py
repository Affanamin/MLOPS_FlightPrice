import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation05(config_path):
    config = read_params(config_path)
    data_path = config["Stage5_preprocess"]["train_path"]
    resultant_df_path = config["Stage6_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    # Any Airline having less than 6 data points termed as other category, We can called this as dimension reduction

    data_train.Airline = data_train.Airline.apply(lambda x: x.strip())
    Airline_stats = data_train['Airline'].value_counts(ascending=False)

    Airline_stats_less_than_10 = Airline_stats[Airline_stats <= 6]

    data_train.Airline = data_train.Airline.apply(lambda x: 'other' if x in Airline_stats_less_than_10 else x)
    dummies = pd.get_dummies(data_train.Airline)
    data_train = pd.concat([data_train, dummies], axis='columns')

    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation05(config_path=parsed_args.config)