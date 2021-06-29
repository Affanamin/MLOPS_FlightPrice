import os
import argparse
import pandas as pd
from get_data import read_params


def DataTransformation02(config_path):
    config = read_params(config_path)
    data_path = config["Stage2_preprocess"]["train_path"]
    resultant_df_path = config["Stage3_preprocess"]["train_path"]
    data_train = pd.read_csv(data_path, sep=",")

    duration = list(data_train['Duration'])

    for i in range(len(duration)):
        if len(duration[i].split()) != 2:
            if 'h' in duration[i]:
                duration[i] = duration[i].strip() + ' 0m'
            elif 'm' in duration[i]:
                duration[i] = '0h {}'.format(duration[i].strip())

    dur_hours = []
    dur_minutes = []

    for i in range(len(duration)):
        dur_hours.append(
            int(duration[i].split()[0][:-1]))  # for examole if duration is 49 mintutes 4 sec then it will reflect like
        dur_minutes.append(
            int(duration[i].split()[1][:-1]))  # 0:49:4 and if 2 hours 10 seconds then it will reflect like 2:0:10

    data_train['Duration_hours'] = dur_hours
    data_train['Duration_minutes'] = dur_minutes

    data_train.drop(labels='Duration', axis=1, inplace=True)  # dropping the original duration column from training set

    data_train.to_csv(resultant_df_path, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    DataTransformation02(config_path=parsed_args.config)