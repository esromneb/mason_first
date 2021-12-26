isprime = 6011


foundDivisor = False

for test in range(2,isprime):
    whole = isprime // test
    remainder = isprime % test
    print('%s divided by %s is whole: %s and remainder %s' % (isprime, test, whole, remainder))
    if remainder == 0:
        print("Found NOT prime!!!")
        foundDivisor = True
        break

if foundDivisor == False:
    print("%s was PRIME" % isprime)