

class NonTransactionalSessionManager(object):
    """Override initial methods """
    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __exit__(self, type, value, traceback):
        self.session.close()
