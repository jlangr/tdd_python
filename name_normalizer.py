import re


class InvalidNameException(Exception):
    pass


class NameNormalizer:
    def __init__(self, name):
        if name.count(',') > 1:
            raise InvalidNameException
        if ',' in name:
            [self.base_name, self.suffix] = name.split(',')
            self.suffix = f",{self.suffix}"
        else:
            self.base_name = name
            self.suffix = ''
        self.parts = re.split('\\s+', self.base_name.strip())

    def normalize(self):
        if self.is_mononym():
            return self.parts[0]
        if self.is_duonym():
            return f"{self.last()}, {self.first()}"
        return f"{self.last()}, {self.first()} {self.middle_initials()}{self.suffix}"

    def first(self):
        return self.parts[0]

    def last(self):
        return self.parts[-1]

    def is_mononym(self):
        return len(self.parts) == 1

    def is_duonym(self):
        return len(self.parts) == 2

    def middle_initials(self):
        # pass  # what does pass mean
        middle_initials = \
            [self.initial(name) for name in self.parts[1:-1]]
        return ' '.join(middle_initials)

    def initial(self, name):
        return f'{name[0]}.'
