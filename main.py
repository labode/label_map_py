import random
import sys
from PIL import Image, ImageDraw


def generate_map():
    increments = []

    i = 0

    while i < 256:
        increments.append(i)
        i += 25

    colors = []

    for i in increments:
        for j in increments:
            for k in increments:
                colors.append([i, j, k])

    random.shuffle(colors)

    # Move [0, 0, 0] to position 0 in array, because that is our background label
    colors.remove([0, 0, 0])
    colors.insert(0, [0, 0, 0])

    return colors


def plot_map(target_file, colors):
    image = Image.new('RGB', (750, 200), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    x = 0
    y = 0
    for color in colors:
        # fill is the inverse to our overlay use of the color codes, so we need to adapt for the plot
        draw.rectangle((x, y, x+9, y+9), fill=(255-color[0], 255-color[1], 255-color[2]))
        if x < 750:
            x += 10
        else:
            x = 0
            y += 10

    image.save(target_file + '.png')


def write_csv(target_file, labels):
    # Initiate File
    filename = str(target_file) + ".csv"
    output_file = open(filename, "w")

    for label in labels:
        output_file.write(str(label[0]) + ',' + str(label[1]) + ',' + str(label[2]) + '\n')

    output_file.close()


if __name__ == '__main__':
    file = sys.argv[1]

    error = False

    if not file:
        print("Missing parameters")
        # Explain the needed parameters to the user
        print("Please supply: filename")
        error = True

    color_map = generate_map()
    plot_map(file, color_map)
    write_csv(file, color_map)

