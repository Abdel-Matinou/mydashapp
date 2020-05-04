import pandas as pd
import numpy as np

def count_tickets(dataframe, column):
    count_dict = {}
    for x in dataframe[column]:
        tickets_by_item = dataframe[dataframe[column] == x].shape[0]
        count_dict[x] = tickets_by_item
    return count_dict
