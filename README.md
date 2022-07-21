# CounterCell
# INBRE-Internship-2022

# Project Abstract:

Microglia research of the central nervous system (CNS) is a rapidly growing field in biology. Dr. Diana Mitchell’s2 research investigates wild-type retinal microglia in zebrafish and a mutation that triggers the regeneration of retinal neurons. Further research on this mutation may lead to medical treatments that repair the damaged retinas of patients. Cell data is recorded as a digital video file at 20x magnification using a spinning disk confocal microscope. A 488nm laser illuminates green fluorescent proteins (GFPs) within the microglia while an optimized filter set detects GFP emissions. This type of imaging allows researchers to observe cell behavior. Using Python, the Long3 computer science lab aids researchers by automating image analysis. The software stores the data as image files by extracting half-second frames from the zebrafish video file while reporting the frames-per-second (FPS). Through user input, a second routine identifies the microglia cell’s red, green, and blue (RGB) pixel values and then isolates them. After its runtime, the software records cell count and applies a color fill filter to each cell. Additional work includes computational metrics such as microglia cell tracking, cell speed, and total distance traveled in the future.

# Project Background:
## 1. Pixels in an image are comprised of red, green, and blue channels. Each channel has an assigned numeric range between 0 and 255 bits (0 = black, 255 = brightest pigment for the color channel). 
## 2. Color compositions are represented in a computer system as a tuple in the following notation: (R,G,B).
## 3. Bit Masking is the method of isolating specific color value combinations (objects of interest) from the rest of a digital image.
## 4. The connective analysis algorithm allows the software to separate identified objects or combine them based on adjacency or diagonality. This is commonly referred to as one jump and two jump connectivity.



![image](https://user-images.githubusercontent.com/57776752/180286751-8418b961-7ea1-403f-88e3-f81d5a01a89f.png)



# Image Processing Pipeline Research:  Lewis and Clark State College 
## **Pofessional Investigator: Dr. Seth Long** 
## **INBRE Fellow: Dan Blanchette**

# Project Overview:
Dr. Seth Long's goal is to help automate the collection of microglia cell data from Dr. Mtichell's zebrafish video files. 
Dr. Long specializes in image analysis and automation processes. The expectation is to create user-friendly software 
that helps analyze large quantities of data. This summer, I am tasked with creating a method to extract frames (still images) from 
the provided video files. After that program is working, I will program additional methods that address the following questions:   

# Project Questions
####      1. How many cells are in each image?
####      2. What is the distance each cell has travelled from image to image and in total based on the data?
####      3. What is the velocity of each cell?
####      4. What user interface design would be the most effective to display the aforementioned information for a researcher?
      
# Project Goals:
- [x] Create a program to extract frames from a video file (Prototyping Python).
- [ ] Translate the extraction program to run as a Rust program for efficiency and reduced memory overhead.(Rust)
- [ ] Conduct analysis and object recognition for each image by identifying the microglia cells.(Python)
- [ ] Display count, size, and find the center of each cell.(Python)
- [ ] Determine distance traveled by tracing the cell's path.(Python)
- [ ] Create a program that diplays data via a user interface.(Python)

# Visualized Project Task List:

![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Project%20Planning.jpeg?raw=true)

# Objective 1: Create a program to extract frames from a video file

The program videoToFrames.py asks the user to provide the directory path to their file through the terminal command prompt. It then asks the user to specify a destination for the extracted files. There is error checking for both the file type and the directory to prevent potential overwriting of the data. 
The program then breaks the video into .jpg images and stores them in the specified directory. 
**(See Figure 1: Visualized Frame Extraction Program below)**


# Figure 1: Visualized Frame Extraction Program
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Video%20To%20Image%20Software%20Inbre2022.jpeg?raw=true)

# Figure 2: Pixel Count Example
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Figure%202022-06-06%20134847%20(0).png?raw=true)

# Figure 3: RGB Range Isolation Example
## Original Image
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/rangeImg_1.png?raw=true)
## Microglia Cell Image Sample Capture Using Image Masking
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/mgSample_1.png?raw=true)
## RGB Histogram Report of Microglia Pixel Composition
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/sample1histo.png?raw=true)
## Pixel Neighborhoods: Image Object Recognition
![image](https://github.com/Dan-Blanchette/INBRE-Internship-2022/blob/main/rdMeImg/Screenshot%20from%202022-06-14%2013-53-11.png?raw=true)

