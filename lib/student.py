#!/usr/bin/env python

from user import User

class Student(User):

    def __init__(self, first, last):
        super().__init__(first, last)
        self.knowledge = []
    
    def learn(self, idea):
        self.knowledge.append(idea)