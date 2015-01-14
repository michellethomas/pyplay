from collections import Counter
import email
from email.utils import parsedate
import nltk
from nltk.corpus import stopwords
import re
import time


def num_days(chats_dict):
    total = 0
    for key in chats_dict:
        total += 1
    return total

def print_dict(chats_dict):
    for key, value in chats_dict.iteritems():
        if key.endswith('13') or key.endswith('14'):
            print "%s: %s" %(key, value)

def most_common_words(chats_dict):
    stops = set(stopwords.words('english'))
    word_counts = Counter()
    for key, value in chats_dict.iteritems():
        if key.endswith('13') or key.endswith('14'):
            words = set(value.split())
            for word in words:
                if word.lower() not in stops:
                    word_counts[word.lower()] += 1
    return word_counts

def two_grams(chats_dict):
    phrase_counts = Counter()
    for key, value in chats_dict.iteritems():
        if key.endswith('13') or key.endswith('14'):
            words = value.split()
            for i in range(1, len(words)):
                phrase = words[i-1].lower() + " " + words[i].lower()
                phrase_counts[phrase] += 1
    return phrase_counts

def put_message_into_dict(payload, chats_dict, message_date):
    if message_date not in chats_dict:
        # Bad form, redo
        chats_dict[message_date] = payload.get_payload() + '\n'
    else:
        chats_dict[message_date] += payload.get_payload() + '\n'

f = open("/Users/michelle/Library/Thunderbird/Profiles/ru917dq9.default/ImapMail/imap.googlemail.com/[Gmail].sbd/Chats", "r")
f = f.read()
chat_lines = re.split(r'From - .*', f)
chats_dict = {}
for chat in chat_lines:
    message = email.message_from_string(chat.strip())
    sender = message["From"]
    receiver = message["To"]
    if (sender == 'Colin Pollock <pollockcolin@gmail.com>'
        or receiver == 'Colin Pollock <pollockcolin@gmail.com>'):
        message_date = time.strftime('%m-%d-%y',parsedate(message["Date"]))
        if message.is_multipart():
            for payload in message.get_payload():
                # if payload.is_multipart(): ...
                put_message_into_dict(payload, chats_dict, message_date)        
        else:
            put_message_into_dict(message, chats_dict, message_date)        

#print_dict(chats_dict)
print "Chat days: %d" %num_days(chats_dict)
print "common words:"
most_common = most_common_words(chats_dict).most_common(30)
for key, value in most_common:
    print "%s: %d" %(key, value)

print "common phrases"
common_phrases = two_grams(chats_dict).most_common(20)
for key, value in common_phrases:
    print "%s: %d" %(key, value)
