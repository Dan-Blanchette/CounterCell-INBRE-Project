# CounterCell-INBRE-Project
My cell counter program from the INBRE 2022 internship I took part in as an undergrad fellow.


# Abstract:
Microglia research of the central nervous system (CNS) is a rapidly growing field in biology. 
Dr. Diana Mitchell’s2 research investigates wild-type retinal microglia in zebrafish and a mutation that triggers the regeneration of retinal neurons. 
Further research on this mutation may lead to medical treatments that repair the damaged retinas of patients. 
Cell data is recorded as a digital video file at 20x magnification using a spinning disk confocal microscope. 
A 488nm laser illuminates green fluorescent proteins (GFPs) within the microglia while an optimized filter set detects GFP emissions. 
This type of imaging allows researchers to observe cell behavior. Using Python, the Long3 computer science lab aids researchers by automating image analysis. 
The software stores the data as image files by extracting half-second frames from the zebrafish video file while reporting the frames-per-second (FPS). 
Through user input, a second routine identifies the microglia cell’s red, green, and blue (RGB) pixel values and then isolates them. 
After its runtime, the software records cell count and applies a color fill filter to each cell. 
Additional work includes computational metrics such as microglia cell tracking, cell speed, and total distance traveled in the future.

# Background:
#### 1.) Pixels in an image are comprised of red, green, and blue channels. Each channel has an assigned numeric range between 0 and 255 bits (0 = black, 255 = brightest pigment for the color channel). 
#### 2.) Color compositions are represented in a computer system as a tuple in the following notation: (R,G,B).
#### 3.) Bit Masking is the method of isolating specific color value combinations (objects of interest) from the rest of a digital image.
#### 4.) The connective analysis algorithm allows the software to separate identified objects or combine them based on adjacency or diagonality. This is commonly referred to as one jump and two jump connectivity.
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/tempsnip.png)

# Materials:
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Spyder%60.png)
### Spyder IDE (https://www.spyder.org/)

# Cell counter program technical specifications: 
### Hard disk space (programs and Spyder IDE): 659.1 MB  
### Memory: 8GB, DDR4 SDRAM (recommended) 
### Compatible GPU used for project:  NVIDIA GeForce RTX 2060 6GB RAM

# Project Questions
####      1. How many cells are in each image?
####      2. What is the distance each cell has travelled from image to image and in total based on the data?
####      3. What is the velocity of each cell?
####      4. What user interface design would be the most effective to display the aforementioned information for a researcher?
      
# Project Goals:
- [x] Create a program to extract frames from a video file.
- [x] Conduct analysis and object recognition for each image by identifying the microglia cells.
- [x] Display cell count and image file name.
- [ ] Create a calibration routine to allow for user thresholding. (In Progress)
- [ ] Display approximate cell size (by pixel count) then find the center of each cell.
- [ ] Determine distance traveled by tracing the cell's path.
- [ ] Create a program that diplays data via a user interface.

# Visualized Project Task List:

![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Project%20Planning.jpeg?raw=true)

# Objective 1: Create a program to extract frames from a video file

The program videoToFrames.py asks the user to provide the directory path to their file through the terminal command prompt. It then asks the user to specify a destination for the extracted files. There is error checking for both the file type and the directory to prevent potential overwriting of the data. 
The program then breaks the video into .jpg images and stores them in the specified directory. 
**(See Figure 1: Visualized Frame Extraction Program below)**


# Figure 1: Visualized Frame Extraction Program
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Video%20To%20Image%20Software%20Inbre2022.jpeg?raw=true)
