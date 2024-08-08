import numpy as n
import pandas as p
d=p.DataFrame({"data":p.date_range(start="2023-09-07",periods=5,freq="D"),"temp":n.random.randint(18,30,size=5)})
d["f"]=d["temp"].shift(1)
print("shift:\n",d)
dfw=d.resample("M",on="data").mean()
print("\nresampling:\n",dfw)