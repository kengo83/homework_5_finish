import csv
import pandas as pd

sample_data = [['001','りんご','100'], ['002','なし','120'], ['003','みかん','150'], ['004','ぶどう','200'], ['005','いちご','220']]
df = pd.DataFrame(sample_data)
df.to_csv('super.csv', index=False, header=False)