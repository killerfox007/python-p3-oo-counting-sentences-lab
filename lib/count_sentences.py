#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
      self._value = ''
      self.value = value
    @property
    def value(self):
      return self._value
    @value.setter
    def value(self, argumentt):
      if isinstance(argumentt, str):
        self._value = argumentt
      else:
        print("The value must be a string.")

    def is_sentence(self):
      if isinstance(self._value, str) and self._value.endswith('.'):
        return True
      else:
        return False

    def is_question(self):
      if isinstance(self._value, str) and self._value.endswith('?'):
        return True
      else:
        return False

    def is_exclamation(self):
      if isinstance(self._value, str) and self._value.endswith('!'):
        return True
      else:
        return False
    def count_sentences(self):
      if not isinstance(self._value, str) or len(self._value) == 0:
        return 0
      sentences = [".", "?", "!"]
      count = 0 
      for characters in self._value:
        if characters in sentences:
          count += 1
      return count
