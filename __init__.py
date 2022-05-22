import subprocess

from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number


class IdasenController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('move-to-favorite.intent')
    def handle_move_to_favorite_position(self, message):
        favorite = message.data.get('favorite')
        self.speak(f'Moving to {favorite} position.')
        subprocess.run(['idasen-controller', '--move-to', favorite])


def create_skill():
    return IdasenController()

