from Application.GUI.Uis.Trello_Pin_Window_Ui.trello_pin_window_ui import *
from Application.Functions.trello_api.ping_authorization import *
from Application.Functions.trello_api.task_card import *
import json

os.environ["TRELLO_API_KEY"] = '2e0161c01eca7ad03bda843f811dac8b'
os.environ["TRELLO_API_SECRET"] = 'd4446e39644f0992f6db9859c77441754f0085ad5725d86699780d1ba86dfeea'

class trello_pin_window_ext(Ui_trello_pin_window):

    def __init__(self, trello, email, acct_window):
        super().__init__()
        self.trello = trello
        self.email = email
        self.parent = acct_window


    def setupUi(self, trello_pin_window):
        super().setupUi(trello_pin_window)
        self.trello_pin_window = trello_pin_window

        QtGui.QDesktopServices.openUrl(QtCore.QUrl(ping_oauth_link()))

        self.connect_trello_button.clicked.connect(self.enter_trello_pin)

    def enter_trello_pin(self):
        provided_pin = self.trello_pin_edit.text()

        if provided_pin == '':
            error_text = "Enter the pin provided in the link"

        else:

            self.trello_pin_edit.clear()
            ping_token = ping_oauth_pin(provided_pin)
            user_token = ping_token.get('oauth_token')
            user_token_secret = ping_token.get('oauth_token_secret')

            client = TrelloClient(
                api_key='2e0161c01eca7ad03bda843f811dac8b',
                api_secret='d4446e39644f0992f6db9859c77441754f0085ad5725d86699780d1ba86dfeea',
                # token = '3e1c54bc5ae2f18fe2e449c102c49b40400de0b39e2aca401dfc7a028c1ed33e',
                # token_secret = '298b5e59c4c09cff9666ba32fd381c5f'
                token=user_token,
                token_secret=user_token_secret
            )

            file = open("pinguin.json", "w")
            accounts = json.load(file)
            account = {self.email:{"token":user_token, "token_secret": user_token_secret}}
            accounts.append(account)
            file.close()

            self.trello.client = client
            self.parent.close()
