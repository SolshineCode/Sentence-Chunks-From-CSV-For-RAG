import csv

in_file = 'LOCATION/Transformed_Nutrients_Data_New_1.csv' #Add path for input file
out_file = 'LOCATION/Bioaccumulator_Plant_Sentence_Chunks.txt' #Add path for output file

# Define the sentence template
sentence_template = "{latin_name} ({plant_part}) can provide the following nutrient ranges when made into a farming input or fertilizer: Nitrogen between {nitrogen_min} - {nitrogen_max} PPM, Phosphorus between {phosphorus_min} - {phosphorus_max} PPM, Potassium between {potassium_min} - {potassium_max} PPM, Aluminum between {aluminum_min} - {aluminum_max} PPM, Arsenic between {arsenic_min} - {arsenic_max} PPM, Boron between {boron_min} - {boron_max} PPM, Cadmium between {cadmium_min} - {cadmium_max} PPM, Calcium between {calcium_min} - {calcium_max} PPM, Cobalt between {cobalt_min} - {cobalt_max} PPM, Copper between {copper_min} - {copper_max} PPM, Fluoride between {fluoride_min} - {fluoride_max} PPM, Iodine between {iodine_min} - {iodine_max} PPM, Iron between {iron_min} - {iron_max} PPM, Lead between {lead_min} - {lead_max} PPM, Magnesium between {magnesium_min} - {magnesium_max} PPM, Manganese between {manganese_min} - {manganese_max} PPM, Mercury between {mercury_min} - {mercury_max} PPM, Molybdenum between {molybdenum_min} - {molybdenum_max} PPM, Selenium between {selenium_min} - {selenium_max} PPM, Silica between {silica_min} - {silica_max} PPM, Silver between {silver_min} - {silver_max} PPM, Sodium between {sodium_min} - {sodium_max} PPM, Sulfur between {sulfur_min} - {sulfur_max} PPM, Tungsten between {tungsten_min} - {tungsten_max} PPM, Zinc between {zinc_min} - {zinc_max} PPM."

