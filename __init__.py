from mycroft import MycroftSkill, intent_file_handler


class SwitchToPrimaryLink(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('link.primary.to.switch.intent')
    def handle_link_primary_to_switch(self, message):
        self.speak_dialog('link.primary.to.switch')


def create_skill():
    return SwitchToPrimaryLink()

