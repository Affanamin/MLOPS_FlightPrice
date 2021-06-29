import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation01(config_path):
    config = read_params(config_path)
    data_path = config["Stage1_preprocess"]["train_path"]
    resultant_df_path = config["Stage2_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")


    data_train['Journey_Day'] = pd.to_datetime(data_train.Date_of_Journey, format='%d/%m/%Y').dt.day
    data_train['Journey_Month'] = pd.to_datetime(data_train.Date_of_Journey, format='%d/%m/%Y').dt.month
    data_train['Journey_Year'] = pd.to_datetime(data_train.Date_of_Journey, format='%d/%m/%Y').dt.year
    data_train.drop(['Date_of_Journey'], axis=1, inplace=True)
    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation01(config_path=parsed_args.config)