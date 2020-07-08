import imageio
import glob

filepath = "./UTDAL_04651v113_generated" + "/*"
filenames = glob.glob(filepath)

with imageio.get_writer('./UTDAL_04651v113_generated.gif', mode='I') as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)