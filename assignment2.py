import numpy as np

def stat():
    # 1. Load data from populations.txt
    data = np.loadtxt("populations.txt")
    
    # Columns:
    # 0 -> Year
    # 1 -> Hare
    # 2 -> Lynx
    # 3 -> Carrot
    
    # 2. Extract Hare population column
    hare = data[:, 1]
    
    # 3. Find the year with minimum Hare population
    min_index = np.argmin(hare)
    min_year_hare = data[min_index, 0]
    
    # 4. Calculate average Lynx population
    lynx_avg = np.mean(data[:, 2])
    
    # 5. Create new_data with an extra column (sum of species per year)
    species_sum = np.sum(data[:, 1:], axis=1)
    new_data = np.column_stack((data, species_sum))
    
    # 6. Set Carrot population below 40000 to 0
    new_data[new_data[:, 3] < 40000, 3] = 0
    
    # 7. Return required outputs
    return data, hare, min_year_hare, lynx_avg, new_data
