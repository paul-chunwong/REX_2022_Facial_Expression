from deepface import DeepFace
from deepface.basemodels import VGGFace
import matplotlib.pyplot as plt
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

def process_image(img_path,i):
    print ("Processing image...")

    # Open the image
    img=Image.open(img_path)
    img.show()

    #Do the processing
    #facial analysis
    attributes=['emotion']
    demography=DeepFace.analyze(img_path,actions=attributes)
    percentage_emotion=demography["emotion"]
    
    #Saving the data
    temp=pd.DataFrame(percentage_emotion,index=[i])
    temp_df = temp.reindex(columns = temp.columns.tolist() + ["Parkinson"])
    temp_df["Parkinson"]=temp_df["Parkinson"].fillna(0)
    new_df=pd.read_excel(excel_file, sheet_name='Sheet',index_col=0)
    df=temp_df.append(new_df,ignore_index=True)
    print(df)

    #Export the data to the excel
    writer=pd.ExcelWriter(excel_file,engine='xlsxwriter')
    df.to_excel(writer,sheet_name='Sheet')

    #Save the excel file
    writer.save()

    #Close the images
    img.close()

images_dir="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Image"
excel_dir="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Excel"
excel_file="C:/Users/ChrisRA/Desktop/URO_2022/deepface/Excel/Data.xlsx"


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
        process_image(img_path,i)
        i=i+1

