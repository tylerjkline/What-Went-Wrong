# analyze.py
import openai
import sys

# Get the output file from the command-line arguments
output_file = sys.argv[1]

# Load the shell output
with open(output_file, "r") as file:
    shell_output = file.read()

# Initialize the OpenAI API
openai.api_key = 'YOUR-API-KEY-HERE'

# Send the output to the GPT-3.5 model
response = openai.Completion.create(
  engine="text-davinci-003",
  prompt=f"I am using linux and I have some output with a potential error:\n{shell_output}\nWhat could be wrong and how can I fix it? If necessary, please include specific details on how to fix. Also, please start off your response with Do not worry, be happy.",
  max_tokens=200
)

# Print the responsea
print(response.choices[0].text.strip())
