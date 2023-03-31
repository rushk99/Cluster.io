# NanomechanicalMappingBackend

## Overview:
This project focused on making a backend for a web app which will allow for clustering of nanomechanical mapping data.
This project is created and worked on by Christopher Vieira and Eric Schimd

UPDATE ALL SECTIONS BELOW 

## Functionality:
This section highlights the functionality that exists within the helper classes and some of the end products, such as
the Jupyter Notebooks.

### Helper Classes
This section discusses the helper classes inside of the project. It goes into detail for what they are, what they are
used for, and which ones are currently in use within the project.

To start off, a helper class in this project was a class that was used in one of two ways. Firstly, it was used to 
store functions, such as EquationsLibrary.py, in order to simplify any and all scripts written that use those
equations. Another helper class type that was used was done in a more object oriented approach, creating objects that
represent certain bits of functionality. One example of this is the DataProcessingHelper.py class. This class is 
responsible for reading any and all data the program uses and then possibly processing it to follow Hertz's theory.
This was made into an object due to the DataProcessingHelper object you declare also storing all of the information
you read. For example, at any point during the program's execution, if you have read data then you can access the
orig_load_col property of the DataProcessingHelper in order to get the original load column.

After this section all currently implemented helper classes will be listed off along with why they are important or how
they are used.

#### BinHelper.py
This class will generate the probability density function values from the min value to max value. It counts all data
between the min and max values in input data, having bins of bin_increment size. It is also able to plot the data.

#### ContourPlotHelper.py
The purpose of this class is to provide helper methods that involve making plots that are involved in the process
of plotting contour plots for hardness or modulus values. This involving directly plotting the contour plots or
plotting bar graphs involving other data.

#### DeconHelper.py
The purpose of this class is to assist in running the deconvolution method obtained through a MatLab project

#### DeconPhaseHelper.py
The purpose of this class is to show off the functionality associated with reading data from an excel document,
putting it in a contour plot, running the deconvolution method, and then plotting the resulting data in another
contour plot.

#### ExcelFileReaderHelper.py
This class is responsible for reading from excel files, especially when it needs to read from multiple sheets.
This structure allows it to only bring the excel file into memory once, saving run time.

#### KMeansHelper.py
The purpose of this class is to show off the functionality associated with reading data from an excel document,
putting it in a contour plot, running the k means clustering method, and then plotting the resulting data in
another contour plot.

#### MaxAreaRectangle.py
The purpose of this class it to find the maximum rectangular area in a series of bars from a histogram. Used for
finding the largest square of non null data in a grid.

#### PDFHelper.py
This class will find the pdf values associated with the input data set using the BinHelper object. This object will
also automatically get the bin increment value over time. If the percentage is to large in one bin, it reduces
bin size. If it is too small in the largest bin, then it increases bin size. Does this process until it gets
an acceptable value as the max of all pdf bins. It also is responsible for plotting the data.

#### RemoveOutliers.py
A class used to help remove the outliers inside of the data_df DataFrame and corrects them according to the data 
around them in their grid.

#### SimpleAgglomerativeHelper.py
Simpler method of doing agglomerative clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleBirchHelper.py
Simpler method of doing birch clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleDBSCANHelper.py
Simpler method of doing DBSCAN clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleDeconHelper.py
Simpler method of doing Decon clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleKMeansHelper.py
Simple method of doing KMeans clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleKMedoidsHelper.py
Simple method of doing KMedoids clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleOPTICSHelper.py
Simple method of doing OPTICS clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

#### SimpleSpectralHelper.py
Simple method of doing Spectral clustering. Involves a single function that can be called to complete all of the
clustering process. Has an option of whether to remove outliers or not. Very modular.

### Jupyter Notebooks
This section covers the Jupyter Notebooks that currently exists and gives a brief description of what each one of them
is responsible for doing.

#### 9-29_DataAnalysis_01NOV2019_600degF-5min-Austempering_BCS-1444
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_04SEP2019_600F-30min_BCS-RCS-1301
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_05SEP2019_600F-02min_BCS-1152
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_06NOV2019_Austemper-600defF-5min_BCS-1027
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_15JAN2020_Aust30Min_BCS
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_15JAN2020_Aust5min_BCS
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### 9-29_DataAnalysis_Jan 5-min - DO NOT USE
Below is one of the data analysis segments asked for on 9/29 for a talk on Wednesday.

