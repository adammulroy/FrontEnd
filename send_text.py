__author__ = 'adam.mulroy'

from twilio import rest


account = 'twilioaccount'
token = 'twiliotoken'

client = rest.TwilioRestClient(account, token)

call = client.calls.create(from_='8327802144',
                           to='8505869170',
                           url="http://twimlets.com/message?Message")