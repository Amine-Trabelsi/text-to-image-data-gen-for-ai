# Text Image Generator

This project generates images from lines of text using the [Text Recognition Data Generator (trdg) library](https://github.com/Belval/TextRecognitionDataGenerator). 

The script reads lines from a text file and generates multiple images per line with varying styles.

## Setup

### Prerequisites

- Python 3.x
- pip

### Step-by-Step Instructions

1. **Clone the Repository**

    ```sh
    git clone https://github.com/yourusername/text-image-generator.git
    cd text-image-generator
    ```

2. **Create a Virtual Environment**

    It's recommended to use a virtual environment to manage dependencies.

    ```sh
    python -m venv env
    ```

3. **Activate the Virtual Environment**

    - On Windows:
        ```sh
        .\env\Scripts\activate
        ```
    - On macOS and Linux:
        ```sh
        source env/bin/activate
        ```

4. **Install Dependencies**

    Ensure you have the required libraries, specifically `pillow` version 9.5 and `trdg`.

    ```sh
    pip install trdg Pillow==9.5.0
    ```

5. **Adjust trdg Background Image Directory**

    It may be necessary to change the background image directory in the `trdg` library to point to the correct location.

    - Locate the `trdg` library in your virtual environment. This is typically found in `env/Lib/site-packages/trdg/` on Windows or `env/lib/python3.x/site-packages/trdg/` on macOS/Linux.
    
    - Navigate to the `background_generator.py` file. Change the image directory path from `trdg/images/` to `trdg/generators/images/`.

## Usage

1. **Prepare Input File**

    Create a text file named `input.txt` with each line containing a text that will become an image.

2. **Run the Script**

    Use the script provided in the repository to generate images from the text file. The script reads lines from `input.txt` and generates images with varying styles. The generated images are saved in the `output_images` directory.

    ```sh
    python main.py
    ```

## Notes

- **Virtual Environment**: Make sure to use a virtual environment and downlevel the Pillow library to version 9.5.0 to avoid compatibility issues.
- **Background Image Directory**: You may need to adjust the background image directory path in the `trdg` library to point to `trdg/generators/images/`.