#### AgglomerativeClusteringNotebook
A notebook that shows off the AgglomerativeClustering library. Its functionality is gathered from 
AgglomerativeClusteringTester.py and is used to show off the four methods of clustering associated with the library 
on some hardness data.

#### BinHelperNotebook
This notebook focuses on showing off the functionality that currently exists in the BinHelper.py class. It takes code 
from BinHelperTester.py

#### BirchNotebook
Notebook that shows off clustering functionality from Birch library. Functionality gathered from BirchTester.py.

#### DBSCANNotebook
Notebook that shows off functionality from DBSCAN library. Originally made in DBSCANTester.py. 

#### DeconPhaseHelperNotebook
This notebook shows off the functionality associated with the DeconPhaseHelper.py class as shown in the 
DeconPhaseHelperTester.py script. This notebook highlights how it is able to analyze different properties, 
either one at a time or both at one.

#### DeconvolutionAlgorithmV1Notebook
The section below shows off the current algorithm representing the deconvoluion algorithm. It is a little 
difficult to understand, some elements still remain uncommented and due to the structure of the algorithm it 
needs to be in one large block. I will comment everything I can though there is a large portion that remains 
unknown for exactly what it is and what it does.

#### DeconvolutionAlgorithmV2Notebook
This notebook shows off the functionality of the DeconHelper.py class as shown in the DeconHelperTester.py script. 
It is an updated version of the deconvolution method.

#### ExcelReadingNotebook
This notebook shows off functionality associated with reading from an excel file and then performing pdf analysis on 
it. This is taken from ExcelDataTesting.py, at the time of this notebook's creation it was in testing folder.

#### KMeansHelperNotebook
This notebook shows off the functionality associated with the KMeansHelper.py class as shown in the 
KMeansHelperTester.py script. This notebook highlights how it is able to analyze different properties, 
either one at a time or both at one.

#### KMedoidsNotebook
Notebook focuses on showing off K Medoids clustering method. Functionality taken from KMedoidsTester2.py.

#### OPTICSNotebook
Notebook focusing on showing off clustering from OPTICS library. Made originally in OPTICSTester.py

#### OutlierRemovalAgglomerativeNotebook
This notebook focuses on showing off the agglomerative notebook clustering with and without outlier removal on the 
hardness data from one of the original excel files. The first example is without outlier removal, the second 
has outlier removal.Taken from OutlierRemovalAgglomerative.py.

#### OutlierRemovalBirchNotebook
This notebook focuses on showing off the birch clustering method on data with outliers and data without outliers. 
Copied over from OutlierRemovalBirch.py. The first section has outliers, the second does not have outliers.

#### OutlierRemovalDBSCANNotebook
This notebook focuses on running the DBSCAN clustering method with and without outlier removal. This is taken from 
OutlierRemovalDBSCAN.py. It first runs the clustering process with outliers and then runs it again without outliers.

#### OutlierRemovalDeconNotebook
This notebook focuses on running the deconvolution method on a dataset with outliers and then again without outliers. 
Functionality taken from OutlierRemovalDecon.py.

#### OutlierRemovalKMeansNotebook
This notebook focuses on showing off the K Means clustering method on our hardness data set with and without outliers. 
The first run through has outliers, the second does not. Functionality taken from OutlierRemovalKMeans.py.

#### OutlierRemovalKMedoidsNotebook
This notebook focuses on running the K Medoids clustering method on the hardness data with and without outliers 
in that order. Functionality taken from OutliersRemovalKMedoids.py.

#### OutlierRemovalOPTICSNotebook
This notebook shows off the OPTICS clustering method on hardness data with and without outliers. The first fun 
has outliers, the second does not. Functionality taken from OutlierRemovalOPTICS.py.

#### OutlierRemovalSpectralNotebook
This notebook focuses on showing off the spectral clustering method on hardness data with outliers and then without 
outliers in that order. Functionality taken from OutlierRemovalSpectral.py.

#### PDFHelperNotebook
This notebook focuses on generating the pdf values of input data using a helper class. This helper class has automated 
finding the process of getting the size of bins for fair distributions.
The first test is also done using 100k samples, esentially just showing it off in a sort of stress test, to which it 
performs fairly well in.
Content is gathered from PDFHelperTester.py.

#### RemoveOutliersNotebook
This notebook focuses on showing off functionality from the RemoveOutliers.py helper class. This functionality is 
taken from RemoveOutliersTester.py and RemoveOutliersTester2.py. This focuses on removing outliers from a dataset 
and replacing them based on the scipy interpolate.grid library.

