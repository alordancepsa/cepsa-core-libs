
def save_pd_to_s3(dataFrame, urlDestination, sep="|"):
    """
    Save file to s3

    :param dataFrame:
    :param urlDestination:
    """

    dataFrame.to_csv(urlDestination, index=False, sep=sep)

