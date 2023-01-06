from deepface import DeepFace
from matplotlib import pyplot as plt
import numpy as np
import math
import csv
import numba
from numba import jit, njit, vectorize, cuda, uint32, f8, uint8
from pylab import imshow, show
from timeit import default_timer as timer
import os
import time
import pandas as pd
import numpy as np
import xlsxwriter
import openpyxl
from openpyxl.utils import get_column_letter
from openpyxl.styles import Font
from glob import glob
try:
    # PIL
    import Image
except ImportError:
    # Pillow
    from PIL import Image

# function optimized to run on gpu 
@jit(target_backend='cuda')  
def process_image(img_path,i,img_filename):
    print ("Processing image...")

    #Do the processing
    #facial analysis
    attributes=['emotion']
    demography=DeepFace.analyze(img_path,actions=attributes)
    percentage_emotion=demography["emotion"]
    
    #Saving the data
    temp=pd.DataFrame(percentage_emotion,index=[i])
    temp_df = temp.reindex(columns = temp.columns.tolist() + ["Parkinson"])
    temp_df["Parkinson"]=temp_df["Parkinson"].fillna(0)
    temp_final=temp_df.reindex(columns = temp_df.columns.tolist() + ["img_filename"])
    temp_final["img_filename"]=img_filename
    new_df=pd.read_excel(excel_file, sheet_name='Sheet',index_col=0)
    df=temp_final.append(new_df,ignore_index=True)
    print(df)

    #Export the data to the excel
    writer=pd.ExcelWriter(excel_file,engine='xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet')

    #Convert the data from excel to csv file
    df.to_csv(csv_file,index=None, header=True)

    #Save the excel file
    writer.save()


images_dir="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Image"
excel_dir="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Excel"
excel_file="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Excel/Data.xlsx"
csv_file="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Excel/Data.csv"

if not os.path.exists(excel_dir):
    os.makedirs(excel_dir)

if not os.path.isfile('Data.xlsx'):
    wb = openpyxl.Workbook()  
    dest_filename = 'Data.xlsx' 
    wb.save(os.path.join(excel_dir, dest_filename))


if __name__ == "__main__":
    # List all JPEG files in your directory
    images_list = glob(os.path.join(images_dir, "*.jpg"))
    i=0

    for img_filename in images_list:
        img_path = os.path.join(images_dir, img_filename)
        start=timer()
        process_image(img_path,i,img_filename)
        print("with GPU:", timer()-start)
        i=i+1

