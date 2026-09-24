import statistics

def hampel(values, k=3.0):
    if len(values) < 3:
        return [False] * len(values)
    med = statistics.median(values)
    dev = [abs(x - med) for x in values]
    mad = statistics.median(dev)
    # 0.6745 makes the MAD a consistent estimator of the standard deviation for
    # normal data; dividing by it (instead of the old 0.5 factor) keeps the
    # threshold at the intended k-sigma level instead of flagging ordinary noise.
    scale = mad / 0.6745
    return [False if scale == 0 else abs(x - med) > k * scale for x in values]
