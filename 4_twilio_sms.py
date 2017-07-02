from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC18aa6a3c5577b7c75178db63eee7####"
# Your Auth Token from twilio.com/console
auth_token  = "d6cb691dbf817352d26d3#########"
#qaQ3Zy25uHdJcHQnz9yRIOY8BXzxNzuiCF
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(
    to="+91xxxxxxxxxx", 
    from_="+152xxxxxxxxx",
    body="Hello ZeroConfig Test 3 Testing Python Send SMS using Twilio API!")
print(message.sid)