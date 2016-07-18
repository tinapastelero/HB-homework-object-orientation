"""
Part 1: Discussion

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

Three main advantages of object orientation are: (1) abstraction or the ability to hide the details we don't need but keep things organized, (2) encapsulation or the ability to keep all related details together, for example keeping subclass attributes together in separate subclasses, and (3) polymorphism, or the ability to interchange components based on how attributes are defined in parent and subclasses.

2. What is a class?
A class is an object for which specific attributes and methods can be defined.

3. What is an instance attribute?
An instance attribute is an attribute that is unique to that instance (not necessarily all members of that class).

4. What is a method?
A method is like a function that resides within a class and can be called by instances of that class.

5. What is an instance in object orientation?
An instance is one created "instance" of a class that has been created by the user.

6. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

A class attribute is something that applies to all instances of the class, while an instance attribute is something that applies to a specific instance of the class. For example, if we have a Class = "Hackbright Student," we can have a class attribute of cohort = "Summer 2016" which will apply to all students, and an instance attribute of name = "Tina" which will be unique to the instance of the student.

"""


# Parts 2 through 5:
# Create your classes and class methods



# PARTS 2 and 3 ===================


class Student(object):
    """Class to take in student information"""
    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """Class to take in questions"""
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

    def ask_and_evaluate(self):
        print self.question
        user_answer = raw_input('>>> ')
        if user_answer == self.answer:
            return True
        else:
            return False


class Exam(Question):
    """Class to build the exam"""
    question_list = []

    def __init__(self, name):
        self.name = name

    def add_question(self, question, answer):
        self.question = question
        self.answer = answer
        self.question_list.append((question, answer))

    def administer(self):
        score = 0   #initialize score as zero
        #iterate over tuples in list of questions
        #questions are item 1 in tuple, answers are item 2
        for question in self.question_list:
            self.question = question[0]
            self.answer = question[1]
            #call ask & evaluate method from parent Question
            ask_and_evaluate = super(Exam, self).ask_and_evaluate()
            #if result is True add 1 to score
            if ask_and_evaluate is True:
                score += 1
        #return final score when all questions in list are done
        return score


# PART 4 ===================

def take_test(exam, student):
    """Function to administer exam and assign final score to student

    Assumes exam and student have been instantiated
    Assigns output of Administer method as score, and creates new attribute score for instance of student"""

    #create new variable score to take in value of administered exam
    score = exam.administer()
    #assign output score to student
    student.score = score
    return score


def example(exam_name, questions_list, student_details):
    """Function that creates an exam, adds questions to exam, creates student, and administers test for student

    Assumes questions_list will be passed as list of tuples
    Assumes student_details will be passed as list"""

    #instatiate exam with parameter for exam name
    my_exam = Exam(exam_name)
    #using questions_list passed as argument, add questions to my_exam instance
    for item in questions_list:
        my_exam.add_question(item[0], item[1])
    #instantiate student based on passed argument 
    my_student = Student(student_details[0], student_details[1], student_details[2])
    score = take_test(my_exam, my_student)
    #return final score for the student
    return "{} {} got a score of {} on the {}.".format(my_student.first_name, my_student.last_name, score, my_exam.name)



# PART 5 ===================

class Quiz(Exam):
    """Subclass based on parent class Exam

    Administer method passes value of True or False instead of score based on percentage of correct answers"""

    #initialize quiz by calling parent class Exam and passing name
    def __init__(self, name):
        super(Quiz, self).__init__(name)

    #call super method from parent class Exam and return value of True or False based on percentage of questions answered correctly
    def administer(self):
        score = super(Quiz, self).administer()
        percent_score = score / len(self.question_list)
        if percent_score > 0.50:
            return True
        else:
            return False


"""
IGNORE BELOW THIS LINE 

sample inputs for classes

my_student = Student('Tina', 'Pastelero', '1365 Chestnut')
my_exam = Exam('mid')
my_exam.add_question('a','1')
my_exam.add_question('b','2')
my_exam.add_question('c','3')
take_test(my_exam,my_student)

my_quiz = Quiz('mini test')
my_quiz.add_question('a','1')
my_quiz.add_question('b','2')
my_quiz.add_question('c','3')

my_exam.administer()

exam_name = "midterm"
questions_list = [('a','1'), ('b','2'), ('c','3')]
student_details = ['Tina', 'Pastelero', '1365 Chestnut']
example(exam_name, questions_list, student_details)

"""




















