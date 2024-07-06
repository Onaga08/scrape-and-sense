# Instructions for running the code.
### Note - Please download the whole folder and then run the file. The code has inbuilt paths specified and thus it is important that they remain in the same place.<br>

### <p> The code is divided into different parts to promote readibility and reduce render time. Abstraction is achieved using [functions.py](functions.py)</p> <br>

# Pre-requisites 

<ul>
<li>Input.xlsx</li>
<li>Install Libraries using requirements.txt</li>
<li>Dict directory with positive/negative .txt files</li>
<li>Stop Words directory with 3 .txt stop words files</li>
<li>Sequence of running .py files</li>
</ul>

## Sequence
<ul>
<li>main.py</li>
<li>check.py</li>
<li>rmv_StopWords.py</li>
<li>Analysis.py</li>
<li>output.py</li>
</ul>

### main.py
<ul>
<li>Input file - Input.xlsx</li>
<li>Working - Creates Input.csv file(Used further by other .py files). Data Extraction + text_files directory created.</li>
</ul>

### check.py
<ul>
<li>Input file - text_file directory</li>
<li>Working - Checks the .txt files created by main.py for articles with less than 3 lines. If so, there must be some error in data extraction.</li>
</ul>

### rmv_StopWords
.py
<ul>
<li>Input file - Stop Words directory + text_file directory.</li>
<li>Workinig - Creates one .txt file with all StopWords. Creates updated_text_files directory with .txt files having removed all the stopwords.</li>
</ul>

### Analysis.py
<ul>
<li><b>Bulky code. Give time to run!</b></li>
<li>Input file - Uses almost all files mentioned above. </li>
<li>Working - works to calculate all the analysis required for the output.csv. Creates an output.csv file.</li>
</ul>

### output.py
<ul>
<li>Final runable file.</li>
<li>Input - Analysis.csv and Input.csv. Output - final_output.csv.</li>
<li>Working - Modifies output to put URL in the .csv file.</li>
</ul>

### functions.py
<ul>
<li><b>VERY IMPORTANT FILE WITH HELPER FUNCTIONS</b></li>
<li>Provides all other .py codes with important functions. Make sure to keep in directory.</li>
</ul>