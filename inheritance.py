import random
import sys

# Each person has two parents and two alleles
class Person:
    def __init__(self):
        self.parents = [None, None]
        self.alleles = ['', '']

def main():
     # Get the number of generations from the command line
    if len(sys.argv) != 2:
        print("Usage: python script.py <number_of_generations>")
        sys.exit(1)

    try:
        generations = int(sys.argv[1])
    except ValueError:
        print("Please enter a valid integer for the number of generations.")
        sys.exit(1)

    # Seed random number generator
    random.seed()

    # Create a new family with the specified number of generations
    p = create_family(generations)

    # Print family tree of blood types
    print_family(p, 0)
    
    
def create_family(generations):
    # Create a new person
    p = Person()

    # If there are still generations left to create
    if generations > 1:
        # Create two new parents for the current person by recursively calling create_family
        parent0 = create_family(generations - 1)
        parent1 = create_family(generations - 1)

        # Assign references to the parent objects to the child's 'parents' attribute
        p.parents[0] = parent0
        p.parents[1] = parent1

        # Randomly assign current person's alleles based on the alleles of their parents
        p.alleles[0] = random.choice(p.parents[0].alleles)
        p.alleles[1] = random.choice(p.parents[1].alleles)

    # If there are no generations left to create
    else:
        # Set 'parents' attribute to None since there are no parents
        p.parents[0] = None
        p.parents[1] = None

        # Randomly assign alleles
        p.alleles[0] = random_allele()
        p.alleles[1] = random_allele()

    # Return the newly created person
    return p


def print_family(p, generation):
    # Handle base case
    if p is None:
        return

    # Print indentation
    print(" " * (generation * 4), end='')

    # Print person
    if generation == 0:
        print(f"Child (Generation {generation}): blood type {p.alleles[0]}{p.alleles[1]}")
    elif generation == 1:
        print(f"Parent (Generation {generation}): blood type {p.alleles[0]}{p.alleles[1]}")
    else:
        print(f"{'Great-' * (generation - 2)}Grandparent (Generation {generation}): blood type {p.alleles[0]}{p.alleles[1]}")

    # Print parents of the current generation
    print_family(p.parents[0], generation + 1)
    print_family(p.parents[1], generation + 1)


# Randomly chooses a blood type allele
def random_allele():
    r = random.randint(0, 2)
    if r == 0:
        return 'A'
    elif r == 1:
        return 'B'
    else:
        return 'O'


if __name__ == "__main__":
    main()
   
