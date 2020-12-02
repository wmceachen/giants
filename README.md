CS 189 Project S 
Authors:  
William McEachen  
Grace Kull  
Abhinav Gopal  
Shrey Vasavada  
Jai Bansal  

**Project Objective:** Students will understand the industry context that can motivate PCA/CCA/Low Rank Approximations. Students will explore the intricacies of SVD in the context of PCA to better understand the algorithm. Students will also become familiar with data cleaning methodologies, and will be introduced to more formal data processing techniques, including replacing NaNs and one-hot-encoding.

Specifically in the notebook, you will first see how to clean data with missing NaN values. You will also begin to understand how feature selection works, in an intuitive sense. In the case of baseball, some features are naturally more important than others. However, you will explore mathematically (through PCA and CCA) which features are specifically adding some value to the model. Some features are stored as classes, such as the baseball position. You will utilize one-hot-encoding to create indicator variables for these positions, as the position itself certainly affects player salary. Then, you will explore the SVD of the feature matrix $X$, and what happens when singular values are adjusted. The notebook will help you understand why the results of this adjusted SVD are different between PCA and CCA. 

**Navigating the Repository:** There are several important files in the repository. You should first review the slides "CCA_PCA Slides.pdf" and the notes "AWGSJ_notes.pdf" to ensure you have a basic conceptual understanding of the topics to be covered in the main notebook. Don't worry if you are not comfortable with everything; the notebook will certainly help with that. Next, complete the Jupyter Notebook titled "Project_T_final_student_version.ipynb". Once you have completed all code cells to the best of your ability, your next task is to finish the quiz titled "AWGSJ_quiz.ipynb".


Note: Slides and Notes information uses several of the ideas as noted in Notes 10 & 11 of EECS 189, Fall 2020. https://www.eecs189.org/static/notes/n10.pdf, https://www.eecs189.org/static/notes/n11.pdf
