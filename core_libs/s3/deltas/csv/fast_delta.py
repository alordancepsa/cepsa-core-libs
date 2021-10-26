from core_libs.s3.csv import read_pandas
from core_libs.s3.deltas import delta_delete, delta_new, delta_update

def generate(s3Origin, s3OriginCompare, s3DeltaDestination, options):
    """
    bla bla bla
    """

    originDF = read_pandas(s3Origin)

    originCompareDF = read_pandas(s3OriginCompare)



    pass
