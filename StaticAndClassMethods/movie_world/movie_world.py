from StaticAndClassMethods.movie_world.dvd import DVD
from StaticAndClassMethods.movie_world.customer import Customer


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @classmethod
    def dvd_capacity(cls):
        return cls.DVD_CAPACITY

    @classmethod
    def customer_capacity(cls):
        return cls.CUSTOMER_CAPACITY

    def add_dvd(self, dvd:DVD):
        if len(self.dvds) < MovieWorld.DVD_CAPACITY:
            self.dvds.append(dvd)

    def add_customer(self, customer:Customer):
        if len(self.customers) < MovieWorld.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def rent_dvd(self, customer_id, dvd_id):
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        customer = [x for x in self.customers if x.id == customer_id][0]
        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"
        elif dvd.is_rented:
            return "DVD is already rented"
        elif dvd.age_restriction > customer.age:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"
        else:
            customer.rented_dvds.append(dvd)
            dvd.is_rented = True
            return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        dvd = [x for x in self.dvds if x.id == dvd_id][0]
        customer = [x for x in self.customers if x.id == customer_id][0]
        if dvd in customer.rented_dvds:
            customer.rented_dvds.remove(dvd)
            dvd.is_rented = False
            return f"{customer.name} has successfully returned {dvd.name}"
        else:
            return f"{customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        for cust in self.customers:
            result.append(cust)
        for dvd in self.dvds:
            result.append(dvd)
        return '\n'.join([str(x) for x in result])