#### SimpleAgglomerativeNotebook
Notebook showing off functionality of SimpleAgglomerativeHelper.py and SimpleAgglomerativeTester.py. 
Shows a simplified way to call agglomerative clustering.

#### SimpleBirchNotebook
Notebook that shows off functionality from SimpleBirchHelper.py and SimpleBirchTester.py. 
Shows a simplified way of calling the birch clustering method on some data.

#### SimpleDBSCANNotebook
Notebook that shows off functionality from SimpleBirchHelper.py and SimpleBirchTester.py. Shows a simplified way of 
calling the birch clustering method on some data.

#### SimpleDeconNotebook
Notebook that shows off SimpleDeconHelper.py and SimpleDeconTester.py. Shows off a 
simpler way of using the decon clustering method on data.

#### SimpleKMeansNotebook
Shows off functionality from SimpleKMeansHelper.py and SimpleKMeansTester.py. A simpler way to use K Means 
clustering on data.

#### SimpleKMedoidsNotebook
Shows off functionality from SimpleKMedoidsHelper.py and SimpleKMedoidsTester.py. A simpler way to use 
KMedoids clustering.

#### SimpleOPTICSNotebook
Shows off functionality from SimpleOPTICSHelper.py and SimpleOPTICSTester.py. 
A simpler way to use the OPTICS clustering method.

#### SimpleSpectralNotebook
Shows off functionality from SimpleSpectralHelper.py and SimpleSpectralTester.py. A simpler way to use spectral 
clustering.

#### SpectralClusteringNotebook
Notebook that shows off functionality gathered from SpectralClustering library. Originally from 
SpectralClusteringTester.py.

### Plugins / Additional Features
This section discusses the plugins and additional features the project contains.

One feature of the project is the use of auto documentation generation tools. This project uses Sphinx for this.
Sphinx runs its auto doc software on all of the helper classes within the project. This allows us to generate HTML
pages based off of the comments inside of the project. The root page used for this is identified as index.html located
at docs/build/html/index.html. If you would like to learn how Sphinx was used for this project and how to update the 
documentation yourself then please read over HowToRunSphinx.txt located in the dev_notes folder.

## Workflow
This section briefly covers the general workflow of the project and how tasks are managed and organized.

When a new bit of functionality is being worked on it will typically placed within the testing folder in the project's 
root directory. This is where all WIP scripts start off for the most part. They are then developed until they are
functional and ready to be moved onto the next step.

Once these scripts are ready to be transitioned to another area, they are put into one of two formats. The first 
end product involves putting the script, as is, into a Jupyter Notebook. This allows the functionality to be displayed
and very well documented. For the most part, the script is broken up into sections, with each section being placed into
a separate code block. This ensures each section can be commented on and accurately described. The second possible end
result of functionality created within the testing folder is to have it be placed in a helper class. Helper classes are
classes that are meant to store more complex and tedious functionality to allow the end user to more easily use and
understand the project. For example, a helper class is used to store all of the equations needed to calculate the 
stress and strain values. Another helper class then uses this equations helper class in order to iterate over all of
the load, displacement, and stiffness values in order to calculate the stress and strain values. This stress strain
helper class also stores all stress and strain values within it, allowing for them to easily be accessed, plotted, and 
manipulated.

Once the functionality from the testing class is finished it will then be placed within the old folder within the root 
directory of the project. Whatever file being moved into the old folder should maintain the same relative path to the 
old folder as it previously did to the root directory of the project. For example, if a file was located in the testing
folder in the root directory of the project, it should be placed in the old/testing folder. Files located within this 
folder may or may not work due to some of them going back to the creation of the project os be warned. All of these
files have been archives in this way in order to allow them to easily be found should they ever need to be looked back
upon. They will likely not be included with the final version of the tool.

## Using Custom Data Files?
In the event you wish to use your own data files compared to the data files in the project then please read this 
section. In order to use your data file you need to place it inside the data folder inside the project directory.
This data folder will be one level inside of the project. Once this is done look for where the file is being read
by the tool. Jupyter notebooks often show where this is being done by having a variable called file_path,
file_name, file_buffer, and so on. You will want to set this variable equal to the relative path to your data
file. If it is from a jupyter notebook in the project you will want it to be "../data/NameOfYouFile.extension".
After this you may need to fill in other information such as the format of excel files you are reading. If the
format is not included then there are options to manually put in the names of each column and other details.
