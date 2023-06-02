# REX_2022
TODO (updated on Jun 2, 2023):
- Start Jounal draft ASAP (A & A)
- Literature Review (backgrounds), inculding methods for 1) online medical assistance 2) ML methods for similar application 3) Mentor Disorder (A & A)
- Explain how the data will be analyzed and interpreted, such as Hume AI, LATER (A & A)
- Further identify gaps in the literature that the proposed research will address
- Paper format (template + example papers), graphs (what kind of data for ML, what kind of graphs), citation (A & A): https://www.nature.com/npjdigitalmed/for-authors-and-referees?gclid=Cj0KCQjw6cKiBhD5ARIsAKXUdyawQcM_TnONnmqWpV9OwU7Q7Y8wroWkJb7MNDCPnCyHehEHh64x_48aAsLcEALw_wcB
- https://www.nature.com/npjdigitalmed/for-authors-and-referees/submission-guidelines#format-manuscripts
- ----------------------------------------------------------------------------------------------------
- Investigate other machine learning algorithms (supervised learning) to improve the current ML model based on Deepface (DONE Paul & Chris) 
- ML implementation (DONE Paul & Chris)
----------------------------------------------------------------------------------------------------
- Data collection: 1) Beijing Hosipital (Lyka) 2) Open-source (Chris), record the source
- ----------------------------------------------------------------------------------------------------
- Not important for now:
- Target journal: ***** Nature Digital Medicine *****
 3) Ask Michael (Paul) 4) Baidu, use current patient picture to search more patient data from baidu search -> hide raw patient data, but we could release processed 3D meshed data
- CHECK IF POSSIBLE: Identify the population (color skins, countries) and sample for the study (A & A) -> For now, Asians
- Improve the patent’s consent form to avoid unnecessary trouble in the future (Lyka)
- Data and graphs will be filtered and interpreted using Python Panda Dataframe & Excel (Chris)



----------------------------------------------------------------------------------------------------------


NEXT (updated on May 1, 2023):
- Reading & Literature Review:
- Based on the existing current literature reviews, further investigate and summarize previous research related to the topic, especially for the methodology part.
- Further identify gaps in the literature that the proposed research will address

Methodology:
- Research design: Investigate other machine learning algorithms (supervised learning) to improve the current ML model.
- Data collection methods: Active collaboration with Beijing Tiantan Hospital to collect patent data. Further improve the patent’s consent form to avoid unnecessary trouble in the future. Open-source database for training and testing data sets.
- Identify the population and sample for the study: Will try to increase the current population sample size.
- Explain how the data will be analyzed and interpreted.
- Data and graphs will be filtered and interpreted using Python Panda Dataframe & Excel.

Expected Outcomes (end of July, 2023):
- Investigate and implement other machine learning algorithms that can improve the model’s accuracy with a balance of performance and speed.
- Ideally, increase the research sample size from ~650 to ~2000 by building more collaborations with the Beijing Tiantan Hospital and an open-source database
- Finish the journal paper with good quality and submit it to journals such as Nature Digital Medicine. 

----------------------------------------------------------------------------------------------------------

Done:
- Focus on method
- My friend, Lyka Wang, the person who does the ML part is now in this github repo
- Revise and improve the details of the abstract (A & A done)
- Try to write up the template for the remaining paragraphs in the paper such as methodology, can leave the data empty for now (A & A done)
- Write workflow (Z & P done)
- Data Collection for both normal and abnormal ppl (Z & P done)
- Deepface speed optimization (Z & P done)
- pandas dataframe for filtering data (Z & P done)
- machine learning using decision tree algorithm with sklearn framework (my friend Done)
- result and conclusion in statistical meaning (Anna & my friend not yet started)
- write up the template for the remaining paragraphs in the paper (A & A done)
- run data + get emotion values (P done)
- machine learning using decision tree algorithm with sklearn framework (my friend done)
- Have meeting in the weekend to finalize the literature review.
- Research topic: Can we use online pictures and videos to detect early symptoms of motor disorders in patients? 
- Approach: Can we compare the accuracy with facial expression recognition in normal people, and use it as an indicator of the risk first?
- Provide research literature review, will need to submit it to REX on next week.
- Find out the limitation of the current research.

Abstract:
- https://docs.google.com/document/d/1dmmE--VwOc0T7PapOv-us6ZdQmqF4DJjhlztl6qpwNU/edit

Main paper: 
- https://docs.google.com/document/d/1-u4XFWJjHWnzD40yFFj9TyUYooPIxXLkOaCmwqGCnf4/edit

Help writing papers:
- https://medium.com/nerd-for-tech/deep-face-recognition-in-python-41522fb47028
- https://osf.io/dashboard

Parkinson related:

Limitation of facial recognition in Parkinson's:
1. factors like age-related differences, cultural differences and the method of data analysis can affect recognizing and predicting PD in facial expression processing. (possible solution: instead of recognizing a particular disease, we can predict a more generic mental disorder disease based on the evaluation.)
- https://arxiv.org/pdf/2012.06563.pdf
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6868040/
- https://iopscience.iop.org/article/10.1088/1742-6596/1937/1/012058/pdf
- https://www.sciencedirect.com/science/article/pii/S0165027017300481
2. facial expressions are highly correlated to the severity of the disease. Patients with PD often show dull expressions in the middle and late stage. 
- https://www.sciencedirect.com/science/article/pii/S0885230821000887 

Other:

How mental disorders affect facial expression accuracy(if parkinson's data is not accessible):
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0015058
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8493300/
- https://onlinelibrary.wiley.com/doi/full/10.1111/j.1399-5618.2004.00121.x?casa_token=lgp[…]D2PJ-rzcJ0bN5Hv5_iSQVSJvUhDgo9URNrzAvCmjjkzbQlTQ022NbnVgI
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2932776/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8316620/
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4277603/ 


Code Resources:
- (Open Pose Tutorial): https://www.youtube.com/watch?v=4FZrE3cmTPA&list=PL_Nji0JOuXg24bHB60SB2TwF0PpwhJkCF&index=2


Hardware:
- My setup: CPU: AMD Ryzen 5 3600X; Display Card: NVIDIA GeForce RTX 3070 Ti; RAM: 32gb ddr4 ram 3600mhz
- Possible: I have RTX TITAN 24GB and RTX 3090 Ti, even A6000 computer.



Data Set:

- (for download pictures): https://chrome.google.com/webstore/detail/image-downloader/cnpniohnfphhjihaiiggeabnkjhpaldj/related
- (for download pictures): https://www.youtube.com/watch?v=NBuED2PivbY
- (analysis tool): https://viso.ai/computer-vision/deepface/
- (analysis tool): https://github.com/serengil/deepface
- (analysis tool): https://www.youtube.com/watch?v=WnUVYQP4h44
- https://www.kaggle.com/datasets/ashwingupta3012/human-faces?resource=download
- https://analyticsindiamag.com/10-face-datasets-to-start-facial-recognition-projects/#:~:text=UTKFace%20dataset%20is%20a%20large,of%20age%2C%20gender%20and%20ethnicity
- https://imerit.net/blog/5-million-faces-top-14-free-image-datasets-for-facial-recognition-all-pbm/
- https://www.kaggle.com/datasets/drgilermo/face-images-with-marked-landmark-points
- https://research.google/tools/datasets/google-facial-expression/
- https://github.com/NVlabs/ffhq-dataset
- https://www.kaggle.com/datasets/shawon10/ckplus


