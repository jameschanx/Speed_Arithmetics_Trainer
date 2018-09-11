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
        
        self.problems = np.zeros((sum(self.categories.values()),3))
        self.populate_quiz()
        
    def populate_quiz(self):
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
    quiz.show_problems()