import random
from update_predict import predict, update

def main():

    const = 5

    for i in range(20):
        noise = random.random()
        print(const+noise)



if __name__ == "__main__":
    main()