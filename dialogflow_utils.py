import logging
from google.cloud import dialogflow


logger = logging.getLogger(__name__)

def get_dialogflow_response(project_id:str, session_id:str, text:str, language_code:str='ru'):
    logger.debug('Создана сессия Dialogflow')
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    text_input = dialogflow.TextInput(
        text=text,
        language_code='ru'
    )
    query_input = dialogflow.QueryInput(text=text_input)
    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )
    return response.query_result.fulfillment_text, response.query_result.intent.is_fallback
