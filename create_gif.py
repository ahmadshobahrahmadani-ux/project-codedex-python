import imageio.v3 as iio

filenames = ['team-pic1', 'team-pic2']
images = [iio.imread(f'{filename}.png') for filename in filenames]

iio.imwrite('team-anim.gif', images, duration=500, loop=0)