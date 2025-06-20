# 1. Run len(people)

# 2. No, tuples are immutable.

# 3. Lists are mutable and use [] and tuples are not and use ()
# , and both are sequences and heterogenous

# 4. Strings can be viewed as sequences of individual characters
# because you can index them.

# 5. Sets are unordered, sequences are not.

pi = 3.141592
str_pi = str(pi)

# 7. 0-6
#    1-5
#    3, 7, 11
#    empty list
#    8-4

print(list(range(3, 17, 4)))

# 9. 1- Yes they are
#    2- No, the list constructor for another_list creates a new list
#    3- Yes they are
#    4- Yes, it shallow loads(? loads? I might be forgetting the word)
#       which I believe means it just points at the same place in memory.

# 10. As this is a set, it is hard to guarantee which order they will print

country_names = {
    'Alice': 'Usa',
    'Francois': 'Canada',
    'Inti': 'Peru',
    'Monika': 'Germany',
    'Sanyu': 'Uganda',
    'Yoshitaka': 'Japan',
}

country = country_names['Sanyu']
print(country)