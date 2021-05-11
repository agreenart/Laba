from collections import defaultdict

schema_office_worker = (
    (
        ('schema_data', 'f'),
        ('schema_data', 'i'),
        ('schema_data', 'o'),
        ('schema_data', 'job'),
        ('schema_data', 'department'),
        ('date_day', range(1,31)),
        ('date_month', range(1,12)),
        ('date_year', range(2009,2020))
    ), '{} {} {}; {}; {}; {}_{}_{} \n' #csv
)

data_office_worker = {
    'i' : ['Alex', 'Anton', 'Gabe','Kevin', 'Konstantin',
           'Georg', 'Oleg', 'Andrew', 'Michael', 'Liza', 'Helen', 'Kate',
           'Alexander', 'Jake', 'Jim', 'Dwight', 'Glen', 'Tob', 'Tim', 'Victor','Cameron','Carl','Carlos','Charles',
           'Christopher','Cole','Connor','Caleb','Carter','Chase','Christian','Clifford','Cody','Colin','Curtis',
           'Cyrus','Daniel','David','Dennis','Devin','Diego','Dominic','Donald','Douglas','Dylan', 'Jack','Jackson',
           'Jacob','Jaden','James','Jason','Jayden','Jeffery','Jeremiah','Jesse','Jesus','John''Jonathan','Jordan',
           'Jose','Joseph','Joshua','Juan','Julian','Justin','Samantha','Sandra','Sara','Sarah','Savannah', 'Sharon',
           'Sheila', 'Shirley', 'Sierra', 'Sofia', 'Sophia', 'Stephanie', 'Susan', 'Sybil', 'Sydney', 'Sylvia','Mabel',
           'Mackenzie', 'Madeline', 'Madison', 'Makayla', 'Margaret', 'Maria', 'Marisa', 'Marjorie', 'Mary', 'Maya',
           'Megan', 'Melanie', 'Melissa', 'Mia', 'Michelle', 'Mildred', 'Molly', 'Monica', 'Aaliyah', 'Abigail', 'Ada',
           'Adelina', 'Agatha', 'Alexa', 'Alexandra', 'Alexis', 'Alise', 'Allison', 'Alyssa', 'Amanda', 'Amber', 'Amelia',
           'Angelina', 'Anita', 'Ann', 'Ariana', 'Arianna', 'Ashley', 'Audrey', 'Autumn', 'Ava', 'Avery'],

    'f' : ['Abbott', 'Acevedo', 'Acosta', 'Adams', 'Adkins','Aguilar', 'Aguirre', 'Alexander', 'Ali', 'Allen', 'Allison',
           'Alvarado', 'Alvarez', 'Andersen', 'Anderson', 'Andrade', 'Andrews', 'Anthony', 'Archer', 'Arellano', 'Arias',
           'Armstrong', 'Arnold', 'Arroyo', 'Ashley', 'Atkins', 'Atkinson', 'Austin', 'Avery', 'Avila', 'Ayala', 'Ayers',
           'Bailey', 'Baird', 'Baker', 'Baldwin', 'Ball', 'Ballard', 'Banks', 'Barajas', 'Barber', 'Barker', 'Barnes',
           'Barnett', 'Barr', 'Barrera', 'Barrett', 'Barron', 'Barry', 'Bartlett', 'Barton', 'Bass', 'Bates', 'Bauer',
           'Bautista', 'Baxter', 'Bean', 'Beard', 'Beasley', 'Beck', 'Becker', 'Bell', 'Beltran', 'Bender', 'Benitez',
           'Benjamin', 'Bennett', 'Benson', 'Bentley', 'Benton', 'Berg', 'Berger', 'Bernard', 'Berry', 'Best', 'Bird',
           'Bishop', 'Black', 'Blackburn', 'Blackwell', 'Blair', 'Blake', 'Blanchard', 'Blankenship', 'Blevins',
           'Bolton', 'Bond', 'Bonilla', 'Booker', 'Boone', 'Booth', 'Bowen', 'Bowers', 'Bowman', 'Boyd', 'Boyer',
           'Boyle', 'Bradford', 'Bradley', 'Bradshaw', 'Brady', 'Branch', 'Brandt', 'Braun', 'Bray', 'Brennan',
           'Brewer', 'Bridges', 'Briggs', 'Bright', 'Brook', 'Brown', 'Browning', 'Bruce', 'Bryan', 'Bryant',
           'Buchanan', 'Buck', 'Buckley', 'Bullock', 'Burch', 'Burgess', 'Burke', 'Burnett', 'Burns', 'Burton', 'Bush',
           'Butler', 'Byrd', 'Cabrera', 'Cain', 'Calderon', 'Caldwell', 'Calhoun', 'Callahan', 'Camacho', 'Cameron',
           'Campbell', 'Campos', 'Cannon', 'Cantrell', 'Cantu', 'Cardenas', 'Carey', 'Carlson', 'Carney', 'Carpenter',
           'Carr', 'Carrillo', 'Carroll', 'Carson', 'Carter', 'Case', 'Casey', 'Castaneda', 'Castillo', 'Castro',
           'Cervantes', 'Chambers', 'Chan', 'Chandler', 'Chaney', 'Chang', 'Chapman', 'Charles', 'Chase', 'Chavez',
           'Chen', 'Cherry', 'Choi', 'Christensen' ,'Helpert','Schrut','Scott','Openghemer','Remper','Vatorin','Kwit',
           'Wrong','Kot','Archi','Man','Shtich','Lot','Qot','Kim','Dom', 'Dorn','Nidal','Yodel','Kantarov'],

    'o' : ['Alex', 'Anton', 'Gabe','Kevin', 'Konstantin',
           'Georg', 'Oleg', 'Andrew', 'Michael', 'Liza', 'Helen', 'Kate',
           'Alexander', 'Jake', 'Jim', 'Dwight', 'Glen', 'Tob', 'Tim', 'Victor','Cameron','Carl','Carlos','Charles',
           'Christopher','Cole','Connor','Caleb','Carter','Chase','Christian','Clifford','Cody','Colin','Curtis',
           'Cyrus','Daniel','David','Dennis','Devin','Diego','Dominic','Donald','Douglas','Dylan', 'Jack','Jackson',
           'Jacob','Jaden','James','Jason','Jayden','Jeffery','Jeremiah','Jesse','Jesus','John''Jonathan','Jordan',
           'Jose','Joseph','Joshua','Juan','Julian','Justin','Samantha','Sandra','Sara','Sarah','Savannah', 'Sharon',
           'Sheila', 'Shirley', 'Sierra', 'Sofia', 'Sophia', 'Stephanie', 'Susan', 'Sybil', 'Sydney', 'Sylvia','Mabel',
           'Mackenzie', 'Madeline', 'Madison', 'Makayla', 'Margaret', 'Maria', 'Marisa', 'Marjorie', 'Mary', 'Maya',
           'Megan', 'Melanie', 'Melissa', 'Mia', 'Michelle', 'Mildred', 'Molly', 'Monica', 'Aaliyah', 'Abigail', 'Ada',
           'Adelina', 'Agatha', 'Alexa', 'Alexandra', 'Alexis', 'Alise', 'Allison', 'Alyssa', 'Amanda', 'Amber', 'Amelia',
           'Angelina', 'Anita', 'Ann', 'Ariana', 'Arianna', 'Ashley', 'Audrey', 'Autumn', 'Ava', 'Avery'],

    'job' : ['Intern','Manager','ITGuy','Accountant','Lawyer', 'Analyst', 'HR', 'DataScience', 'Someguy',
             'Toiletcliner','web designer', 'imposer', 'programmer', 'software tester', 'system administrator',
             'screenwriter of computer games', 'neural interface designer', 'ios developer', 'android developer',
             'database architect', 'database developer', 'network administrator', 'game developer', 'system engineer',
             'information systems specialist', 'front-end developer'],

    'department' : ['IT','Welfare','HR','Main','Innovation']
}

