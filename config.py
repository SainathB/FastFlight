from authomatic.providers import oauth2

CONFIG = {
  'google': {
        'class_': oauth2.Google,
        'consumer_key': '583446649413-n7u4eu7snr2vrpdd3dohklhifvqjj5so.apps.googleusercontent.com',
        'consumer_secret': 'fFdaBGBB9XMOKJ777ZvnPWyb',
        'scope': oauth2.Google.user_info_scope,
    },
   
}
