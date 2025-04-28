import pandas as pd

df=pd.read_excel(r"C:\Users\atefg\Downloads\SegmentDataPreview.xlsx")
silver=df[["Email Address","Address Line1","City","State","Zip"]]
silver
