import tornado.escape
import tornado.web
import tornado.gen
from RedisClient import RedisClient
from NYTimes import NYTimes

class IntentHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.payload = {}
        self.outcome = tornado.escape.json_decode(self.request.body)
        intent = self.outcome["intent"]
        if ("id" in self.outcome):
            self._id = self.outcome["id"]
        else:
            self.error_response("No id passed in outcome")
        if (intent == "get_headlines"):
            self.get_headlines()
        elif (intent == "get_summary"):
            self.get_summary()
        elif (intent == ""):
            self.get()
        else:
            self.error_response("No recognizable intent found")

    def get_headlines(self):
        NYTimes.get_headlines(self.respond_get_headlines)

    def respond_get_headlines(self, payload):
        self.payload = {
            "read": "Your articles today are: %s" % [0]
        }
        r = RedisClient()
        r.set(self._id + ":" + "articles", payload)
        self.finish_response()

    def get_summary(self):
        number_words = ["first", "second", "third", "fourth", "fifth", "sixth",
                        "seventh", "eigth", "ninth", "tenth"]
        r = RedisClient()
        articles = r.get(self._id + ":articles")
        entities = self.outcome["entities"]
        article = None
        if "topic" in entities:
            topic = entities["topic"]
            for article in articles:
                if topic in article:
                    article = article
                    break
        elif "nArticle" in entities:
            nArticle = entities["nArticle"]
            for i, number_word in enumerate(number_words):
                if number_word in nArticle:
                    if len(articles) >= i:
                        article = articles[i]
        else:
            self.error_response("No matching article")
        self.payload = {
            "read": "Your article is %s" % article
        }
        self.finish_response()

    def finish_response(self):
        self.payload["status"] = 200
        self.write(tornado.escape.json_encode(self.payload))
        self.finish()

    def error_response(self, reason):
        payload = {
            "status": 500,
            "reason": reason
        }
        self.write(tornado.escape.json_encode(payload))
        self.finish()
