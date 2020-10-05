#!/usr/bin/env python
# coding: utf-8

# # Using Python for Research Homework: Week 1
# 
# In this homework, we will use objects, functions, and randomness to find the length of documents, approximate $\pi$, and smooth out random noise.

# ### Exercise 1
# 
# In this five-part exercise, we will count the frequency of each letter in a given string.
# 
# #### Exercise 1a
# 
# - Import the `string` library.
# - Create a variable `alphabet` that consists of the lowercase and uppercase letters in the English alphabet using the `ascii_letters` data attribute of the `string` library.

# In[1]:


# write your code here!
import string
alphabet = string.ascii_letters


# #### Exercise 1b
# - The lower and upper case letters of the English alphabet should stored as the string variable `alphabet`.
# - Consider the sentence 'Jim quickly realized that the beautiful gowns are expensive'. Create a dictionary `count_letters` with keys consisting of each unique letter in the sentence and values consisting of the number of times each letter is used in this sentence. Count upper case and lower case letters separately in the dictionary.

# In[2]:


sentence = 'Jim quickly realized that the beautiful gowns are expensive'

count_letters = {}
# write your code here!
for i in sentence:
    if i in alphabet:
        count_letters[i] = sentence.count(i)
print(count_letters)


# #### Exercise 1c
# - Rewrite your code from 1b to make a function called `counter` that takes a string `input_string` and returns a dictionary of letter counts `count_letters`.
# - Use your function to call `counter(sentence)`.

# In[3]:


# write your code here!
def counter(input_string):
    count_letters = {}
    for letter in input_string:
        if letter in alphabet:
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return count_letters


# #### Exercise 1d
# - Abraham Lincoln was a president during the American Civil War. His famous 1863 Gettysburg Address has been stored as `address`. Use the `counter` function from 1c to return a dictionary consisting of the count of each letter in this address and save it as `address_count`.

# In[4]:


address = """Four score and seven years ago our fathers brought forth on this continent, a new nation, 
conceived in Liberty, and dedicated to the proposition that all men are created equal. Now we are engaged in a 
great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. 
We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final 
resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper 
that we should do this. But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- 
this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add 
or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. 
It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so 
nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored 
dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here 
highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of 
freedom -- and that government of the people, by the people, for the people, shall not perish from the earth."""   

# Write your code here!
address_count = counter(address)
print(address_count)


# #### Exercise 1f
# - The frequency of each letter in the Gettysburg Address is already stored as `address_count`. Use this dictionary to find the most common letter in the Gettysburg address.

# In[7]:


import random
# write your code here!
most_frequent_letter = max(address_count, key=address_count.get)
print(most_frequent_letter)


# ### Exercise 2
# 
# Consider a circle inscribed in a square. The ratio of their areas (the ratio of the area of the circle to the area of the square) is $\frac{\pi}{4}$. In this six-part exercise, we will find a way to approximate this value.
# 
# #### Exercise 2a
# - Using the `math` library, calculate and print the value of $\frac{\pi}{4}$

# In[8]:


# write your code here
import math

pi = math.pi
print(pi/4.0)


# #### Exercise 2b
# - Using `random.uniform()`, create a function `rand()` that generates a single float between $-1$ and $1$.
# - Call `rand()` once. For us to be able to check your solution, we will use `random.seed()` to fix the seed value of the random number generator.

# In[14]:


import random
random.seed(1)
def rand():
    return random.uniform(-1, 1)
rand()


# #### Exercise 2c
# - The distance between two points x and y is the square root of the sum of squared differences along each dimension of x and y. Write a function` distance(x, y)` that takes two vectors as its input and outputs the distance between them. Use your function to find the distance between $x=(0,0)$ and $y=(1,1)$.

# In[15]:


def distance(x, y):
    # define your function here!
    X = (x[0]-y[0])**2
    Y = (x[1]-y[1])**2
    ans = math.sqrt(X + Y)
    return ans
   
x = (0, 0)
y = (1, 1)

print(distance(x, y))


