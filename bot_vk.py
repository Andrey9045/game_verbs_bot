import os
import random
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from dotenv import load_dotenv
from dialogflow_utils import get_dialogflow_response

def message_handler(event, vk_api):
    session_id = f"vk-{event.user_id}"
    text = event.text
    answer, is_fallback = get_dialogflow_response(project_id, session_id, text)
    if not is_fallback:
        vk_api.messages.send(
            user_id=event.user_id,
            message=answer,
            random_id=random.randint(1, 1000)
        )


if __name__ == '__main__':
    load_dotenv()
    vk_token = os.environ["VK_TOKEN"]
    project_id = os.environ["ID_DF"]
    if not vk_token or not project_id:
        raise ValueError("Токен или ID не задан в .env")
    vk_session = vk_api.VkApi(token=vk_token)
    vk_api = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me:
            message_handler(event, vk_api)
