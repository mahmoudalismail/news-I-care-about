import datetime
import random

class Greeting:
  def __init__(self, username, request_time):
    self.username = username
    self.time = request_time
    self.phrases = []
    if self.time.time().hour < 12:
      tod = "morning"
    elif (self.time.time().hour >= 12 and self.time.time().hour < 17):
      tod = "afternoon"
    else:
      tod = "evening"
    self.phrases = [
      "Hello %s" % self.username,
      "Hi %s" % self.username,
      "Hey %s" % self.username,
      "Good %(tod)s %(user)s" % {'tod': tod, 'user': self.username}
    ]
    return self.phrases
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]  
  
class UpdatesOrNoUpdates:
  def __init__(self, updates=False):
    self.updates = updates
    if self.updates:
      self.phrases = [
        "I have some updates on stories you've been following. Would you like to hear them?",
        "I have some stories you may be interested in. Would you like to hear them?"
      ]
    else:
      self.phrases = [
        "Would you like to hear about what's going on today?",
        "Do you want me to tell you about today's headlines?",
        "Want me to fill you in on today's news?"
      ]
      
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
  
class FoundHeadlines:
  def __init__(self, sentence_headlines, topic_headlines):
    self.sentence_headlines = sentence_headlines
    self.topic_headlines = topic_headlines
    self.num_stories = len(self.sentence_headlines) + len(self.topic_headlines)
    first_sentence = ", ".join(self.sentence_headlines[:-1]) + ", and " + self.sentence_headlines[-1] + "."
    second_sentence = "I also have news about " + ", ".join(self.topic_headlines[:-1]) + ", and " + self.topic_headlines[-1] + "."
    self.base_phrase = "I have %s stories for you." % self.num_stories + " " + first_sentence + " " + second_sentence
    self.phrases = [
      "Are any of these interesting to you?",
      "Would you like to hear about any of these?",
      "Do you want me to tell you more about any of these stories?",
      "Do any of these interest you?",
      "Let me know if any of these stories interest you!"
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.base_phrase + " " + self.phrases[n]  
  
class LoadingConfirmation:
  def __init__(self, user_input=None):
    self.user_input = user_input
    self.phrases = [
      "Sure! Just give me a second to find that for you."
    ]
    subject = "some stories about %s" % self.user_input if self.user_input else "today's top stories"
    self.phrases.append("Okay! I will find you %s" % subject)
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
  
class SaveConfirmation:
  def __init__(self):
    self.phrases = [
      "Okay! I've saved this story for you to read later!",
      "I've saved the article to your Kindle so you can read it later.",
      "All done! When you have time, you can read this story on your Kindle."
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
  
class Media:
  def __init__(self):
    self.phrases = [
      "Here are the photos for this story.",
      "Here are some images from this article",
      "Here are the photos you requested."
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]
    
class Error:
  def __init__(self):
    self.phrases = [
      "I'm sorry, but I didn't understand what you said. Would you mind repeating that?",
      "I didn't quite catch that. Could you say that again?",
      "Can you please repeat your request for me?"
    ]
    
  def get_phrase(self):
    n = random.randrange(len(self.phrases))
    return self.phrases[n]