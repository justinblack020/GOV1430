import pandas as pd
from openai import OpenAI

client = OpenAI()


# Assuming the existence of a function to query GPT-3.5, which we'll mock here
def query_gpt_3_5(prompt):
    message = {
        'role': 'user',
        'content': prompt
    }

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[message]
    )

    # Extract the chatbot's message from the response.
    # Assuming there's at least one response and taking the last one as the chatbot's reply.
    chatbot_response = response.choices[0].message.content
    return chatbot_response.strip()

# Load the dataset
file_path = 'Pennsylvania_DemographicsByZipCode_sample.xlsx'
df = pd.read_excel(file_path)

# Select 10 random rows from the dataset
df_sample = df.sample(n=10)

# Prepare your questions, with placeholders for the zip code
questions = [
    "What is the voter registration deadline for ZIP code ___?",
    "How can someone in ZIP code ___ request a mail-in ballot?",
    "Where is the nearest polling place for ZIP code ___?",
    "Can you vote by text message in ZIP code ___?",
    "What are the voting hours in ZIP code ___?"
]

# Initialize a list to hold your new dataset rows
zip_data_list = []

# Loop through each selected row, replace the placeholder with the zip code, query GPT-3.5, and store the response
# Loop through each selected row, replace the placeholder with the zip code, query GPT-3.5
for index, row in df_sample.iterrows():
    zip_code = row['Zip Code']  # Assuming your DataFrame has a 'Zip Code' column
    population = row['Population']  # Assuming your DataFrame has a 'Population' column
    zip_data = {'Zip Code': zip_code, 'Population': population}  # Initialize dictionary for this zip code
    
    for question_template in questions:
        # Replace the placeholder with the actual zip code
        question = question_template.replace("___", str(zip_code))
        # Query GPT-3.5
        answer = query_gpt_3_5(question)
        # Use a modified version of the question as the key for readability
        key = question_template[0:30] + "..."  # Example simplification
        zip_data[key] = answer
    
    # Add this zip code's data to the list
    zip_data_list.append(zip_data)

# Convert the list of dictionaries to a DataFrame
results_df = pd.DataFrame(zip_data_list)

# Display the DataFrame to check the structure
results_df.to_excel('data.xlsx', index=False, engine='openpyxl')
