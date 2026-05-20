from addition import addition

# or
 
# import addition
# print(addition.addition(10, 12))


rad = random.randrange(start=0, stop=25)
area = round(math.pi * rad ** 2, 2)
print(f"This circle has the area: {area} with the radius of {rad}")

if __name__ == "__main__":
    print("Testing")
    print(addition(10, 12))