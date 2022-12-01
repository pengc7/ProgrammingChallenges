#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import pandas as pd
from csv_combiner import csv_combiner

class TestCsvCombiner(unittest.TestCase):
        
    #test if the length and the number of columns of the combined file are correct
    
    def setUp(self):
        self.dirpath = ''
        self.files = ['accessories.csv','clothing.csv','household_cleaners.csv']
        self.flen, self.ncol, file_lst = [],[],[]
        for f in self.files:
            file = self.dirpath+f
            df = pd.read_csv(file)
            self.flen.append(len(df))
            self.ncol.append(len(df.columns))
            file_lst.append(file)
        self.combined_file = csv_combiner(file_lst)
    
    def test_length(self):
        assert len(self.combined_file)==sum(self.flen)

    def test_columns(self):
        assert len(self.combined_file.columns) == max(self.ncol)+1
        
    def tearDown(self):
        self.flen, self.ncol, self.combined_file = [],[],[]
    
if __name__ == '__main__':
    unittest.main()


# In[ ]:




