# beggining-tetris-project

Purpose behind the project

In the past about 7 years ago I decided to create a platformer game in java for a high school project.
And although a general audience would consider it to be impressive, I believe that I can write an application where I could simply do the code better. 
Asides from that I’d rather talk about something that I have done recently.
So, I figured coding Tetris in python was appropriate since I liked the game to start out with and that I can create something where the code is more 
readable.

total hours spent on the project: 18


The basic concept behind the project:
In the grid.py file on line 14 I have what is called my passive grid and in the updating grid.py on line 17 I have what is called my active grid. the passive
grid is responsible for displaying the placed pieces while the active grid is responsible for displaying the falling pieces. Each zero in the arrays represents
an empty space in the grid and if there is a number in it asides from a zero it would represent a cube. The reason to why I did this is because I believed that
it would be fairly simple to simply copy what was on one grid and put in on to another and that there needed to be a distingtion between a falling piece and 
something that wasn't moving. But asides from that, that is essentially the main building block that I have built the application around. 

Running the project in the pycharm IDE

Assuming that whoever opens this has the PyCharm IDE installed. To simply run the project the first thing that needs to be done is to go into 
file>settings>project>python interpreter> then click the plus to add the pygame package. From there it should be as simple as clicking and 
dragging all the files into the project folder and running it from the main.py file(everything you need should be in the day 6 folder)

controls:
arrow keys to move the piece
c and v to rotate your piece
