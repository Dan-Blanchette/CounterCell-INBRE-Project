# Project_CounterCell-INBRE
This README is intended to provide a project overview and background information about the development of this software.


# Abstract:
Microglia research of the central nervous system (CNS) is a rapidly growing field in biology. 
Dr. Diana Mitchell’s research investigates wild-type retinal microglia in zebrafish and a mutation that triggers the regeneration of retinal neurons. 
Further research on this mutation may lead to medical treatments that repair the damaged retinas of patients. 
Cell data is recorded as a digital video file at 20x magnification using a spinning disk confocal microscope. 
A 488nm laser illuminates green fluorescent proteins (GFPs) within the microglia while an optimized filter set detects GFP emissions. 
This type of imaging allows researchers to observe cell behavior. Using Python, the Long computer science lab aids researchers by automating image analysis. 
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
### Compatible GPU used for project:  NVIDIA GeForce RTX 2060 6GB RAM (equivilent or greater specs)

# Project Dependencies and Libraries documentation
### 1.) Scikit-image [skiamge documenatation](https://scikit-image.org/docs/stable/).
### 2.) Numpy [Numpy documenatation](https://numpy.org/doc/stable/)
### 3.) Matplotlib [Matplotlib user's guide](https://matplotlib.org/stable/users/index)
### 4.) Plotly [Plotly Python information](https://plotly.com/python/)
### 5.) Anaconda [Anaconda Webpage](https://www.anaconda.com/products/distribution)
### 6.) Jupyter Notebook [Jupyter Notebook Documentation](https://docs.jupyter.org/en/latest/)

