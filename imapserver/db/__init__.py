class DbLayer(object):
    def __init__(self, model_name=None):
        self.model_name = model_name


Message = DbLayer('message')
Mailbox = DbLayer('mailbox')
User = DbLayer('user')
