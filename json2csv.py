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
import numpy as np
import pandas as pd

# Define the path and keypoints
path = r'D:\My Documents\projects\frailty\videos\video'
openpose_keypoints = [
    "nosex", "nosey", "neckx", "necky", "rshoulderx", "rshouldery", "relbowx", "relbowy",
    "rwristx", "rwristy", "lshoulderx", "lshouldery", "lelbowx", "lelbowy", "lwristx",
    "lwristy", "midhipx", "midhipy", "rhipx", "rhipy", "rkneex", "rkneey", "ranklex",
    "rankley", "lhipx", "lhipy", "lkneex", "lkneey", "lanklex", "lankley", "reyex",
    "reyey", "leyex", "leyey", "rearx", "reary", "learx", "leary", "lbigtoex", "lbigtoey",
    "lsmalltoex", "lsmalltoey", "lheelsx", "lheely", "rbigtoex", "rbigtoey", "rsmalltoex",
    "rsmalltoey", "rheelx", "rheely"
]

def get_file_paths(directory, extension=".json"):
    """Retrieve all file paths with the specified extension."""
    file_paths = []
    for root, _, files in os.walk(directory):
        file_paths.extend(os.path.join(root, file) for file in files if file.endswith(extension))
    return file_paths

def classify_folder_name(folder_name):
    """Classify folder name into a class label."""
    if "Normal" in folder_name:
        return 0
    elif "Abnormal" in folder_name:
        return 1
    elif "Fall" in folder_name:
        return 2
    return -1  # In case of unexpected folder names

def process_json_file(file_path):
    """Process a single JSON file and return its DataFrame and metadata."""
    folder_name = os.path.basename(os.path.dirname(file_path))
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    class_label = classify_folder_name(folder_name)
    combined_name = folder_name + file_name

    with open(file_path, encoding='utf-8') as inputfile:
        df = pd.read_json(inputfile)
        df = df.astype(str)
        df = df['people'].str.split(r":", expand=True)
        if not df.empty:
            df = df[df.columns[2]].str.split(r",", expand=True)
            df = df.apply(lambda x: x.str.replace('[','').str.replace(']',''))
            df = df.iloc[[0], :-1]
            return df, combined_name, class_label
    return pd.DataFrame(), combined_name, class_label

# Main processing
def main():
    file_paths = get_file_paths(path)
    
    results = [process_json_file(fp) for fp in file_paths]
    
    all_df, nnames, ffclass = zip(*results)
    
    # Convert lists to numpy arrays
    data = np.array([df.values.flatten() for df in all_df])
    idt = np.array(nnames)
    classd = np.array(ffclass)

    # Convert to DataFrame
    data_df = pd.DataFrame(data)
    idt_df = pd.DataFrame(idt, columns=['name'])
    classd_df = pd.DataFrame(classd, columns=['class'])

    # Concatenate dataframes
    final_df = pd.concat([idt_df, data_df, classd_df], axis=1)
    final_df.columns = openpose_keypoints

    # Save to CSV
    final_df.to_csv(os.path.join(path, 'keypoints.csv'), encoding='utf-8', index=False)

if __name__ == "__main__":
    main()
