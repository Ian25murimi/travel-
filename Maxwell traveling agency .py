import tkinter as tk
from tkinter import scrolledtext

class Activity:
    def __init__(self, name, description, cost, capacity, destination):
        self._name = name
        self.description = description
        self._cost = cost
        self._capacity = capacity
        self._destination = destination

    @property
    def name(self):
        return self._name

    @property
    def cost(self):
        return self._cost

    @property
    def capacity(self):
        return self._capacity

    @property
    def destination(self):
        return self._destination


class Destination:
    def __init__(self, name):
        self._name = name
        self._activities = []

    @property
    def name(self):
        return self._name

    @property
    def activities(self):
        return self._activities

    def add_activity(self, activity):
        self._activities.append(activity)


class PassengerType:
    BRONZE = "Bronze"
    SILVER = "Silver"
    ELITE = "Elite"


class Passenger:
    def __init__(self, name, passenger_number, passenger_type):
        self._name = name
        self._passenger_number = passenger_number
        self._type = passenger_type
        self._signed_up_activities = []
        self._balance = 0.0 if passenger_type != PassengerType.ELITE else None

    @property
    def name(self):
        return self._name

    @property
    def passenger_number(self):
        return self._passenger_number

    @property
    def balance(self):
        return self._balance

    @property
    def signed_up_activities(self):
        return self._signed_up_activities

    @property
    def type(self):
        return self._type

    def sign_up_for_activity(self, activity):
        # Implement signing up logic based on passenger type and available balance
        self._signed_up_activities.append(activity)


class TravelPackage:
    def __init__(self, name, passenger_capacity):
        self._name = name
        self._passenger_capacity = passenger_capacity
        self._passengers = []
        self._destinations = []

    @property
    def name(self):
        return self._name

    @property
    def passenger_capacity(self):
        return self._passenger_capacity

    @property
    def passengers(self):
        return self._passengers

    @property
    def destinations(self):
        return self._destinations

    def add_destination(self, destination):
        self._destinations.append(destination)

    def add_passenger(self, passenger):
        if len(self._passengers) < self._passenger_capacity:
            self._passengers.append(passenger)
        else:
            print("No more capacity for additional passengers")

    @staticmethod
    def print_itinerary(travel_package):
        root = tk.Tk()
        root.title("Itinerary")
        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30)
        text_area.grid(column=0, pady=10, padx=10)
        
        text_area.insert(tk.INSERT, f"Itinerary for {travel_package.name}\n")
        for destination in travel_package.destinations:
            text_area.insert(tk.INSERT, f"Destination: {destination.name}\n")
            for activity in destination.activities:
                text_area.insert(tk.INSERT, f"  Activity: {activity.name}, Cost: {activity.cost}, "
                                            f"Capacity: {activity.capacity}, Description: {activity.description}\n")
        
        text_area.config(state=tk.DISABLED)
        root.mainloop()

    @staticmethod
    def print_passenger_list(travel_package):
        root = tk.Tk()
        root.title("Passenger List")
        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30)
        text_area.grid(column=0, pady=10, padx=10)
        
        text_area.insert(tk.INSERT, f"Passenger list for {travel_package.name}\n")
        text_area.insert(tk.INSERT, f"Capacity: {travel_package.passenger_capacity}\n")
        text_area.insert(tk.INSERT, f"Number of passengers: {len(travel_package.passengers)}\n")
        for passenger in travel_package.passengers:
            text_area.insert(tk.INSERT, f"  Passenger: {passenger.name}, Number: {passenger.passenger_number}\n")
        
        text_area.config(state=tk.DISABLED)
        root.mainloop()

    @staticmethod
    def print_passenger_details(passenger):
        root = tk.Tk()
        root.title(f"Passenger Details - {passenger.name}")
        text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=30)
        text_area.grid(column=0, pady=10, padx=10)
        
        text_area.insert(tk.INSERT, f"Details for passenger {passenger.name}\n")
        text_area.insert(tk.INSERT, f"  Number: {passenger.passenger_number}\n")
        text_area.insert(tk.INSERT, f"  Balance: {passenger.balance}\n")
        text_area.insert(tk.INSERT, "  Activities:\n")
        for activity in passenger.signed_up_activities:
            price = TravelPackage.calculate_price(passenger, activity)
            text_area.insert(tk.INSERT, f"    Activity: {activity.name}, Destination: {activity.destination.name}, "
                                        f"Price: {price}\n")
        
        text_area.config(state=tk.DISABLED)
        root.mainloop()

    @staticmethod
    def calculate_price(passenger, activity):
        if passenger.type == PassengerType.ELITE:
            return 0.0  # Elite passengers sign up for free
        elif passenger.type == PassengerType.SILVER:
            return activity.cost * 0.9  # 10% discount for Silver passengers
        else:
            return activity.cost  # Bronze passengers pay the full cost


# Example usage of the classes and methods
if __name__ == "__main__":
    africa_trip = TravelPackage("Africa Trip", 100)
    tanzania = Destination("Tanzania")
    kenya = Destination("Kenya")

    sightseeing_tanzania = Activity("Sightseeing", "Explore mount kilimanjaro", 50.0, 30, tanzania)
    serengeti_park_visit_tanzania = Activity("Serengeti Park Visit", "Watch The Big 5", 20.0, 20, tanzania)
    mara_park_tour_kenya = Activity("Mara Park Tour", "Watch The Great Migration of Wildebeest", 30.0, 25, kenya)

    tanzania.add_activity(sightseeing_tanzania)
    tanzania.add_activity(serengeti_park_visit_tanzania)
    kenya.add_activity(mara_park_tour_kenya)

    africa_trip.add_destination(tanzania)
    africa_trip.add_destination(kenya)

    mark = Passenger("mark", 1, PassengerType.BRONZE)
    beatrice = Passenger("beatrice", 2, PassengerType.SILVER)
    martin = Passenger("martin", 3, PassengerType.ELITE)

    africa_trip.add_passenger(mark)
    africa_trip.add_passenger(beatrice)
    africa_trip.add_passenger(martin)

    mark.sign_up_for_activity(sightseeing_tanzania)
    beatrice.sign_up_for_activity(mara_park_tour_kenya)

    TravelPackage.print_itinerary(africa_trip)
    TravelPackage.print_passenger_list(africa_trip)
    TravelPackage.print_passenger_details(mark)
