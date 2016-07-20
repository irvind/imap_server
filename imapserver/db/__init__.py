class DbLayer(object):
    def __init__(self, model_name=None):
        self.model_name = model_name

    def select(self, order_by=None, **kwargs):
        pass

    def insert(self, **kwargs):
        pass


Message = DbLayer('message')
Mailbox = DbLayer('mailbox')
User = DbLayer('user')
