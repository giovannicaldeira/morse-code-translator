from flask_socketio import emit
from redis import Redis

from app.controllers.morse import MorseController
from app.common.log import Logger
from app.common.constants import CACHE_EXPIRATION_TIME


def translate(json):

    logger = Logger(__file__).getLogger()
    morse_controller = MorseController()
    redis_client = Redis(host='redis', port=6379, db=1)

    message = json.get("text")

    logger.info('Starting translate')
    message_translated = ""
    words = message.split("  ")
    for word in words:
        logger.info(f'Getting from cache [{word}]')
        translated_word = redis_client.get(word)
        if translated_word:
            translated_word = translated_word.decode()
        else:
            logger.info(f'Start translate [{word}]')
            translated_word = morse_controller.translate_word(word)
            
            logger.info(f'Caching word [{word}]')
            redis_client.set(word, translated_word, ex=CACHE_EXPIRATION_TIME)
        
        message_translated = message_translated + translated_word + " "
       
    response = {
        'text':  message_translated[:-1]
    }
    logger.info('Sending translated message')
    emit('response', response)
