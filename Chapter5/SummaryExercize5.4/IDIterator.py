notes = {
    "La": [ 55, 110, 220, 440, 880 ],
    "Si": [ 61, 123, 246, 493, 987 ],
    "Do": [ 65, 131, 262, 523, 1046 ],
    "Re": [ 73, 147, 294, 587, 1175 ],
    "Mi": [ 82, 165, 330, 659, 1319 ],
    "Fa": [ 87, 175, 349, 698, 1397 ],
    "Sol": [ 98, 196, 392, 784, 1568 ]
}

class IDIterator:
    def __init__(self, id = 100000000):
        self._id = id
    
    def new_id(num):
        """
        Multiply the digits of a number by 2 if the index is even and by 1 if the index is odd
        :param num: int (id)
        """
        num_str = str(num)
        result = []

        # enumerate the number to get the index and digit - a tuple of index and digit
        for index, digit in enumerate(num_str):
            # multiply Even dual digit in the number by 2 and each Odd by 1
            if (index + 1) % 2 == 0:
                # if the result is greater than 9, subtract 9 from the result
                if int(digit) * 2 > 9:
                    result.append(int(digit) * 2 - 9)
                else: # else add the result to the list
                    result.append(int(digit) * 2)
            else:
                result.append(int(digit))
        
        return result
    
    def check_id_valid(id_number):
        """
        Check if the id is valid
        :param id_number: int
        """
        # check if the id is valid - the sum of the digits of the new id is divisible by 10
        return sum(IDIterator.new_id(id_number)) % 10 == 0

    def __iter__(self):
        return self
    
    def __next__(self):
        while True:
            # check the current id and increment the id
            if self._id == 999999999:
                raise StopIteration
            if IDIterator.check_id_valid(self._id):
                valid_id = self._id
                self._id += 1
                return valid_id
            self._id += 1
            


def id_generator(id):
    """
    Generate a valid id
    :param id: int
    """
    while True:
        if id == 999999999:
            break
        if IDIterator.check_id_valid(id):
            yield id
        id += 1


def main():
    # input the id and the type of generator or iterator
    id = int(input("Enter the id: "))  # 123456780
    it_or_gen = input("Generator or Iterator? (gen/it)? ").lower()

    # if iterator
    if it_or_gen == 'it':
        id_iter = IDIterator(id)
        for i in range(10):
            print(next(id_iter))
    # if generator
    elif it_or_gen == 'gen':
        id_gen = id_generator(id)
        for i in range(10):
            print(next(id_gen))
    # invalid option
    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
