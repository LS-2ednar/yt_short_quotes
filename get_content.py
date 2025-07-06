import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

#Main Setup
load_dotenv()

riddle_file = "./riddle_db.txt"
system_prompt = f"""You are a riddle creator master. You come up with clever riddles which should be solved by one sentence max. 
you should pack your riddles into lists which look like this  [riddle, answer_to_the_riddle].
if you are asked to create new riddles you should check the following file {riddle_file} to ensure that you do not provide the same riddle again. 
your output should only be the [riddles, answers to the riddles] as mentioned before no addional text output should be generated.
"""
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

message = "create 20 new riddles"
current_entries = []
def generate_content(client,message,riddle_file,goal_entries=1000):
    entries = 0
    while entries < goal_entries: 
        response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=f"{message} and ignore the following: {open(riddle_file,'r').read()}",
                config=types.GenerateContentConfig(system_instruction=system_prompt)
                )
        
        print("Done creating new riddles")
        with open(riddle_file,"a+") as f:
            entries = len([x for x in f.read() if x == "["])

        for line in response.text.split("\n"):
            print(line)
            f.write(f"\n{line}")
        f.close()
        print(f"Currently {entries} riddles out of {goal_entries} riddles have been generated.")

if __name__ == "__main__":
    generate_content(client,message,riddle_file)
