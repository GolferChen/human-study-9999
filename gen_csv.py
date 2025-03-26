
import numpy as np
import pandas as pd
import os

url_predix = "https://golferchen.github.io/human-study-9999"
info = dict()
info["audio_url"] = []

root = 'wavs'
for pair_flag in sorted(os.listdir(root)):
    pair_dir = os.path.join(root, pair_flag)
    for wav_name in sorted(os.listdir(pair_dir)):
        url = "{}/{}/{}/{}".format(url_predix, root, pair_flag, wav_name)
        url = f'<iframe src="{url}" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>'
        info["audio_url"].append(url)

df = pd.DataFrame(info)
df.to_csv("unshuffle-html.csv", index=False)
print(df)
df = df.sample(frac=1, random_state=666)
print(df)
df.to_csv("html.csv", index=False)