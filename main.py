import openai
openai.ai_key="fRs83irFgLS-XCQ-QBwf4jaURiG4hME5jUzzduT0FSm7rG1SPlssA"

def open_ai(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        message=[{
            "role":"User",
            "content":prompt
        }]
    )
    return response.choice[0].message.content.strip()

if __name__ =='__main__':
    while True:
        human_input = input("human input: ")
        if human_input.lower() in ["bye","quit"]:
          break
    response = open_ai(human_input)
    print("Open AI response: ",response)