class OfficeWorkers :

    def __init__(self, fio='' , job ='', date='', department=''):
        self.fio = str(fio)
        self.job = str(job)
        self.date = str(date)
        self.department = str(department)
        self._sort_index2 = 'job'
        self._sort_index1 = 'fio'
        self.hash_index = 'fio'
        self.hash = Hashes.good_hash

    def __repr__(self):
        return 'OfficeWorker(' + str(self.fio) + ',' \
            + str(self.job) + ',' \
            + str(self.department) + ',' \
            + str(self.date) + ')'

    def __str__(self):
        return str(self.fio) + ';' \
               + str(self.job) + ';' \
               + str(self.department) + ';' \
               + str(self.date) + '\n'

    def __gt__(self, other):
        if not isinstance(other, OfficeWorkers):
            raise TypeError("Only for OfficeWorkers")
        return not self.__le__(other)

    def __lt__(self, other):
        if not isinstance(other, OfficeWorkers):
            raise TypeError("Only for OfficeWorkers")
        return not self.__ge__(other)

    def __ge__(self, other):
        if not isinstance(other, OfficeWorkers):
            raise TypeError("Only for OfficeWorkers")
        if getattr(self, self._sort_index1) == getattr(other, self._sort_index1):
            return getattr(self, self._sort_index2) >= getattr(other, self._sort_index2)
        else:
            return getattr(self, self._sort_index1) > getattr(other, self._sort_index1)

    def __le__(self, other):
        if not isinstance(other,OfficeWorkers):
            raise TypeError("Only for OfficeWorkers")
        if getattr(self, self._sort_index1) == getattr(other,self._sort_index1):
            return getattr(self, self._sort_index2) <= getattr(other,self._sort_index2)
        else:
            return getattr(self, self._sort_index1) < getattr(other, self._sort_index1)

    def set_sort_index(self, sort_index1, sort_index2):
        if sort_index1 in dir(self) and sort_index2 in dir(self):
            self._sort_index1 = sort_index1
            self._sort_index2 = sort_index2
        else:
            raise ValueError('Sort index ERROR')

    def __hash__(self):
        return self.hash(getattr(self, self.hash_index))

    def set_hash_type(self, hash_type):
        if hash_type == 'bad':
            self.hash = Hashes.bad_hash
        else:
            self.hash = Hashes.good_hash

    @property
    def fio(self):
        return self.fio

    @property
    def job(self):
        return self.job

    @property
    def date(self):
        return self.date

    @property
    def department(self):
        return self.department

    @property
    def get_sort_index(self):
        return self._sort_index1, self._sort_index2


class Hashes:

    @staticmethod
    def bad_hash(key):
        h = 0
        for _ in range(5):
            for i, el in enumerate(key):
                h += (i * ord(el) ^h * 11) & 0xFFFFFFFF
        return h

    @staticmethod
    def good_hash(key):
        h = 0
        for i, el in enumerate(key):
            h += ((i * ord(el)) - h * 11) & 0xFFFFFFFF
        return h


class HashTable:
    def __init__(self):
        self.table = defaultdict(list)
        self.collision_count = 0

    def add(self, object):
        index = hash(object)
        if self.table[index]:
            for element in self.table[index]:
                if getattr(object, object.hash_index) != getattr(element, element.hash_index):
                    self.collision_count += 1
                    #print("Find collision:", object, hash(object), element, hash(element))
                    break
        self.table[index].append(object)

    def get(self, object):
        return self.table[hash(object)]

    def __repr__(self):
        return str(self.table)