import unittest
import numpy as np
from copy_of_scalable_agglomerative_clustering import cos_sim, get_embeddings

class TestScalableAgglomerativeClustering(unittest.TestCase):
    
    def test_cos_sim(self):
        a = np.array([1,1,1])
        b = np.array([2,2,2])
        result = cos_sim(a, b)
        self.assertAlmostEqual(result, 1.0)
        
    def test_get_embeddings(self):
        ids = [1,2,3]
        embeddings = {1: np.array([1,1,1]), 2:np.array([0,1,0]), 3:np.array([-1,1,-1])}
        result = get_embeddings(ids, embeddings)
        self.assertEqual(result.shape, (3,3))
        

if __name__ == "__main__":
    unittest.main()