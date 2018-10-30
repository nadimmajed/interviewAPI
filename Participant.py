__author__ = 'MyTEK'

class Participant:
    #initialize the attributes
    def __init__(self,interviewSubject,participantName,*availability):
        self.interviewSubject =interviewSubject
        self.participantName=participantName
        self.availability=availability
