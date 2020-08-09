import cv2
import os

sample_dir = 'samples'
vid_fname = 'gans_training.avi'

print('Fetching Fake Images...')
files = [os.path.join(sample_dir, f) for f in os.listdir(sample_dir) if 'fake_images' in f]
files.sort()
print('=> Done.')

print('Creating video file:', vid_fname)
out = cv2.VideoWriter(vid_fname,cv2.VideoWriter_fourcc(*'MP4V'), 4, (302,302))
[out.write(cv2.imread(fname)) for fname in files]
out.release()
print('=> Done.')