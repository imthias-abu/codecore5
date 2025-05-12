def transition_score(tags1, tags2):
    """
    Compares two sets of tags and returns the transition score.
    """
    common_tags = tags1 & tags2
    only_in_first = tags1 - tags2
    only_in_second = tags2 - tags1
    return min(len(common_tags), len(only_in_first), len(only_in_second))


def score_order(frameglasses):
    """
    Goes through the list of frameglasses and adds up the transition scores.
    """
    total = 0
    for i in range(len(frameglasses) - 1):
        tags1 = frameglasses[i].tags
        tags2 = frameglasses[i + 1].tags
        total += transition_score(tags1, tags2)
    return total
