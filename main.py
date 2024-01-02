from service import Bot
message_faqbot={
    "hi!":"Hello!",
    "bye!":"Good bye!",
    "what is your name?": "My name is support"
}
faqBot=Bot("support", "data/faqBot_dict.csv")

message ='germaniA'
reply = faqBot.replyTo(message.lower())
print (reply)