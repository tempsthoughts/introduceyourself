# This app will ask classmates their name and a few questions about themselves.
# Afterward, the app will share the answers given by the classmates.

# Greeting
print('Welcome back to a new school year! To help you get to know your classmates better, please answer the following questions!')

# Question 1
name = input('What is your name? ')
print(name)

# Question 2
favorite_color = input('What is your favorite color? ')
print(favorite_color)

# Question 3
favorite_food = input('What is your favorite food? ')
print(favorite_food)

# Question 4
favorite_tv_show = input('What is your favorite tv show? ')
print(favorite_tv_show)

# Question 5
favorite_song = input('What is your favorite song? ')
print(favorite_song)

# Question 6
print(f"Everyone, meet {name}! {name}'s favorite color is {favorite_color}. {name}'s favorite food is {favorite_food}. {name}'s favorite tv show is {favorite_tv_show}. {name}'s favorite song is {favorite_song}.")
