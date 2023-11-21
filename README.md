# dnp-aapi-data
Demographic data often misrepresents marginalized communities, whether it be through overgeneralizing experiences by aggregating data when it shouldn’t, omitting entire communities from the data altogether, or categorizing individuals as “other." Asian American Pacific Islander (AAPI) people are particularly at risk, being misrepresented in all kinds of data from cardiovascular risk data to education data. These issues are not only inherently harmful but also inflict more harm when problematic data is used to develop AI. In an investigation of data bias against AAPI people, I employed machine learning and data analysis on Census microdata: I analyzed the effects of disaggregating race data, compared various approaches to coding data on multiracial and multiethnic people, and studied the effects of including race data in AI.

To do so, I built an AAPI socioeconomic dataset using lasso regression, indexing, and a correlation matrix on the Census microdata. You can find the data dictionary for the dataset [here](https://docs.google.com/document/d/1hGPmwgD06HIE2_xxVq_vM5hiXBkpkHPKOc7wLQHmA8M/edit). With income as the target, I trained 6 machine learning models with the dataset, each with a different level of ethnoracial data. In order of best-performing to worst-performing:  
(1) **ethnicity (other):** with only ethnicity data, all multiethnic and multiracial people classified as "other"  
(2) **ethnicity (census):** with only ethnicity data, including some categories for multiethnic people  
(3) **race:** with only race data, including categories for multiracial people  
(4) **race (other):** with only race data, all multiracial people classified as "other"  
(5) **no ethnoracial data:** with no race or ethnicity data  
(6) **ethnicity:** with only ethnicity data, including categories for multiethnic people   
  
(1), (2), and (4) were categories already given with Census data, and (3) and (6) were created by me based on the data as alternative approaches to coding data on multiracial and multiethnic people.

The results show the following:  
(1) For the most part, disaggregating AAPI race data improves predictions. 2 of 3 ethnicity models—**ethnicity (other) and ethnicity (census)** performed better than the 2 race models. While obtaining disaggregated data does require more effort, it is vital to fairly represent AAPI people in data  
(2) Expanding ethnoracial categories to be more inclusive improved model performance for race, but not for ethnicity. The likely reason for this is that **race (other)** had 20 categories compared to **race**’s 3 whereas **ethnicity (census)** had 87 and **ethnicity** had 105 compared to **ethnicity (other)**’s 30 — too many categories hurt model performance. This does not necessarily mean that it is better to code mixed people as “other”, but rather that we need to find a midpoint between coding mixed people as “other” and coding every ethnicity combination, regardless of population size. The multiracial and multiethnic AAPI population is getting larger and larger—currently, 19.47% are multiracial and 23.53% are multiethnic—and cannot continue to be ignored by demographic data.  
(3) All models (except **ethnicity**) performed better than **no ethnoracial data**, highlighting the importance of ethnoracial data to illustrate income disparities. That being said, in the decision to include ethnoracial data, context is key: for example, a model trained on past court cases may become unfairly biased with the inclusion of that data. 

