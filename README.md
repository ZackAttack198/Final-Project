# Night Drive


## Demo Video
Video: https://youtu.be/UC-0fvX7BgQ


## GitHub Repository
Repository: https://github.com/ZackAttack198/Final-Project


## Description
"Night Drive" is a digital screensaver depicting a futuristic car driving past a bustling city at night. It features an infinitely scrolling road and skyline, as well as rapidly twinkling stars. The user can also interact with the program. By left mouse-clicking, they can spawn a firework burst animation of random particle sizes, lifetimes, and colors. They can perform this action as many times as they want, with no cooldown in between clicks. What's more is that the positions of the stars are randomized every time the program is run.

The source folder only contains a few files, as most of the artistry is done within the program itself. The program makes use of the PyGame, Random, and Math libraries. PyGame is used to draw the road, skyline, stars, and firework particles, as well as what makes the road/skyline scroll. Meanwhile, the stars twinkling and firework burst animation are primarily done through Math and Random. The only part of the program that was done externally is the flying car sprite, which was drawn by me in a pixel art app and blitted onto the screen via PyGame.

While making this project, I wanted to create something that was "simple but effective". Originally, I was just gonna draw every single sprite I needed in a pixel art app and make use of the Image library to infinitely loop those images, but that would've meant the program was basically ONLY doing that action. So, I decided to do most of the imagery programatically instead, making use of PyGame's drawing features to create an infinitely looping road with dashes, an infinitely looping skyline with windows, a collection of stars that rapidly twinkle out-of-sync with each other, and a randomly-colored firework burst that spawns every time the user left-clicks. It took me quite a bit of trial and error to figure out how to properly do each element, especially the skyline and firework animation.

If I was to make improvements on this project in the future, I would want to slightly change the skyline by adding little details such as poles or blinking lights to the tops of the buildings, and I would want to give the user the option to control the car's horizontal placement via the left and right arrow keys.
