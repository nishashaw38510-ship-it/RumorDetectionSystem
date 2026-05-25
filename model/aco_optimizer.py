import random


def ant_colony_optimization(features):
    selected_features = []

    for feature in features:
        if random.random() > 0.5:
            selected_features.append(feature)

    return selected_features