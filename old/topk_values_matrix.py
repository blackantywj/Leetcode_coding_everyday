# https://stackoverflow.com/questions/31790819/scipy-sparse-csr-matrix-how-to-get-top-ten-values-and-indices

import numpy as np
import time 
from multiprocessing import Pool
import scipy.sparse as sparse

pred = np.random.rand(10,10)

print(pred)

class TopKCompressor():
    def __init__(self, k):
        self.k = k
#     def topk(self, matrix, K, axis=1):
#         if axis == 0:
#             row_index = np.arange(matrix.shape[1 - axis])
#             topk_index = np.argpartition(-matrix, K, axis=axis)[0:K, :]
#             topk_data = matrix[topk_index, row_index]
#             topk_index_sort = np.argsort(-topk_data,axis=axis)
#             topk_data_sort = topk_data[topk_index_sort,row_index]
#             topk_index_sort = topk_index[0:K,:][topk_index_sort,row_index]
#         else:
#             column_index = np.arange(matrix.shape[1 - axis])[:, None]
#             topk_index = np.argpartition(-matrix, K, axis=axis)[:, 0:K]
#             topk_data = matrix[column_index, topk_index]
#             topk_index_sort = np.argsort(-topk_data, axis=axis)
#             topk_data_sort = topk_data[column_index, topk_index_sort]
#             topk_index_sort = topk_index[:,0:K][column_index,topk_index_sort]
#         return topk_data_sort, topk_index_sort


    def _top_k(self, args):
        """
        Helper function to process a single row of top_k
        """
        data, row = args
        data, row = zip(*sorted(zip(data, row), reverse=True)[:self.k])
        return data, row

    def top_k(self, m, k):
        """
        Keep only the top k elements of each row in a csr_matrix
        """
        ml = m.tolil()
        with Pool() as p:
            ms = p.map(self._top_k, zip(ml.data, ml.rows))
        ml.data, ml.rows = zip(*ms)
        return ml.tocsr()
    def compress(self, matrix, K):
        matrix = sparse.csr_matrix(matrix)
        start = time.time() 
        print(self.top_k(matrix, K))
        end = time.time()
        print("using time is {:.20f}".format(end - start))
        residual = np.zeros((pred.shape))
        for n, i in enumerate(residual):
            i[indexes[n]] = values[n]
            residual[n] = i
        
        return residual

if __name__ == '__main__':
    cc = TopKCompressor(2)
    result = cc.compress(pred,2)
# print(largest_indices(pred, 2))