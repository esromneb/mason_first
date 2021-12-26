mason_born = 2011
mason_age = 10
mason_start = 0
message = 'In year %s mason was %s years old'
for x in range(0,mason_age+1):
    print(message % (mason_born, mason_start))
    mason_born = mason_born + 1
    mason_start = mason_start + 1