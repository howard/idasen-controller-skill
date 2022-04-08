from mycroft import MycroftSkill, intent_file_handler


class IdasenController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.idasen.intent')
    def handle_controller_idasen(self, message):
        self.speak_dialog('controller.idasen')


def create_skill():
    return IdasenController()

