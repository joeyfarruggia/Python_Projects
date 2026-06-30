from openai import OpenAI

# Set up OpenAI client
client = OpenAI(
    api_key="API_KEY_HERE"   # ← Replace with your actual key
)

# Get user input for raw data
raw_data = input("Enter raw data: ")

# Preprocess the data (example: converting to lowercase)
preprocessed_data = raw_data.lower()

# Perform API call for data processing
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": preprocessed_data,
        }
    ],
    model="gpt-3.5-turbo",
)

# Get the generated output from the API response
generated_output = chat_completion.choices[0].message.content.strip()

# Print the generated output
print("Generated Output:")
print(generated_output)





from openai import OpenAI

# Set up OpenAI client
client = OpenAI(
    api_key="API_KEY_HERE"   # ← Replace with your actual key
)

# Prompt the user for an English sentence
english_sentence = input("Enter an English sentence: ")

# Create the translation prompt
prompt = f"Translate the following English sentence to Italian:\n\n{english_sentence}"

# Call the OpenAI API
response = client.chat.completions.create(
    model="gpt-4o-mini",          
    messages=[
        {"role": "system", "content": "You are a professional translator."},
        {"role": "user", "content": prompt}
    ],
    max_tokens=150,
    temperature=0.3,              # Good for accurate translations
)

# Extract and print the translation
italian_translation = response.choices[0].message.content.strip()

print("\nItalian Translation:")
print(italian_translation)