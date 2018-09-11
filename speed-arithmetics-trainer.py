"""
Created on 9/10/18

James Chan
"""
import numpy as np
import time

class Quiz:
    def __init__(self, num_questions=25):
#        self.num_questions = num_questions
#        self.problems = np.zeros((self.num_questions,3))
        
        self.categories = {'10to20':2,
                          'firstsamelastsum10':2,
                          'x11':2,
                          'almost100':2,
                          '9series':2,
                          '2digit':1,
                          '3digit':0,
                          'sq_last5':2,
                          'sq_2digit':1,
                          'sq_3digit':0}
        
        self.problems = np.empty((0,3))
        self.populate_quiz()
        
    def populate_quiz(self):
        for q_type, count in self.categories.items():
            for _ in range(count):
                q = self.get_question(q_type)
                q = np.array(q, ndmin=2)
                self.problems = np.vstack((self.problems, q))
        np.random.shuffle(self.problems)
    
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
    
    def start(self):
        wrongs = []
        print('-----------------quiz started, ' + str(self.problems.shape[0]) + ' problems')
        st = time.time()
        num_correct = 0
        for i in range(self.problems.shape[0]):
            print(self.problems[i,:-1])
            ans = float(raw_input('answer: '))
            if ans != self.problems[i,-1]:
                wrongs.append((i, ans))
            else:
                num_correct += 1
        lapsed = time.time()-st
        print('-----------------quiz complete in {} seconds, {}/{} correcct. wrong answers below'.format(lapsed, num_correct, self.problems.shape[0]))
        for i in range(len(wrongs)):
            prob_idx = wrongs[i][0]
            prob = self.problems[prob_idx,:-1]
            correct_ans = self.problems[prob_idx,-1]
            ans = wrongs[i][1]
            print('problem: {}, correct answer {}, your answer {}'.format(prob, correct_ans, ans))
    
    def show_answers(self):
        print('-----------------' + str(self.problems.shape[0]) + ' answers')
        for i in range(self.problems.shape[0]):
            print(self.problems[i,-1])
        
    def show_problems(self, style='normal'):
        print('-----------------' + str(self.problems.shape[0]) + ' problems')
        if style == 'normal':
            for i in range(self.problems.shape[0]):
                print(self.problems[i,:-1])
        if style == 'stacked':
            for i in range(self.problems.shape[0]):
                print(np.expand_dims(self.problems[i,:-1],1))
                print("")
        
    def add(q_type, num):
        pass
    
    def add_all_concept_equal_prob(self):
        pass
        
    def add_all_concept_rand_prob(self):
        pass

    def help(self):
        
        print("TBD")
    

if __name__=="__main__":
    
#{'10to20':5,
#  'firstsamelastsum10':5,
#  'x11':2,
#  'almost100':5,
#  '9series':2,
#  '2digit':30,
#  '3digit':10,
#  'sq_last5':5,
#  'sq_10to20':5,
#  'sq_almost100':5,
#  'sq_2digit':5,
#  'sq_3digit':5}
    np.random.seed(16519151)
    quiz = Quiz()
    quiz.start()
#    quiz.show_problems('normal')
#    quiz.show_problems('stacked')
#    quiz.show_answers()

