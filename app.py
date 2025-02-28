from JoshServerOllama import JoshServerOllama

# Create the client
client = JoshServerOllama()
#client.chat("What is the best way to learn and practice parkour?")
#client.prompt_template("What is the best way to learn and practice {activity}?", {"activity": "parkour"})
client.chat_prompt_template("You are an expert and teacher.", "What is the best way to learn and practice {activity}?", {"activity": "parkour"})
