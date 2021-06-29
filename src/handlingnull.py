import os
import argparse
import pandas as pd
from get_data import read_params


def HandlingMissingValues(config_path):
    config = read_params(config_path)
    raw_data_path = config["load_data"]["raw_dataset_csv"]
    train_data_nonull=config["Stage1_preprocess"]["train_path"]
    df = pd.read_csv(raw_data_path, sep=",")
    train = df.dropna()
    train.to_csv(train_data_nonull, sep=",", index=False, encoding="utf-8")

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    HandlingMissingValues(config_path=parsed_args.config)