from math import sqrt
from typing import Union
from pathlib import Path

import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

DATADIR = './data'
TARGETS = ['dym', 'palenie', 'papieros', 'tytoń']


def main():
    G = create_graph(DATADIR)

    for target in TARGETS:
        with open('shortests_paths_to_{}'.format(target), mode='w') as file:
            file.write('Shortest paths to "{}":\n'.format(target))
            for start, path in nx.shortest_path(G, target=target, weight='weight').items():
                file.write('from "{}": {}\n'.format(start, path))

    nx.draw(G)
    plt.show()


def create_graph(datadir: str, weight=lambda c: 1 / c, average=lambda x, y: sqrt(x * y)) -> nx.Graph:
    """
    Create association graph from data found in a given directory.

    :param average:
    :param weight:
    :param datadir: The directory in which data is found. Each file should contain word associations with counts
    for the word that is the name of the file (without the .csv extension)
    :return: A graph of word associations
    """

    graph = nx.Graph()

    for path in Path(datadir).iterdir():
        if path.is_file():
            word = path.stem
            for a, count in get_counts(path).items():
                if graph.has_edge(word, a):
                    graph.add_edge(word, a, weight=average(weight(count), graph[word][a]['weight']))
                else:
                    graph.add_edge(word, a, weight=weight(count))

    return graph


def get_counts(filepath: Union[str, Path]) -> dict:
    return pd.read_csv(filepath, header=None, index_col=1).to_dict()[0]


if __name__ == '__main__':
    exit(main())
