from concurrent.futures import ProcessPoolExecutor
import os
import timeit
from queue import Queue
from PIL import Image


def convert_image(image_path):
        image = Image.open('images/{}'.format(image_path))
        bw_image = image.convert('L')
        bw_image.save('output/bw_{}.jpg'.format(image_path))


def get_images():
    return os.listdir('images')


def main():
    t1 = timeit.default_timer()
    images_queue = Queue()
    original_images = get_images()
    for image in original_images:
        images_queue.put(image)
    with ProcessPoolExecutor(max_workers=4) as executor:
        executor.map(convert_image, original_images)
    print(timeit.default_timer() - t1)

if __name__ == '__main__':
    main()