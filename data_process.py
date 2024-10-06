import numpy as np
import pandas as pd

import os 

def convert_dta_to_csv(dta_path, output_folder):
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for root, dirs, files in os.walk(dta_path):
        for file in files:
            if file.endswith('.dta'):
                dta_file_path = os.path.join(root, file)
                csv_file_path = os.path.join(output_folder, file.replace('.dta', '.xlsx'))

                try:
                    df = pd.read_stata(dta_file_path)
                    df.to_csv(csv_file_path, index=False)
                    print(f'Successfully converted {dta_file_path} to {csv_file_path}')
                except Exception as e:
                    print(f'Error converting {dta_file_path} to {csv_file_path}: {str(e)}')

convert_dta_to_csv('/Users/albert/Documents/数据集/CHARLS2020r(1)', 'csv_output_folder_excel')
