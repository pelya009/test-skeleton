import traceback


class TransactionalSessionManager(object):
    """Override initial methods """

    def __init__(self, session):
        self.session = session

    def __enter__(self):
        return self.session

    def __del__(self):
        self.session.commit()
        self.session.close()

    def __exit__(self, err_type, err_value, err_traceback):
        if err_traceback:
            self.session.rollback()
            raise Exception(f"Transaction rolled back due to next reason: \n{err_value}\n"
                            f"Line number: {err_traceback.tb_lineno}\n"
                            f"Traceback: {''.join(traceback.format_tb(err_traceback))}")
        self.session.commit()
        self.session.close()
