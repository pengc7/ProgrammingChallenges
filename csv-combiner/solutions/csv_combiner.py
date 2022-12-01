#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import os, sys
import csv
import tracemalloc

def csv_combiner(csv_files):
    combined_df = None
    for file in csv_files:
        df = pd.read_csv(file)
        df['filename'] = os.path.basename(file)
        combined_df = pd.concat([combined_df, df], axis=0, copy=False, ignore_index=True)
    return combined_df


def main():
    tracemalloc.start()
    combined_csv = csv_combiner(csv_files).to_csv
    combined_csv(sys.stdout)
    print(tracemalloc.get_traced_memory())
    tracemalloc.stop()
    
if __name__ == "__main__":
    csv_files = sys.argv[1:]
    main()


# In[ ]:




