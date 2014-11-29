import tornado.testing
import tornado.httputil

import os, sys, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir)

import server

class IntentsTests(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return server.get_app()

    @tornado.testing.gen_test
    def get_headlines(self):
        mock_outcome = {
            "_text" : "Whats happening today?",
            "intent" : "get_headlines",
            "entities" : { },
            "confidence" : 0.525
        }
        response = yield self.http_client.fetch(self.get_url("/"),
                                                method="POST",
                                                headers=tornado.httputil.HTTPHeaders({"content-type": "application/json"}),
                                                body=tornado.escape.json_encode(mock_outcome))
        payload = tornado.escape.json_decode(response.body)
        self.assertEqual(payload["status"], 200)
        self.assertEqual(payload["headlines"][0], "john")
