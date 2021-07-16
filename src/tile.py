import pyvips

impath = '/home/gryan/projects/nft/data/XE09-039_1_Tau_1.mrxs'
dir = '/'.join(impath.split('/')[:-1])


image = pyvips.Image.new_from_file(impath, level=0)

crop_square = 10
tile_size = 256
left, top = image.width // 2, image.height // 2
left1, top1 = left - crop_square * tile_size, top - crop_square * tile_size
left2, top2 = left + crop_square * tile_size, top + crop_square * tile_size

big_tile = image.crop(left1, top1, left2 - left1, top2 - top1)
big_tile.tiffsave(dir + '/large_tile.tif')

for i in range(0, crop_square * 2 * tile_size, tile_size):
    for j in range(0, crop_square * 2 * tile_size, tile_size):
        big_tile.crop(i, j, i + tile_size, j + tile_size).tiffsave(dir + f'/crop/{i},{j}.tif')

