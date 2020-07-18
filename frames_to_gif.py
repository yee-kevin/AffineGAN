'''
Converts folder of image frames into a GIF
'''

import imageio
import glob

filepath = "./dataset/UTDAL_smile/generated/UTDAL_04651v113" + "/*"
filenames = glob.glob(filepath)

with imageio.get_writer('./GIFS/UTDAL_04651v113_generated.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)