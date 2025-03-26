import os
import pandas as pd

html_path = "index.html"
writer = open(html_path, "w")
writer.write("<!DOCTYPE html>" + "\n")
writer.write("<html>" + "\n")
writer.write("<head>" + "\n")
writer.write("    <title>audios</title>" + "\n")
writer.write("</head>" + "\n")
writer.write("<body>" + "\n")

root = 'wavs'
for pair_flag in sorted(os.listdir(root)):
    pair_dir = os.path.join(root, pair_flag)
    for wav_name in sorted(os.listdir(pair_dir)):
        url = f'{root}/{pair_flag}/{wav_name}'
        item = "    <embed src='" + url + "'/>\n"
        writer.write(item)
        
writer.write("</body>" + "\n")
writer.write("</html>" + "\n")
writer.close()