# Open the CSV file and read its contents
with open(in_file, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    with open(out_file, 'w', encoding='utf-8') as output_file:
        for row in reader:
            # Extract the relevant data from the row
            latin_name = row['Latin Name']
            plant_part = row['Plant Part']
            aluminum_min = 'approximately 0' if row['Aluminum Min PPM'] and str(row['Aluminum Min PPM']).strip() in ('-', '--') else row['Aluminum Min PPM'] if row['Aluminum Min PPM'] else 'unknown'
            aluminum_max = 'approximately 0' if row['Aluminum Max PPM'] and str(row['Aluminum Max PPM']).strip() in ('-', '--') else row['Aluminum Max PPM'] if row['Aluminum Max PPM'] else 'unknown'
            arsenic_min = 'approximately 0' if row['Arsenic Min PPM'] and str(row['Arsenic Min PPM']).strip() in ('-', '--') else row['Arsenic Min PPM'] if row['Arsenic Min PPM'] else 'unknown'
            arsenic_max = 'approximately 0' if row['Arsenic Max PPM'] and str(row['Arsenic Max PPM']).strip() in ('-', '--') else row['Arsenic Max PPM'] if row['Arsenic Max PPM'] else 'unknown'
            boron_min = 'approximately 0' if row['Boron Min PPM'] and str(row['Boron Min PPM']).strip() in ('-', '--') else row['Boron Min PPM'] if row['Boron Min PPM'] else 'unknown'
            boron_max = 'approximately 0' if row['Boron Max PPM'] and str(row['Boron Max PPM']).strip() in ('-', '--') else row['Boron Max PPM'] if row['Boron Max PPM'] else 'unknown'
            cadmium_min = 'approximately 0' if row['Cadmium Min PPM'] and str(row['Cadmium Min PPM']).strip() in ('-', '--') else row['Cadmium Min PPM'] if row['Cadmium Min PPM'] else 'unknown'
            cadmium_max = 'approximately 0' if row['Cadmium Max PPM'] and str(row['Cadmium Max PPM']).strip() in ('-', '--') else row['Cadmium Max PPM'] if row['Cadmium Max PPM'] else 'unknown'
            calcium_min = 'approximately 0' if row['Calcium Min PPM'] and str(row['Calcium Min PPM']).strip() in ('-', '--') else row['Calcium Min PPM'] if row['Calcium Min PPM'] else 'unknown'
            calcium_max = 'approximately 0' if row['Calcium Max PPM'] and str(row['Calcium Max PPM']).strip() in ('-', '--') else row['Calcium Max PPM'] if row['Calcium Max PPM'] else 'unknown'
            cobalt_min = 'approximately 0' if row['Cobalt Min PPM'] and str(row['Cobalt Min PPM']).strip() in ('-', '--') else row['Cobalt Min PPM'] if row['Cobalt Min PPM'] else 'unknown'
            cobalt_max = 'approximately 0' if row['Cobalt Max PPM'] and str(row['Cobalt Max PPM']).strip() in ('-', '--') else row['Cobalt Max PPM'] if row['Cobalt Max PPM'] else 'unknown'
            copper_min = 'approximately 0' if row['Copper Min PPM'] and str(row['Copper Min PPM']).strip() in ('-', '--') else row['Copper Min PPM'] if row['Copper Min PPM'] else 'unknown'
            copper_max = 'approximately 0' if row['Copper Max PPM'] and str(row['Copper Max PPM']).strip() in ('-', '--') else row['Copper Max PPM'] if row['Copper Max PPM'] else 'unknown'
            fluoride_min = 'approximately 0' if row['Fluoride Min PPM'] and str(row['Fluoride Min PPM']).strip() in ('-', '--') else row['Fluoride Min PPM'] if row['Fluoride Min PPM'] else 'unknown'
            fluoride_max = 'approximately 0' if row['Fluoride Max PPM'] and str(row['Fluoride Max PPM']).strip() in ('-', '--') else row['Fluoride Max PPM'] if row['Fluoride Max PPM'] else 'unknown'
            iodine_min = 'approximately 0' if row['Iodine Min PPM'] and str(row['Iodine Min PPM']).strip() in ('-', '--') else row['Iodine Min PPM'] if row['Iodine Min PPM'] else 'unknown'
            iodine_max = 'approximately 0' if row['Iodine Max PPM'] and str(row['Iodine Max PPM']).strip() in ('-', '--') else row['Iodine Max PPM'] if row['Iodine Max PPM'] else 'unknown'
            iron_min = 'approximately 0' if row['Iron Min PPM'] and str(row['Iron Min PPM']).strip() in ('-', '--') else row['Iron Min PPM'] if row['Iron Min PPM'] else 'unknown'
            iron_max = 'approximately 0' if row['Iron Max PPM'] and str(row['Iron Max PPM']).strip() in ('-', '--') else row['Iron Max PPM'] if row['Iron Max PPM'] else 'unknown'
            lead_min = 'approximately 0' if row['Lead Min PPM'] and str(row['Lead Min PPM']).strip() in ('-', '--') else row['Lead Min PPM'] if row['Lead Min PPM'] else 'unknown'
            lead_max = 'approximately 0' if row['Lead Max PPM'] and str(row['Lead Max PPM']).strip() in ('-', '--') else row['Lead Max PPM'] if row['Lead Max PPM'] else 'unknown'
            magnesium_min = 'approximately 0' if row['Magnesium Min PPM'] and str(row['Magnesium Min PPM']).strip() in ('-', '--') else row['Magnesium Min PPM'] if row['Magnesium Min PPM'] else 'unknown'
            magnesium_max = 'approximately 0' if row['Magnesium Max PPM'] and str(row['Magnesium Max PPM']).strip() in ('-', '--') else row['Magnesium Max PPM'] if row['Magnesium Max PPM'] else 'unknown'
            manganese_min = 'approximately 0' if row['Manganese Min PPM'] and str(row['Manganese Min PPM']).strip() in ('-', '--') else row['Manganese Min PPM'] if row['Manganese Min PPM'] else 'unknown'
            manganese_max = 'approximately 0' if row['Manganese Max PPM'] and str(row['Manganese Max PPM']).strip() in ('-', '--') else row['Manganese Max PPM'] if row['Manganese Max PPM'] else 'unknown'
            mercury_min = 'approximately 0' if row['Mercury Min PPM'] and str(row['Mercury Min PPM']).strip() in ('-', '--') else row['Mercury Min PPM'] if row['Mercury Min PPM'] else 'unknown'
            mercury_max = 'approximately 0' if row['Mercury Max PPM'] and str(row['Mercury Max PPM']).strip() in ('-', '--') else row['Mercury Max PPM'] if row['Mercury Max PPM'] else 'unknown'
            molybdenum_min = 'approximately 0' if row['Molybdenum Min PPM'] and str(row['Molybdenum Min PPM']).strip() in ('-', '--') else row['Molybdenum Min PPM'] if row['Molybdenum Min PPM'] else 'unknown'
            molybdenum_max = 'approximately 0' if row['Molybdenum Max PPM'] and str(row['Molybdenum Max PPM']).strip() in ('-', '--') else row['Molybdenum Max PPM'] if row['Molybdenum Max PPM'] else 'unknown'
            nitrogen_min = 'approximately 0' if row['Nitrogen Min PPM'] and str(row['Nitrogen Min PPM']).strip() in ('-', '--') else row['Nitrogen Min PPM'] if row['Nitrogen Min PPM'] else 'unknown'
            nitrogen_max = 'approximately 0' if row['Nitrogen Max PPM'] and str(row['Nitrogen Max PPM']).strip() in ('-', '--') else row['Nitrogen Max PPM'] if row['Nitrogen Max PPM'] else 'unknown'
            phosphorus_min = 'approximately 0' if row['Phosphorus Min PPM'] and str(row['Phosphorus Min PPM']).strip() in ('-', '--') else row['Phosphorus Min PPM'] if row['Phosphorus Min PPM'] else 'unknown'
            phosphorus_max = 'approximately 0' if row['Phosphorus Max PPM'] and str(row['Phosphorus Max PPM']).strip() in ('-', '--') else row['Phosphorus Max PPM'] if row['Phosphorus Max PPM'] else 'unknown'
            potassium_min = 'approximately 0' if row['Potassium Min PPM'] and str(row['Potassium Min PPM']).strip() in ('-', '--') else row['Potassium Min PPM'] if row['Potassium Min PPM'] else 'unknown'
            potassium_max = 'approximately 0' if row['Potassium Max PPM'] and str(row['Potassium Max PPM']).strip() in ('-', '--') else row['Potassium Max PPM'] if row['Potassium Max PPM'] else 'unknown'
            selenium_min = 'approximately 0' if row['Selenium Min PPM'] and str(row['Selenium Min PPM']).strip() in ('-', '--') else row['Selenium Min PPM'] if row['Selenium Min PPM'] else 'unknown'
            selenium_max = 'approximately 0' if row['Selenium Max PPM'] and str(row['Selenium Max PPM']).strip() in ('-', '--') else row['Selenium Max PPM'] if row['Selenium Max PPM'] else 'unknown'
            silica_min = 'approximately 0' if row['Silica Min PPM'] and str(row['Silica Min PPM']).strip() in ('-', '--') else row['Silica Min PPM'] if row['Silica Min PPM'] else 'unknown'
            silica_max = 'approximately 0' if row['Silica Max PPM'] and str(row['Silica Max PPM']).strip() in ('-', '--') else row['Silica Max PPM'] if row['Silica Max PPM'] else 'unknown'
            silver_min = 'approximately 0' if row['Silver Min PPM'] and str(row['Silver Min PPM']).strip() in ('-', '--') else row['Silver Min PPM'] if row['Silver Min PPM'] else 'unknown'
            silver_max = 'approximately 0' if row['Silver Max PPM'] and str(row['Silver Max PPM']).strip() in ('-', '--') else row['Silver Max PPM'] if row['Silver Max PPM'] else 'unknown'
            sodium_min = 'approximately 0' if row['Sodium Min PPM'] and str(row['Sodium Min PPM']).strip() in ('-', '--') else row['Sodium Min PPM'] if row['Sodium Min PPM'] else 'unknown'
            sodium_max = 'approximately 0' if row['Sodium Max PPM'] and str(row['Sodium Max PPM']).strip() in ('-', '--') else row['Sodium Max PPM'] if row['Sodium Max PPM'] else 'unknown'
            sulfur_min = 'approximately 0' if row['Sulfur Min PPM'] and str(row['Sulfur Min PPM']).strip() in ('-', '--') else row['Sulfur Min PPM'] if row['Sulfur Min PPM'] else 'unknown'
            sulfur_max = 'approximately 0' if row['Sulfur Max PPM'] and str(row['Sulfur Max PPM']).strip() in ('-', '--') else row['Sulfur Max PPM'] if row['Sulfur Max PPM'] else 'unknown'
            tungsten_min = 'approximately 0' if row['Tungsten Min PPM'] and str(row['Tungsten Min PPM']).strip() in ('-', '--') else row['Tungsten Min PPM'] if row['Tungsten Min PPM'] else 'unknown'
            tungsten_max = 'approximately 0' if row['Tungsten Max PPM'] and str(row['Tungsten Max PPM']).strip() in ('-', '--') else row['Tungsten Max PPM'] if row['Tungsten Max PPM'] else 'unknown'
            zinc_min = 'approximately 0' if row['Zinc Min PPM'] and str(row['Zinc Min PPM']).strip() in ('-', '--') else row['Zinc Min PPM'] if row['Zinc Min PPM'] else 'unknown'
            zinc_max = 'approximately 0' if row['Zinc Max PPM'] and str(row['Zinc Max PPM']).strip() in ('-', '--') else row['Zinc Max PPM'] if row['Zinc Max PPM'] else 'unknown'

            # Generate the sentence using the template
            sentence = sentence_template.format(
                latin_name=latin_name,
                plant_part=plant_part,
                aluminum_min=aluminum_min,
                aluminum_max=aluminum_max,
                arsenic_min=arsenic_min,
                arsenic_max=arsenic_max,
                boron_min=boron_min,
                boron_max=boron_max,
                cadmium_min=cadmium_min,
                cadmium_max=cadmium_max,
                calcium_min=calcium_min,
                calcium_max=calcium_max,
                cobalt_min=cobalt_min,
                cobalt_max=cobalt_max,
                copper_min=copper_min,
                copper_max=copper_max,
                fluoride_min=fluoride_min,
                fluoride_max=fluoride_max,
                iodine_min=iodine_min,
                iodine_max=iodine_max,
                iron_min=iron_min,
                iron_max=iron_max,
                lead_min=lead_min,
                lead_max=lead_max,
                magnesium_min=magnesium_min,
                magnesium_max=magnesium_max,
                manganese_min=manganese_min,
                manganese_max=manganese_max,
                mercury_min=mercury_min,
                mercury_max=mercury_max,
                molybdenum_min=molybdenum_min,
                molybdenum_max=molybdenum_max,
                nitrogen_min=nitrogen_min,
                nitrogen_max=nitrogen_max,
                phosphorus_min=phosphorus_min,
                phosphorus_max=phosphorus_max,
                potassium_min=potassium_min,
                potassium_max=potassium_max,
                selenium_min=selenium_min,
                selenium_max=selenium_max,
                silica_min=silica_min,
                silica_max=silica_max,
                silver_min=silver_min,
                silver_max=silver_max,
                sodium_min=sodium_min,
                sodium_max=sodium_max,
                sulfur_min=sulfur_min,
                sulfur_max=sulfur_max,
                tungsten_min=tungsten_min,
                tungsten_max=tungsten_max,
                zinc_min=zinc_min,
                zinc_max=zinc_max
            )
            
            # Replace "unknown - unknown PPM" with "of unknown minimal quantities"
            sentence = sentence.replace('between unknown - unknown PPM', 'of unknown minimal quantities (0)')

            # Print the generated sentence
            print(sentence)
            print()  # Add a blank line for readability
            
            # Write the sentence to the output file
            output_file.write(sentence + '\n\n')