from google import genai
import os
from google.genai import types

# Configura client con API Key da variabile d'ambiente
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

safety_settings = [    
    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),    
    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
]

# configura la temperatura ossia il tipo di risposte 
config =types.GenerateContentConfig(
    temperature=0.2,
    max_output_tokens=1024,      #Lunghezza max risposte
     safety_settings=safety_settings,
)

response = client.models.generate_content(
    model="gemini-3.5-flash",    
    contents="Ciao! Chi sei?", 
    config=config,
    )

# Stampa output
print(response.text)