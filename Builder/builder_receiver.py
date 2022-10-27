from Builder.builder import MargaritaBuilder, CreamyBaconBuilder

class Waiter:
    def __init__(self):
        self.builder = None

    def construct_pizza(self, builder):
        self.builder = builder
        steps = (builder.prepare_dough,
                 builder.add_sauce,
                 builder.add_topping,
                 builder.bake)
        [step() for step in steps]

    @property
    def pizza(self):
        return self.builder.pizza

def validate_style(builders):
    try:
        input_msg = "what pizza would you like? [m] or [c]"
        pizza_stype = input(input_msg)
        builder=builders[pizza_style]()
        valid_input = True
    except KeyError:
        error_msg = 'sorry'
        return (False, None)
    return (True, builder)


def main():
    builders = dict(m = MargaritaBuilder, c=CreamyBaconBuilder)
    valid_input = False
    while not valid_input:
        valid_input, builder = validate_style(builders)
    waiter = Waiter()
    waiter.construct_pizza(builders)
    pizza = waiter.pizza

if __name__ == '__main__':
    main()