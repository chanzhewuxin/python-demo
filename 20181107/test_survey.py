import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    def setUp(self):
        """
        创建一个调查对象和一组答案，供使用的测试方法使用
        """
        self.question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(self.question)
        self.response=['English','Spanish','Mandarin']
        
    def test_store_single_response(self):
        # question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(self.question)
        my_survey.store_response(self.response[0])
        self.assertIn(self.response[0],my_survey.responses)

unittest.main()