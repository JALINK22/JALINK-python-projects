


class Stadium:


    """ this explains the class"""
    
    def __init__(self, name, city_state, capacity):
        self.name = name
        self.city_state = city_state
        self.capacity = capacity


        """this explains the methods"""

    def describe_stadium(self):
        print("The " + self.name + " Arena is located in " + self.city_state + " and holds " + self.capacity + " fans.")


    def sport_played(self, sport):
        print("The following sport is mainly played in this stadium: " + sport)

    def seats_available(self, seats):
        print("There are " + seats + " seats still available for tonight's game.")


stadium1 = Stadium("Mercedes Benz", "Atlanta, GA", "70,000")
stadium1.describe_stadium()
stadium1.sport_played("Football")
stadium1.seats_available("15000")