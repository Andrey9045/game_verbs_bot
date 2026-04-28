import os
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from dialogflow_utils import get_dialogflow_response


load_dotenv()
VK_TOKEN = os.environ["VK_TOKEN"]
PROJECT_ID = os.environ["ID_DF"]

if not VK_TOKEN or not PROJECT_ID:
    raise ValueError("Токен или ID не задан в .env")


def message_handler(event, vk_api):
    session_id = event.user_id
    text = event.text
    answer, is_fallback = get_dialogflow_response(PROJECT_ID, session_id, text)
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    vk_session = vk_api.VkApi(token=VK_TOKEN)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message_handler(event, vk_api)
