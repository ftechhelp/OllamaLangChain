from Ollama import Ollama

# Create the client
client = Ollama()
#client.chat("What is the best way to learn and practice parkour?")
#client.prompt_template("What is the best way to learn and practice {activity}?", {"activity": "parkour"})
client.chat_prompt_template("You are an expert and teacher.", "What is the best way to learn and practice {activity}?", {"activity": "parkour"})
