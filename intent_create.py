import os
import logging
import json
from google.cloud import dialogflow
from google.api_core.exceptions import AlreadyExists
from dotenv import load_dotenv


logger = logging.getLogger(__name__)


def create_intent(project_id, display_name, training_phrases_parts, message_texts):
    intents_client = dialogflow.IntentsClient()

    parent = dialogflow.AgentsClient.agent_path(project_id)
    training_phrases = []
    for training_phrases_part in training_phrases_parts:
        part = dialogflow.Intent.TrainingPhrase.Part(text=training_phrases_part)
        training_phrase = dialogflow.Intent.TrainingPhrase(parts=[part])
        training_phrases.append(training_phrase)

    text = dialogflow.Intent.Message.Text(text=message_texts)
    message = dialogflow.Intent.Message(text=text)

    intent = dialogflow.Intent(
        display_name=display_name,
        training_phrases=training_phrases,
        messages=[message]
    )
    try:
        response = intents_client.create_intent(
            request={"parent": parent, "intent": intent}
        )
    except AlreadyExists:
        logger.info("Такие intents уже созданы, уже имеющиеся пропущены")


def main():
    load_dotenv()
    project_id = os.environ["ID_DF"]
    if not project_id:
        raise ValueError("ID_DF не задан в .env")
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.DEBUG)
    with open('questions.json', 'r', encoding='utf-8') as f:
        questions = json.load(f)
    for name, question_answer in questions.items():
        display_name = name
        training_phrases_parts = question_answer["questions"]
        message_texts = [question_answer["answer"]]
        create_intent(
            project_id,
            display_name,
            training_phrases_parts,
            message_texts
        )

if __name__ == '__main__':
    main()
