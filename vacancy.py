class Vacancy:
    def __init__(self, title, url, salary_min, salary_max, requirement):
        self.title = title
        self.url = url
        self.salary_min = salary_min
        self.salary_max = salary_max
        self.requirement = requirement

    def __str__(self):
        return f"{self.title}, {self.url}, {self.salary_min}, {self.salary_max}, {self.requirement}"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.salary_min == other.salary_min and self.salary_max == other.salary_max

    def __lt__(self, other):
        return self.salary_min < other.salary_min

    def __gt__(self, other):
        return self.salary_min > other.salary_min


    def as_dict(self):
        vacancy = {"title": self.title,
                   "url": self.url,
                   "salary_min": self.salary_min,
                   "salary_max": self.salary_max,
                   "requirement": self.requirement

                   }
        return vacancy