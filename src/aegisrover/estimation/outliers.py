import statistics

def hampel(values, k=3.0):
    if len(values) < 3:
        return [False] * len(values)
    med = statistics.median(values)
    dev = [abs(x - med) for x in values]
    mad = statistics.median(dev)
    # 1.4826 makes the MAD a consistent estimator of the standard deviation
    # for normal data; the previous 0.5 factor shrank the threshold to a
    # third of its proper size and flagged ordinary fluctuations as outliers.
    scale = 1.4826 * mad
    if scale == 0:
        # Zero spread: no robust scale exists, so nothing is an outlier.
        return [False] * len(values)
    return [abs(x - med) > k * scale for x in values]