# #### Exercise 2d
# 
# - Write a function `in_circle(x, origin)` that determines whether a point in a two dimensional plane falls within a unit circle surrounding a given origin.
#     - Your function should return a boolean `True` if the distance between `x` and `origin` is less than 1 and `False` otherwise.
#     - Use `distance(x, y)` as defined in 2c.
# - Use your function to determine whether the point (1,1) lies within the unit circle centered at (0,0).

# In[16]:


def in_circle(x, origin = [0,0]):
   # Define your function here!
    if len(x) != 2:
        return "x is not two-dimensional!"
    elif distance(x, origin) < 1:
        return True
    else:
        return False

print(in_circle((1,1)))


# #### Exercise 2e
# 
# - Create a list `inside` of `R=10000` booleans that determines whether or not a point falls within the unit circle centered at `(0,0)`. 
#     - Use the `rand` function from 2b to generate `R` randomly located points.
#     - Use the function `in_circle` to test whether or not a given pint falls within the unit circle.
# - Find the proportion of points that fall within the circle by summing all `True` values in the `inside` list; then divide the answer by `R` to obtain a proportion.
# - Print your answer. This proportion is an estimate of the ratio of the two areas!

# In[17]:


random.seed(1) 

# write your code here!
R = 10000
x = []
inside = []
for i in range(R):
    point = [rand(), rand()]
    x.append(point)
    # Enter your code here! #
    #print(x)
    inside.append(in_circle(x[i], origin = [0]*2))

print(sum(inside)/R)


# #### Exercise 2f
# 
# - Find the difference between your estimate from part 2e and `math.pi / 4`. Note: `inside` and `R` are defined as in Exercise 2e.

# In[18]:


# write your code here!
print(math.pi/4 - sum(inside)/R)


# ### Exercise 3
# 
# A list of numbers representing measurements obtained from a system of interest can often be noisy. One way to deal with noise to smoothen the values by replacing each value with the average of the value and the values of its neighbors.
# 
# #### Exercise 3a
# 
# - Write a function `moving_window_average(x, n_neighbors)` that takes a list `x` and the number of neighbors `n_neighbors` on either side of a given member of the list to consider.
# - For each value in `x`, `moving_window_average(x, n_neighbors)` computes the average of the value and the values of its neighbors.
# - `moving_window_average` should return a list of averaged values that is the same length as the original list.
# - If there are not enough neighbors (for cases near the edge), substitute the original value for a neighbor for each missing neighbor.
# - Use your function to find the moving window sum of `x=[0,10,5,3,1,5]` and `n_neighbors=1`.

# In[19]:


def moving_window_average(x, n_neighbors=1):
    n = len(x)
    width = n_neighbors*2 + 1
    x = [x[0]]*n_neighbors + x + [x[-1]]*n_neighbors
    # To complete the function,
    # return a list of the mean of values from i to i+width for all values i from 0 to n-1.
    ans = []
    for i in range(n):
        ans.append(sum(x[i:i+width])/width)
    return ans

x = [0,10,5,3,1,5]
print(moving_window_average(x, 1))


# #### Exercise 3b
# - Compute and store `R=1000` random values from 0-1 as `x`.
# - Compute the moving window average for `x` for values of `n_neighbors` ranging from 1 to 9 inclusive.
# - Store `x` as well as each of these averages as consecutive lists in a list called `Y`

# In[20]:


random.seed(1) # This line fixes the value called by your function,
               # and is used for answer-checking.
    
# write your code here!
R = 1000
x = []
for i in range(R):
    num = random.uniform(0,1)
    x.append(num)

Y = []

Y.append(x)

for i in range(1,10):
    mov_avg = moving_window_average(x, n_neighbors=i)
    Y.append(mov_avg)


# In[21]:


print(moving_window_average(x, 5))


# #### Exercise 3c
# 
# - For each list in `Y`, calculate and store the range (the maximum minus the minimum) in a new list ranges.
# - Print your answer. As the window width increases, does the range of each list increase or decrease? Why do you think that is?

# In[22]:


# write your code here!
ranges = []
for i in range(len(Y)):
    x = max(Y[i]) - min(Y[i])
    ranges.append(x)


# In[23]:


print(ranges)


# In[ ]:




