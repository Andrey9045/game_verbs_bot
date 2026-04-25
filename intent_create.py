import os
import json
from google.cloud import dialogflow
from dotenv import load_dotenv


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        # Here we create a new training phrase for each provided part.
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name, training_phrases=training_phrases, messages=[message]
    )

    response = intents_client.create_intent(
        request={"parent": parent, "intent": intent}
    )

    print("Intent created: {}".format(response))

def main():
    with open('questions.json', 'r', encoding='utf-8') as f:
    	data = f.read()
    questions = json.loads(data)
    for name, question_answer in questions.items():
        display_name = name
        training_phrases_parts = question_answer["questions"]
        message_texts = [question_answer["answer"]]
        create_intent('exalted-ability-494118-b0', display_name, training_phrases_parts, message_texts)

if __name__ == '__main__':
	load_dotenv()
	main()
