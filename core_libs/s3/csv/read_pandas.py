import pandas as pd


def read_from_s3_file(urlSource, sep="|"):
    """
    Read file from s3 and return a pandas DF full loaded in memory
    :param urlSource:
    :return: pd.DataFrame
    """

    return pd.read_csv(urlSource, sep=sep)
