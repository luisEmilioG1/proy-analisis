from model import Optimize

import unittest
import numpy as np
from model import Optimize

class MyTestCase1(unittest.TestCase):

    def setUp(self) -> None:
        self.optimize = Optimize(
                [  
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                    [0,	1],
                ], 
                [   
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [1,	0],
                    [0,	1],
                ],
                [   
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                    [1,	0],
                    [0,	1],
                    [0,	1],
                    [1,	0],
                ]
            )

    def test_1(self):
        """ (ABC | AC=10 ) """
        distribution = self.optimize.get_probability_distribution(
                        c_state=[1, None, 0], 
                        f_state=[True, True, True]
                        )
        
        distribution_format = [ round(i, 2) for i in distribution ]
        self.assertListEqual(distribution_format, [0.25, 0.25, 0, 0, 0.25, 0.25, 0, 0])

    def test_2(self):
        """ (ABC | ABC=110) """
        distribution = self.optimize.get_probability_distribution(
                        c_state=[1, 1, 0], 
                        f_state=[True, True, True]
                        )
        
        distribution_format = [ round(i, 2) for i in distribution ]
        self.assertListEqual(distribution_format, [0, 1, 0, 0, 0, 0, 0, 0])

