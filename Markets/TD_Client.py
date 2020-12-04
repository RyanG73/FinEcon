from td.client import TDClient
# Create a new session, credentials path is optional.
TDSession = TDClient(
    client_id='<CLIENT_ID>',
    redirect_uri='<REDIRECT_URI>',
    credentials_path='<PATH_TO_CREDENTIALS_FILE>'
)

TDSession.login()


