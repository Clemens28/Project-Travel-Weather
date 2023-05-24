import pandas as pd
import pyarrow as pa
import geopandas as gp
import pyautocad as pa
#df_01=pd.read_parquet('base_table.parquet', engine='pyarrow')



df_05=pa.read_file('Donauwrth20022023.dwg')