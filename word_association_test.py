from math import sqrt
from unittest import TestCase

from word_association import create_graph

DATADIR = './data'


class WordAssociationTest(TestCase):
    def test_create_graph_assigns_correct_weights(self):
        graph = create_graph(DATADIR)

        self.assertEqual(1 / 141, graph['dym']['komin']['weight'], 'dym-komin association weight')
        self.assertEqual(sqrt((1 / 370) * (1 / 313)), graph['papieros']['tytoń']['weight'],
                         'papieros-tytoń association weight')
        self.assertEqual(1 / 2, graph['papieros']['to już było']['weight'], 'papieros-"to już było" association weight')
