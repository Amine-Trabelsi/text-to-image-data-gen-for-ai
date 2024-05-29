from trdg.generators import GeneratorFromStrings
import os
import random

def generate_images_from_file(input_file, output_dir, count_per_line=10):

    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Read lines from input file
    with open(input_file, 'r', encoding='utf-8') as file:
        lines = [line.strip() for line in file.readlines()]

    # Different styles
    font_paths = ["Alice-Regular.ttf", "AMERIKA_.ttf"]  # fonts
    ## fonts should be in the same folder as main.py

    font_sizes = [24, 32, 40, 48] 
    skewing_angles = [0, 5, 10, 15]
    backgrounds = [0, 1, 2, 3]
    ## if you face a problem with backgrounds, 
    ## change the place of the background images in the virtual environment accordingly
    blur_options = [True, False]

    # Iterate over each line and generate images with different styles
    for line in lines:
        for _ in range(count_per_line):
            # Randomly select a style
            font_path = random.choice(font_paths)
            font_size = random.choice(font_sizes)
            skewing_angle = random.choice(skewing_angles)
            background_type = random.choice(backgrounds)
            random_blur = random.choice(blur_options)

            # Create a generator with the selected style
            generator = GeneratorFromStrings(
                [line],
                count=1,
                fonts=[font_path],
                size=font_size,
                skewing_angle=skewing_angle,
                random_blur=random_blur,
                background_type=background_type
            )

            # Generate and save the image
            for i, (img, lbl) in enumerate(generator):
                # Create a unique filename for each image
                output_path = os.path.join(output_dir, f"{font_size}_{skewing_angle}_{background_type}_{random_blur}_{random.randint(1, 1000)}.png")
                img.save(output_path)
                print(f"Saved: {output_path}")

# Example usage
input_file = 'input.txt'
output_dir = 'output_images'
generate_images_from_file(input_file, output_dir)

print("Images generated successfully.")
