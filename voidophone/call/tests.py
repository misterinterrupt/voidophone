import unittest2
from django.test import TestCase
from django.http import HttpResponse, HttpRequest
from BeautifulSoup import BeautifulStoneSoup
import twilio
from voidophone.call.views import index, listen, record, process_index
"""
Tests for the various Call controller Methods
"""
class CallTest(unittest2.TestCase):
    
    def test_index_view(self):
        """
        Tests that the index returns any # of <say> tags 
        followed by a <gather> with a <say> inside it
        And that all of it is inside of a <response>
        """
        webrequest = HttpRequest()
        
        response = index(webrequest)
        
        soup = BeautifulStoneSoup(response.__str__())
        
        self.failUnlessEqual(soup.contents[1].name, u'response', u'There was no Response tag in the response')
        self.assertGreater(len(soup.contents[1].findAll('say')), 0, u'There were no say tags in the response')
        self.assertGreater(len(soup.contents[1].findAll('gather')), 0, u'There wasn\'t a gather tag in the response')

    def test_process_index(self):
        """
        Tests that the correct menu options are available 
        and that they work
        """
        
        webrequest = HttpRequest()
        # choose 1 on the keypad
        webrequest.GET['Digits'] = 1

        response = process_index(webrequest)
        
        soup = BeautifulStoneSoup(response.__str__())
        r = soup.response
        redir = r.contents[1].name
        
        self.failUnlessEqual(r.name, u'response', u'There was no Response tag in the response')
        self.failUnlessEqual(redir, u'redirect', u'There was no listen tag in the response')
        
        # choose 2 on the keypad
        webrequest.GET['Digits'] = 2
        
        response = process_index(webrequest)
        
        soup = BeautifulStoneSoup(response.__str__())
        r = soup.response
        redir = r.contents[1].name
        
        self.failUnlessEqual(r.name, u'response', u'There was no Response tag in the response')
        self.failUnlessEqual(redir, u'redirect', u'There was no Redirect tag in the response')

    def test_listen(self):
        """
        test_listen should produce markup for serving an mp3
        """
        pass
        
    def test_record(self):
        """
        test_record should serve up recording markup
        """
        pass
        