Dataset readme

Author: Sébastien Lallé (lalles@cs.ubc.ca). The University of British Columbia, Vancouver, BC, Canada.

Original paper for which the dataset was created: Sébastien Lallé, Cristina Conatim Giuseppe Carenini. 2016. Predicting Confusion in Information Visualization from Eye Tracking and Interaction Data. In Proceedings of the International Joint Conference on Artificial Intelligence (IJCAI 2016), pp. New York, NY, USA. https://www.ijcai.org/Proceedings/16/Papers/360.pdf

Licence of the dataset and the data included in the archive: Creative Commons Attribution-ShareAlike 4.0 International (https://creativecommons.org/licenses/by-sa/4.0/)

If you reuse the data, please give appropriate credit by citing the above paper. 

Dataset description: The archive includes two CSV files with the data, one for the full window and one for the 5-seconds window (see details and definitions in the paper).

The datasets are formatted as follows:
- UID: user unique anonymized ID
- SessionID: the session ID. Each user performed two sessions (session "a" then session "b")
- Layout: whether the ValueChart visualization was used with a vertical of horizontal layout. Each user got both layouts in a random order in their two sessions. To learn more about the layouts, see http://www.cs.ubc.ca/group/iui/VALUECHARTS/. 
- Confusion: whether the user reported being confused at any time during the task
- Time_confusion: the timestamp in milliseconds since the beginning of the task, when the confusion report occurred
- PS: the levels of perceptual speed of the user (defined here: https://www.cs.ubc.ca/cs-research/lci/research-groups/human-ai-interaction/userchar.html)
- VisWM: the levels of visual working memory of the user (defined here: https://www.cs.ubc.ca/cs-research/lci/research-groups/human-ai-interaction/userchar.html)
- VerWM: the levels of verbal working memory of the user (defined here: https://www.cs.ubc.ca/cs-research/lci/research-groups/human-ai-interaction/userchar.html)
- Locus: the levels of locus of control of the user (defined here: https://www.cs.ubc.ca/cs-research/lci/research-groups/human-ai-interaction/userchar.html)
- Sc_type: the type of task performed (by order of difficulty: RV = retrieve a value; FE = find extremum; SortOverall = sort based on one attribute; CDV = compute derived value; SortTwoFactors = sort based on the aggregation of two attributes)
- Sc_id: the task ID. Each session is made of a maximum of 20 tasks
- The rest of the columns are the eye-tracking features computed for the corresponding window within the task. See the paper cited above for a full descriptions of these features and how they are computed. In addition the library used to compute these features is available at: https://github.com/ATUAV/EMDAT
