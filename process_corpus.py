import os

def read_text_files(input_folder):
    """Reads all text files from the input folder and returns their contents as a list of sentences."""
    sentences = []
    
    for filename in os.listdir(input_folder):
        if filename.endswith('.txt'):
            filepath = os.path.join(input_folder, filename)
            with open(filepath, 'r', encoding='utf-8') as file:
                content = file.read()
                sentences.extend(content.split('.'))
    
    # Remove empty sentences and strip whitespace
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    
    return sentences

def write_sentences_to_file(sentences, output_file, limit):
    """Writes the given sentences to the output file with a maximum number of lines specified by limit."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for i, sentence in enumerate(sentences):
            if i >= limit:
                break
            file.write(sentence + '.\n')

def process_text_files(input_folder, output_file, limit):
    """Reads text files from the input folder, splits them into sentences, and writes to the output file."""
    sentences = read_text_files(input_folder)
    write_sentences_to_file(sentences, output_file, limit)

# Example usage
input_folder = 'input'
output_file = 'input.txt'
limit = 100  # Set the maximum number of lines (sentences) to write

process_text_files(input_folder, output_file, limit)

print(f"Sentences written successfully to {output_file}.")
