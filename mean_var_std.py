import numpy as np

def calculate(list):
    # Memastikan list memiliki tepat 9 elemen
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Mengubah list menjadi array 3x3
    matrix = np.array(list).reshape(3, 3)

    # Menghitung statistik yang diminta
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum()]
    }

    return calculations
