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
                          '2digit':30,
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
    
    def get_question(self, q_type):
        if q_type == '10to20':
            a = np.random.randint(11,20)
            b = np.random.randint(11,20)
        elif q_type == 'firstsamelastsum10':
            first = np.random.randint(1,10)
            a_second = np.random.randint(1,10)
            b_second = 10-a_second
            a = int(str(first) + str(a_second))
            b = int(str(first) + str(b_second))
        elif q_type == 'x11':
            nums = [11]
            nums.insert(np.random.randint(0,2), np.random.randint(10,1000))
            a = nums[0]
            b = nums[1]
        elif q_type == 'almost100':
            a = np.random.randint(95,106)
            b = np.random.randint(95,106)
        elif q_type == '9series':
            nines = [99,999]
            nums = [nines[np.random.randint(0,2)]]
            if nums[0] == 99:
                   nums.insert(np.random.randint(0,2), np.random.randint(10,100))
            else:
                   nums.insert(np.random.randint(0,2), np.random.randint(10,1000))
            a = nums[0]
            b = nums[1]
        elif q_type == '2digit':
            a = np.random.randint(10,100)
            b = np.random.randint(10,100)
        elif q_type == '3digit':
            a = np.random.randint(100,1000)
            b = np.random.randint(100,1000)
        elif q_type == 'sq_last5':
            first = np.random.randint(1,10)
            a = int(str(first) + str(5))
            b = a
        elif q_type == 'sq_10to20':
            a = np.random.randint(11,20)
            b = a
        elif q_type == 'sq_almost100':
            a = np.random.randint(95,106)
            b = a
        elif q_type == 'sq_2digit':
            a = np.random.randint(10,100)
            b = a
        elif q_type == 'sq_3digit':
            a = np.random.randint(100,1000)
            b = a
        return a,b,a*b
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
    
#        self.categories = {'10to20':5,
#                          'firstsamelastsum10':5,
#                          'x11':2,
#                          'almost100':5,
#                          '9series':2,
#                          'twodigit':10,
#                          '3digit':10,
#                          'sq_last5':5,
#                          'sq_10to20':5,
#                          'sq_almost100':5,
#                          'sq_2digit':5,
#                          'sq_3digit':5}
    quiz = Quiz()
    quiz.show_problems()
    print(quiz.get_question('sq_3digit'))
