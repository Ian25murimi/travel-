# Maxwell's Travel Package System

A simple python-based travel agency system that facilitates the management of travel packages, destinations, activities, and different types of passengers. The system supports Standard, Gold, and Premium passenger classes with varying privileges, providing a versatile solution for organizing and booking travel experiences.


## Features

- Travel Packages: Create and manage travel packages with destinations, activities, and passenger details.
- Passenger Types: Support for different passenger types (Bronze, Silver, Elite) with varying privileges.
- Activity Sign-up: Passengers can sign up for activities within the travel packages.


## Classes

- Activity: Represents an activity within a destination.
- Destination: Represents a destination in a travel package.
- TravelPackage: Represents a travel package with destinations and passengers.
- Passenger: Base class for different types of passengers.
- BronzePassenger: Subclass representing a bronze passenger.
- SilverPassenger: Subclass representing a silver passenger.
- EltePassenger: Subclass representing a elite  passenger.

### Class Descriptions

#### Activity

The Activity class represents an activity available within a destination. It includes properties such as name, description, cost, and capacity. Passengers can sign up for these activities.

#### Destination

The Destination class represents a specific location within a travel package. It contains a list of activities available at that destination.

#### TravelPackage

The TravelPackage class represents an entire travel package, comprising multiple destinations and managing the list of passengers. It also calculates charges based on passenger sign-ups for activities.

#### Passenger

The Passenger class serves as the base class for different types of passengers. It includes common attributes like name and passenger number.

#### BronzePassenger

The BronzePassenger subclass extends the Passenger class, representing passengers with a balance. They pay the full cost of activities, deducting from their balance.

#### SilverPassenger

The SilverPassenger subclass extends the Passenger class and provides a 10% discount on activity
