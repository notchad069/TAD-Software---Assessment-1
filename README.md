# TAD - Software tasks
    
    So, this is the documentation for each tasks that you guys asked to do. We'll jump right into 

## Task - 1:
    First off, we were supposed to do a github account and also had to install git locally, which i already did. So, I went straight into coding the games. 

### Git pushing steps:
So, I already started working on a separate folder in my drive for all the programs that I've written or bouta write. In the terminal, I first cd to the path of that folder. After that i use the command:

**git remote add origin**

So what this does is that, it creates a local repo in our computer, that i could access anytime. The next step is to create branches. I dont really want more than one branch, so i just create the main branch using, 

**git branch -M main**

I then add all the files using the command, 

**git add .**

I then make a commit with a pretty good message by using the command

**git commit -m "bigchungus"**

The next is the final step, where i upload the local repo to github using, 

**git push -u origin main**

### Finding the nth fibonacci number
    I used both the iterative and recursive way of finding the nth number. Let's first look at how i did the iterative one.
        
        Iterative method:
        I first created an empty list and hard coded the first two values into it as 0 and 1. Then I iterated the list from index 2 to n. The iterating condition was to get the i-th element, we have to add the (i-1)th value and the (i-2)th value. That's the iterative method and now let's look at the recursive method.
        
        Recursive method:
        Here, you dont need no lists. You give the conditions that the first two elements are 0 and 1 and the rest of the elements are all the sum of (n-1)th and (n-2)th elements. You do all this with just if statements and no loops required.

        Now let's get into coding the little games. I coded all 3 of them.
        
### Hangman
    I started off by importing the library "random". I then uploaded a list with the words that we'd be using to play the game. I wanted to add like a dataset of wordle which is available in a github repo but i thought, it'd be overcomplicating it. So i just went with this small list of words. Then i created another list for the stick figure positions for the actual game. 
    
    I then created a function for the letters' placement if the user guessed the letter correct. Since, the user only gets 6 lives, i went with revealing all the locations of the letter that the user guessed.
    
    The next is the game function where we code the game. First we choose a random word from the list. We also create an empty list so that we could keep track of the letters that the user is guessing. First we print the word with all blank spaces so that the user knows how many letters the word has. Then we use a while loop and we run the loop till the user doesnt have any lives left. We add each letter that the user guesses to that list, if and only if that letter is present in the original word. We then reveal the placement of the letters in the words using the function that we created earlier. 
    
    If the user guessed the placement of all the words correctly, then the user wins.
    
### Rock Paper Scissors

        So, the code for this is pretty straightforward. We create a list that contains the three choices. We then choose a random choice out of those three. And we have a nested if blocks for the conditions under which the user wins. 

### Guess a number
    So, here the task is for the user to guess a number in 5 tries. They'd recieve a message if the number is greater or lesser than their guess and based off of that, the user is supposed to make their guesses. I restricted the range of the function to 1 and 100.
        We use a while loop under the condition that the user has atleast one life left. And then a nested if block that has the conditions where the user wins, or the guessed number is greater or lesser than the actual number.

## Task - 2
Task 2 was writing in markdown, which I'm doing here and in the About Me.md file, where I write about **what makes me - *me*.**

## Task - 3

This completely revolved around learning graphs and graph algorithms. I hadnt learnt graphs till this point, so this task helped a lot. I watched some lectures and also used some books to learn them. I learn all the algorithms but still I feel like I have to give another read for understanding MST(both Krushkal’s and Prim's) in a better way. So, here's how I used all the algorithms that I learned and used them on a graph:

I used this adjacency list for all the algorithms :
>adj_list = {
    0: [(1, 2), (3, 5)],
    1: [(2, 1)],
    3: [(4, 3), (6, 2), (7, 1)],
    4: [(2, 4), (5, 6)],
    5: [(2, 2)]
}

### DFS
- Starts from node 0
- Uses a stack to explore as deep as possible before backtracking.
- Skips already visited nodes.

### BFS 
- Starts from node 0
- Uses a queue to explore neighbors level by level.
- Skips already visited nodes.

### Dijkastra's Algorithm
- Finds shortest paths from node 0 to all other reachable nodes.
- Tracks and updates minimum distances.
- Ignores already visited nodes.

### Kruskal's MST 
- Builds a minimum spanning tree using the union-find (DSU) structure.
- Sorts all edges and adds the smallest ones while avoiding cycles.
- Outputs total weight of MST.

### Prim's MST 
- Greedily selects the minimum weight edge from visited to unvisited nodes.
- Grows the MST starting from node 0.
- Outputs total weight of MST.

## Applications of the graph algorithms
- So, let's get to a situation where a drone is deployed in an unknown environment. The major task there, is to explore the landscape but how does it navigate. First things first, it first maps out the environment using sensors like LIDAR,IMU etc. It now has to pass through the obstacles that are marked in the map and reach the final destination. So, here's where **graph algorithms** come into play. We could use algorithms like, A* or Dijkastra's to find the shortest path to the final destination by avoiding the obstacles.
- Let's imagine another situation where in an environment, more than one drone/VTOL aircraft is deployed. Now all these drones need to operate without colliding with each other. We could use MST to distrubute tasks and communicate efficiently. 
- Another situation where the drone needs to collect data from multiple sensors or relay it to ground stations. Here, graphs help in optimizing data routing paths based on bandwidth, signal strength, or battery limits.
    
            
