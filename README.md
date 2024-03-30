## Documentation

This program takes a CSV file containing information on the nutrient content of various plant parts and transforms it into sentences suitable for a RAG database. These sentences can then be used by Large Language Models (LLMs) for improved interaction with the data, overcoming many issues that arise for tabular data in LLM's RAG library.

###  Input and Output Files

* Input file: The program expects a CSV file containing data on plant nutrients. The location of this file needs to be specified in the `in_file` variable.
* Output file: The program generates a text file containing the formulated sentences. The location of this file needs to be specified in the `out_file` variable.

### Program Logic

1. **Import libraries:** The program uses the `csv` library to read the CSV file.
2. **Define sentence template:** A string variable `sentence_template` holds the base structure of the sentence to be generated. This template includes placeholders for the plant's Latin name, plant part, and nutrient data with minimum and maximum ranges.
3. **Open CSV file:** The program opens the CSV file using the `with open` statement and the `csv.DictReader` function to access data as a dictionary.
4. **Iterate through rows:** The program loops through each row of the CSV data.
5. **Extract data:** For each row, relevant data points like `latin_name`, `plant_part`, and nutrient minimum/maximum values (e.g., `nitrogen_min`, `nitrogen_max`) are extracted.
6. **Handle missing data:** The program checks for missing data represented by '-' or '--' in the CSV file. It replaces these with 'unknown' or 'approximately 0' depending on the context.
7. **Generate sentence:** The extracted data is used to populate the placeholders in the `sentence_template`, resulting in a complete sentence about the nutrient content of a specific plant part.
8. **Refine sentence:** The program replaces the phrase "between unknown - unknown PPM" with "of unknown minimal quantities (0)" for better readability.
9. **Print and write sentence:** The generated sentence is printed to the console for verification and then written to the output text file.

## README

This README file provides information about the program that converts spreadsheet data on plant nutrients into sentences usable in a RAG database for LLMs.

**What it does:**

* Takes a CSV file containing plant nutrient data.
* Generates sentences describing the nutrient content of various plant parts.
* Outputs the sentences to a text file.

**How to use it:**

1. Update the `in_file` and `out_file` variables in the code with the paths to your specific input CSV and desired output text file locations.
2. Ensure you have the `csv` library installed (`pip install csv`).
3. Run the Python script.

**Output:**

* A text file containing sentences about the nutrient content of plants, formatted for use in a RAG database.

**Additional Notes:**

* The program handles missing data in the CSV file by replacing it with 'unknown' or 'approximately 0'.
* The output sentences use a consistent template for readability and ease of use by LLMs.
