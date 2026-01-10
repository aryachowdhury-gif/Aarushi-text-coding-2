class pair_elements:
    def twoSum(self, num, target):
        #create an empty dictionary
        lookup = {}

        #iterate through the tuple
        for i, j in enumerate(num):
            if target - j in lookup:
                return (lookup[target - j], i)
            lookup[j] = i

#take input of dum from the user
value = int(input("Enter sum for which you want to make this search: "))

print(f"index1=%d, index2=%d" % pair_elements().twoSum((10, 20, 30, 40, 50, 60, 70),value))