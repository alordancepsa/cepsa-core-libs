def delta_new(yesterdayIDS, todayIDS):
    """
    Return ID's included today not included yesterday (NEW CLIENTS)
    """
    return list(set(todayIDS) - set(yesterdayIDS))

def delta_delete(yesterdayIDS, todayIDS):
    """
    Return ID's included yesterday not included today (REMOVED CLIENTS)
    """
    return list(set(yesterdayIDS) - set(todayIDS))


def delta_update(yesterdayDF, todayDF):
    """
    Return hashes not included Yesterday (modified or news clients)
    """
    yHasH = []
    for _, row in yesterdayDF.iterrows():

        yHasH.append(hash(tuple(row)))

    tHash = []
    for _, row in todayDF.iterrows():
        tHash.append(hash(tuple(row)))

    todayDF['hash'] = pd.Series(tHash)

    # return hash included today NOT included yesterday (modified or news)
    return list(set(tHash) - set(yHasH))

