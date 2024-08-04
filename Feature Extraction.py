"""
MIT License

Copyright (c) 2024 Chollette C. Olisah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import pandas as pd
import numpy as np
from math import atan, degrees, sqrt

# Define the source directory
src_dir = r'D:\My Documents\projects\frailty\json'
os.chdir(src_dir)

def quadrant(cord, angle):
    """Determine the direction of the vector based on its quadrant."""
    if cord[0] > 0 and cord[1] > 0:  # 1st quadrant
        return angle
    elif cord[0] < 0 and cord[1] > 0:  # 2nd quadrant
        return 180 - angle
    elif cord[0] < 0 and cord[1] < 0:  # 3rd quadrant
        return 180 + angle
    elif cord[0] > 0 and cord[1] < 0:  # 4th quadrant
        return 360 - angle

def compute_vector_properties(row):
    """Compute direction and magnitude for vectors given a row of DataFrame."""
    vectors = [
        (row['nosex'] - row['neckx'], row['nosey'] - row['necky']),
        (row['neckx'] - row['rshoulderx'], row['necky'] - row['rshouldery']),
        (row['neckx'] - row['lshoulderx'], row['necky'] - row['lshouldery']),
        (row['rshoulderx'] - row['relbowx'], row['rshouldery'] - row['relbowy']),
        (row['relbowx'] - row['rwristx'], row['relbowy'] - row['rwristy']),
        (row['lshoulderx'] - row['lelbowx'], row['lshouldery'] - row['lelbowy']),
        (row['lelbowx'] - row['lwristx'], row['lelbowy'] - row['lwristy']),
        (row['neckx'] - row['midhipx'], row['necky'] - row['midhipy']),
        (row['midhipx'] - row['rhipx'], row['midhipy'] - row['rhipy']),
        (row['rhipx'] - row['rkneex'], row['rhipy'] - row['rkneey']),
        (row['rkneex'] - row['ranklex'], row['rkneey'] - row['rankley']),
        (row['midhipx'] - row['lhipx'], row['midhipy'] - row['lhipy']),
        (row['lhipx'] - row['lkneex'], row['lhipy'] - row['lkneey']),
        (row['lkneex'] - row['lanklex'], row['lkneey'] - row['lankley']),
        (row['lheelx'] - row['lbigtoex'], row['lheely'] - row['lbigtoey']),
        (row['rheelx'] - row['rbigtoex'], row['rheely'] - row['rbigtoey'])
    ]
    
    def vector_properties(vector):
        x, y = vector
        if x == 0:
            angle = 90 if y > 0 else 270
        else:
            angle = degrees(atan(abs(y / x)))
        direction = quadrant(vector, angle)
        magnitude = sqrt(x**2 + y**2)
        return direction, magnitude

    directions, magnitudes = zip(*[vector_properties(v) for v in vectors])
    return pd.Series([list(directions), list(magnitudes)], index=['directions', 'magnitudes'])

# Load DataFrame
df = pd.read_csv(os.path.join(src_dir, 'jsonXXX-no-z.csv'))

# Apply the function to compute directions and magnitudes
df[['directions', 'magnitudes']] = df.apply(compute_vector_properties, axis=1)

# Extract direction and magnitude DataFrames
direction_df = pd.DataFrame(df['directions'].tolist(), columns=[f"KG{i+1}" for i in range(16)])
magnitude_df = pd.DataFrame(df['magnitudes'].tolist(), columns=[f"KG{i+1}" for i in range(16)])

# Save DataFrames to CSV
direction_df.to_csv(os.path.join(src_dir, 'gradient_direction.csv'), index=True, encoding='utf-8')
magnitude_df.to_csv(os.path.join(src_dir, 'gradient_magnitude.csv'), index=True, encoding='utf-8')
