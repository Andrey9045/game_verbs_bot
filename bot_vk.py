import os
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from google.cloud import dialogflow


def detect_intent_texts(project_id, event, vk_api):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, event.user_id)
    text_input = dialogflow.TextInput(text=event.text, language_code='ru')
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    if not response.query_result.intent.is_fallback:
load_dotenv()
VK_TOKEN = os.environ["VK_TOKEN"]
PROJECT_ID = os.environ["ID_DF"]

if not VK_TOKEN or not PROJECT_ID:
    raise ValueError("Токен или ID не задан в .env")
        vk_api.messages.send(
            user_id=event.user_id,
            message=response.query_result.fulfillment_text,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.getenv("VK_TOKEN")
    project_id = 'exalted-ability-494118-b0'
    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            detect_intent_texts(project_id, event, vk_api)
