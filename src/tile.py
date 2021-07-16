import pyvips

impath = '/home/gryan/projects/nft/data/XE09-039_1_Tau_1.mrxs'

image = pyvips.Image.new_from_file(impath)
print(image )