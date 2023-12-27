from PIL import Image, ImageDraw

# Sample pixel coordinates (replace with your list of coordinates)
pixel_coordinates = [(1, 1), (2, 2), (3, 2), (4, 3), (5, 3), (6, 4), (7, 4), (8, 5), (9, 6), (10, 6), (11, 7), (12, 7), (13, 8), (14, 8), (15, 9), (16, 9), (17, 10), (18, 11), (19, 11), (20, 12), (21, 12), (22, 13), (23, 13), (24, 14), (25, 15), (26, 15), (27, 16), (28, 16), (29, 17), (30, 17), (31, 18), (32, 19), (33, 19), (34, 20), (35, 20), (36, 21), (37, 21), (38, 22), (39, 22), (40, 23), (41, 24), (42, 24), (43, 25), (44, 25), (45, 26), (46, 26), (47, 27), (48, 28), (49, 28), (50, 29), (51, 29), (52, 30), (53, 30), (54, 31), (55, 32), (56, 32), (57, 33), (58, 33), (59, 34), (60, 34), (61, 35), (62, 35), (63, 36), (64, 37), (65, 37), (66, 38), (67, 38), (68, 39), (69, 39), (70, 40)]

# Create a blank image with a white background
width = 100
height = 100
image = Image.new("RGB", (width, height), color="white")

# Draw each pixel on the image
draw = ImageDraw.Draw(image)
for x, y in pixel_coordinates:
    draw.point((x, y), fill="black")  # Use point() for individual pixels

# Display the image
image.show()
