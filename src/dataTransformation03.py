import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation03(config_path):
    config = read_params(config_path)
    data_path = config["Stage3_preprocess"]["train_path"]
    resultant_df_path = config["Stage4_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    data_train['departure_Hour'] = pd.to_datetime(data_train.Dep_Time).dt.hour
    data_train['departure_Min'] = pd.to_datetime(data_train.Dep_Time).dt.minute
    data_train.drop(['Dep_Time'], axis=1, inplace=True)

    data_train['Arr_Hour'] = pd.to_datetime(data_train.Arrival_Time).dt.hour
    data_train['Arr_Min'] = pd.to_datetime(data_train.Arrival_Time).dt.minute
    data_train.drop(['Arrival_Time'], axis=1, inplace=True)

    combine = [data_train]
    titlemapping = {'non-stop': 0, '1 stop': 1, '2 stop': 2, '3 stop': 3, '4 stop': 4}
    for row in combine:
        row["Total_Stops"] = row["Total_Stops"].map(titlemapping)
        row['Total_Stops'] = row['Total_Stops'].fillna(0)
        row['Total_Stops'] = row['Total_Stops'].astype(int)


    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation03(config_path=parsed_args.config)