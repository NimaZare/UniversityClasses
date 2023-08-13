class Teacher:
    def __init__(self, teacher_id, first_name, last_name):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name

    # Getter
    @property
    def teacher_id(self):
        return self._teacher_id
    
    # Setter
    @teacher_id.setter
    def teacher_id(self, teacher_id):
        if not teacher_id:
            raise ValueError("Missing teacher id!")
        self._teacher_id = teacher_id

    # Getter
    @property
    def first_name(self):
        return self._first_name
    
    # Setter
    @first_name.setter
    def first_name(self, first_name):
        if not first_name:
            raise ValueError("Missing teacher first name!")
        self._first_name = first_name
    
    # Getter
    @property
    def last_name(self):
        return self._last_name
    
    # Setter
    @last_name.setter
    def last_name(self, last_name):
        if not last_name:
            raise ValueError("Missing teacher last name!")
        self._last_name = last_name
    
