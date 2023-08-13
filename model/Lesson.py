class Lesson:
    def __init__(self, lesson_id, name, teacher_name):
        self.lesson_id = lesson_id
        self.name = name
        self.teacher_name = teacher_name

    # # Getter
    # @property
    # def lesson_id(self):
    #     return self._lesson_id
    
    # # Setter
    # @lesson_id.setter
    # def lesson_id(self, lesson_id):
    #     if not lesson_id:
    #         raise ValueError("Missing Lesson id!")
    #     self._lesson_id = lesson_id
    
    # # Getter
    # @property
    # def name(self):
    #     return self._name
    
    # # Setter
    # @name.setter
    # def name(self, name):
    #     if not name:
    #         raise ValueError("Missing lesson name!")
    #     self._name = name

    # # Getter
    # @property
    # def teacher_name(self):
    #     return self._teacher_name
    
    # # Setter
    # @teacher_name.setter
    # def teacher_name(self, teacher_name):
    #     if not teacher_name:
    #         raise ValueError("Missing teacher name!")
    #     self._teacher_name = teacher_name
    
