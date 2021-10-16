#wieght in Killogramm
#acceleration in Newton

def Newtonslaw(weight, acceleration):
    Force = weight * acceleration
    return Force


if __name__ == "__main__":
    print(Newtonslaw(10, 10))
