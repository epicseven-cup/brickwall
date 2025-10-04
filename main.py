from ollama import chat
from ollama import ChatResponse

# Fill in the model names and the prompt for each model to talk to each other
model1 = ""
model2 = ""

prompt1 = ""
prompt2 = ""
starter_message = "Hello!"


# Code
def setup():
    history1 = [
        {
            "role": "system",
            "content": f"Here is your character: {prompt1}, Your job is to keep the converstation going forever",
        },
        {"role": "user", "content": starter_message},
    ]
    history2 = [
        {
            "role": "system",
            "content": f"Here is your character: {prompt2}, Your job is to keep the converstation going forever.",
        }
    ]
    return history1, history2


def save_conv(path, name, content):
    with open(path, "a") as file:
        file.write(f"{name}: {content}\n\n")
    file.close()


def main():
    h1, h2 = setup()

    while True:
        response: ChatResponse = chat(
            model=model1,
            messages=h1,
        )
        content = response.message.content
        if content == None:
            content = "Sorry can you repeat that?"

        h1.append({"role": "assistant", "content": content})
        h2.append({"role": "user", "content": content})
        save_conv("data.txt", model1, content)

        response: ChatResponse = chat(
            model=model2,
            messages=h2,
        )

        content = response.message.content

        if content == None:
            content = "Sorry can you repeat that?"

        h1.append({"role": "user", "content": content})
        h2.append({"role": "assistant", "content": content})
        save_conv("data.txt", model2, content)


if __name__ == "__main__":
    main()
