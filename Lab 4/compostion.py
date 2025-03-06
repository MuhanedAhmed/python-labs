class Engine:
    def __init__(this, fuel_type, horsepower):
        this.fuel_type = fuel_type
        this.horsepower = horsepower

    def __repr__(this):
        return f"Engine(fuel_type={this.fuel_type}, horsepower={this.horsepower})"

class Car:
    def __init__(this, model, engine):
        this.model = model
        this.engine = engine

    def __repr__(this):
        return f"Car(model={this.model}, engine={this.engine})"

    def get_car_info(this):
        return f"The car of {this.model} has :\n\t- {this.engine.fuel_type} as fuel type\n\t- {this.engine.horsepower} horsepower"

my_engine = Engine(fuel_type="petrol", horsepower=200)

my_car = Car("Toyota", my_engine)

print(my_engine)
print(my_car)
print(my_car.get_car_info())