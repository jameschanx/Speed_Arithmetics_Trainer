"""
Created on 9/10/18

James Chan
"""
import numpy as np

class Quiz:
    def __init__(self, num_questions=25):
#        self.num_questions = num_questions
#        self.problems = np.zeros((self.num_questions,3))
        
        self.categories = {'10to20':5,
                          'firstsamelastsum10':5,
                          'x11':2,
                          'almost100':5,
                          '9series':2,
                          'twodigit':10,
                          '3digit':10,
                          'sq_last5':5,
                          'sq_10to20':5,
                          'sq_almost100':5,
                          'sq_2digit':5,
                          'sq_3digit':5}
        
        self.problems = np.empty((0,3))
        self.populate_quiz()
        
    def populate_quiz(self):
        for items in self.categories.items():
            print(items)
    
    def get_question(q_type):
        if q_type == '10to20':
            np.random.randint(10,20)
        if q_type == 'firstsamelastsum10':
            pass
        if q_type == 'x11':
            pass
        if q_type == 'almost100':
            pass
        if q_type == '9series':
            pass
        if q_type == 'twodigit':
            pass
        if q_type == '3digit':
            pass
        if q_type == 'sq_last5':
            pass
        if q_type == 'sq_10to20':
            pass
        if q_type == 'sq_almost100':
            pass
        if q_type == 'sq_2digit':
            pass
        if q_type == 'sq_3digit':
            pass
    def show_answers(self):
        pass
        
    def show_problems(self):
        print(str(self.problems.shape[0]) + ' problems')
        for i in range(self.problems.shape[0]):
            print(self.problems[i,:-1])
        
    def add(q_type, num):
        pass
    
    def add_all_concept_equal_prob(self):
        pass
        
    def add_all_concept_rand_prob(self):
        pass

    def help(self):
        
        print("TBD")
    

if __name__=="__main__":
    quiz = Quiz()
    quiz.show_problems()
