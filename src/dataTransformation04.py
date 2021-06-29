import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation04(config_path):
    config = read_params(config_path)
    data_path = config["Stage4_preprocess"]["train_path"]
    resultant_df_path = config["Stage5_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    data_train['Route_1'] = ''
    data_train['Route_2'] = ''
    data_train['Route_3'] = ''
    data_train['Route_4'] = ''
    data_train['Route_5'] = ''
    combine = [data_train]
    for row in combine:
        row['Route_1'] = row['Route'].str.split('→ ').str[0]
        row['Route_2'] = row['Route'].str.split('→ ').str[1]
        row['Route_3'] = row['Route'].str.split('→ ').str[2]
        row['Route_4'] = row['Route'].str.split('→ ').str[3]
        row['Route_5'] = row['Route'].str.split('→ ').str[4]
    for row in combine:
        row['Route_1'].fillna("None", inplace=True)
        row['Route_2'].fillna("None", inplace=True)
        row['Route_3'].fillna("None", inplace=True)
        row['Route_4'].fillna("None", inplace=True)
        row['Route_5'].fillna("None", inplace=True)
    data_train.drop(['Route'], inplace=True, axis=1)




    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation04(config_path=parsed_args.config)