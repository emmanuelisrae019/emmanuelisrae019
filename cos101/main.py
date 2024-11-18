def calculate_velocity():
    distance = float(input('enter distance'))
    time = float(input('enter time'))
    velocity = distance / time

    def calculate_density():
        mass = float(input('enter mass'))
        volume = float(input('enter volume'))
        density = mass/volume
        print(density)

    def calculate_upthrust():
        density = float(input('enter density'))
        volume = float(input('enter volume'))
        upthrust = density*volume
        print(upthrust)

    def calculate_force():
            mass = float(input('enter mass'))
            acceleration = float(input('enter acceleration'))
            force= mass * acceleration
            print(force)

    def calculate_impulse():
                force = float(input('enter force'))
                time  = float(input('enter time'))
                impulse = force*time
                print(impulse)

    def calculate_momentum():
        mass = float(input('enter mass'))
        velocity = float(input('enter velocity'))
        momentum =mass*velocity
        print(momentum)

        start=int(input('Type 1 for density\n Type 2 for upthrust\n Type 3 for force\n Type 4 for impulse\n Type 5 for momentum '))

        if start == 1:
            calculate_density()
        elif start== 2:
            calculate_upthrust()
        elif start==3:
            calculate_force()
        elif start==4:
            calculate_impulse()
        elif start==5:
            calculate_momentum()
        else:
            print('Invalid entry ,Try again.')







