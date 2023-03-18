import secrets


class TokenGenerator:

    @staticmethod
    def get_session_token(self):
        pass

    @staticmethod
    def get_refresh_token(self):
        pass

    @staticmethod
    def get_file_token():
        file_token_id = secrets.token_hex(16)
        return file_token_id
