import PyPDF2
import os
from googletrans import Translator

def main(input_file, output_file, target_language):
    translator = Translator()
    try:
        # Open the PDF file for reading
        with open(input_file, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            # Open the output file for writing with UTF-8 encoding
            with open(output_file, 'w', encoding='utf-8') as outfile:
                print("Translating and writing to file...")
                for page_num in range(len(pdf_reader.pages)):
                    try:
                        # Extract text from each page of the PDF
                        page = pdf_reader.pages[page_num]
                        text = page.extract_text()
                        # Translate the extracted text
                        translated_text = translator.translate(text, dest=target_language)
                        # Write the translated text to the output file
                        if translated_text is not None:
                            outfile.write(translated_text.text + '\n')
                        else:
                            print(f"Translation for page {page_num + 1} failed.")
                    except Exception as e:
                        print(f"An error occurred on page {page_num + 1}: {e}" + " You may ignore this.")
        print("Translation completed and written to", output_file)
    except Exception as e:
        print("An error occurred:", e)

def main_txt(input_file, output_file, target_language):
    translator = Translator()
    try:
        # Open the input file for reading with UTF-8 encoding
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Open the output file for writing
            with open(output_file, 'w', encoding='utf-8') as outfile:
                print("Translating and writing to file...")
                for line in infile:
                    # Strip leading and trailing whitespace from the line
                    line = line.strip()
                    if line:
                        # Translate non-empty lines
                        translated_line = translator.translate(line, dest=target_language)
                        if translated_line is not None:
                            # Write the translated line to the output file
                            if translated_line.text is not None:
                                outfile.write(translated_line.text + '\n')
                            else:
                                print("Skipping empty translation:", line)
                        else:
                            print("Skipping line:", line)

        print("Translation completed and written to", output_file)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__)) 
    print(script_dir) #Checks to make sure the script is in "..\File Translator" folder.

    input_path = os.path.join(script_dir, "To translate") #File path is in the "To translate" folder.
    input_file_name = input("What is the file name: ") + "."
    file_type = input("Is the file a pdf or txt? : ")
    input_file_name+=file_type
    input_path += "\\"+ input_file_name



    output_dir = os.path.join(script_dir, "Translated") #File Path is in the "Translated" folder
    output_name = input("What do you want to name the file: ") + ".txt"
    output_file_path = os.path.join(output_dir, output_name)
    target_language = input("What language do you want to output in (ie. en for english, es for spanish, etc.): ")  # Specify the target language here

    if input_path.lower().endswith(".pdf"):
        main(input_path, output_file_path, target_language)
    else:
        main_txt(input_path, output_file_path, target_language)
 
