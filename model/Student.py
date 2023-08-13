class Student:
    def __init__(self, student_id, first_name, last_name, lessons):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.lessons = lessons

    # Getter
    @property
    def student_id(self):
        return self._student_id
    
    # Setter
    @student_id.setter
    def student_id(self, student_id):
        if not student_id:
            raise ValueError("Missing student id!")
        self._student_id = student_id

    # Getter
    @property
    def first_name(self):
        return self._first_name
    
    # Setter
    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise ValueError("Missing student first name!")
        self._first_name = first_name
    
    # Getter
    @property
    def last_name(self):
        return self._last_name
    
    # Setter
    @last_name.setter
    def last_name(self, last_name):
        if not last_name:
            raise ValueError("Missing student last name!")
        self._last_name = last_name
    
    
    # Getter
    @property
    def lessons(self):
        return self._lessons
    
    # Setter
    @lessons.setter
    def lessons(self, lessons):
        self._lessons = lessons

