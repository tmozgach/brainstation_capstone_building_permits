
# 🏡 Unraveling Vancouver's Housing Challenge through Building Permits Analysis 🏡 

## 📒 Table of Contents <a class="anchor" id="toc"></a>
- [Project Overview](#overview)
    - [Introduction](#intro)
    - [Problem Statement](#problem)
    - [The Big Idea](#ideas)
    - [Potential Impact](#impact)
- [Dataset](#dataset) 
    - [Data Description](#desc)
    - [Data Dictionary](#data-dict)
    - [Data Source](#data-source)
    - [Data Coverage](#data-coverage)
- [Project Plan](#plan)
    - [Data Cleaning](#cleaning)
    - [Exploratory Data Analysis](#eda)
    - [Feature Engineering](#engine)
    - [Model Development](#develop)
    - [Model Interpretation](#interpret)
    - [Model Deployment](#deploy)
    - [User Interface Development](#ui)
    - [Next steps...](#next)
---

## ✏️ Project Overview <a class="anchor" id="overview"></a>

### ℹ Introduction <a class="anchor" id="intro"></a>

Vancouver faces a significant housing challenge due to skyrocketing property prices and a lack of affordable housing. This project aims to explore the complex relationship between Vancouver's housing crisis and the city's building permit procedures.

Using a dataset of building permits issued since 2016, I intend to uncover insights into how the permit process influences the housing shortage. The analysis will examine patterns, timelines, and permit characteristics to identify potential obstacles and inefficiencies. Understanding the details of the permit process, such as the types of constructions and regional differences, can provide valuable insights for developing effective urban development and housing strategies.

### 🎯 Problem Statement <a class="anchor" id="problem"></a>
The goal is to provide evidence-based insights that inform policy decisions, aid city planning, and foster collaborations among stakeholders. Through this project, I aspire to contribute meaningful knowledge towards addressing Vancouver's housing affordability challenge and creating a more accessible and equitable living environment for its residents.

**City Planners and Officials** can use the predictions to optimize the workflow, allocate resources efficiently, and improve the overall efficiency of the permitting process.

Knowing the estimated permit issuance time can help **Applicants and Developers** plan construction timelines more accurately.

### 💡 The Big Idea <a class="anchor" id="ideas"></a> 💡
 
**Predicting Future Trends:** Utilize machine learning algorithms to analyze historical building permits data and predict future trends in housing demand. This can assist in proactive planning and resource allocation.

### 🤝😊 Potential Impact <a class="anchor" id="impact"></a>
 The societal value of this project lies in addressing a critical issue  that directly impacts the quality of life for Vancouver residents. By quantifying the scale of the problem through data analysis, I can  provide valuable information to policymakers and urban planners. This could lead to more informed decisions on housing development, potentially alleviating the shortage and making housing more accessible.

[Back to top](#toc)

---
## 📜📜📜 Dataset <a class="anchor" id="dataset"></a>

### Dataset Description <a class="anchor" id="desc"></a>
Building permits are required for new buildings, additions or alterations to existing buildings, and for demolitions or salvage and abatement work.

As permit application processing is a collaboration between the customer / applicant and the City, this dataset has been updated with the elapsed time from the date at which an application generated a permit number to when the permit was first issued. Specifically, the fields PermitNumberCreatedDate and PermitElapsedDays (includes weekends and holidays) are available in all views as well as through data exports and API access. In addition to existing fields that allow this data to be grouped (PropertyUse, TypeofWork, SpecificUseCategory) they have created a new group field, PermitCategory, that focuses on higher volume, lower complexity project scopes.

This dataset includes information of all building permits issued by the City of Vancouver, starting in 2017. The data is based on permit issuance date and does not show current status of a permit or changes after a permit is originally issued.

**Data currency**

​The extract for the current year is updated daily but the extract for prior year is static.

**Data accuracy**

There may be addresses that do not return coordinates through the geocoding process (using BC Address Geocoder API). These Issued Building Permits do not appear on the Map. Please consult the Table view for a complete list of Issued building permits​​

There may be some loss of quality from data entry errors and omissions, in particular where the original application date was prior to May 2016 (when permit software changed).

### 📑 Data Dictionary <a class="anchor" id="data-dict"></a>
| Field Name | Type | Description | Sample |
|------------|------|-------------|--------|
| PermitNumber | text | Unique permit number generated at application date; there may be multiple permits for one project site BU - Original Permit application was made in previous software BP - Building Permit DB - Combined Development & Building Permit | BP-2019-04164 |
| PermitNumberCreatedDate | date | The date at which a permit application, created by staff or an online process, receives a permit number | 2019-09-17 |
| IssueDate | date | Date when the specified permit was first issued | 2019-11-15 |
| PermitElapsedDays | integer | Measures the number of days from the creation and assignment of a permit number until the issuance of a permit.  Application processing represents a collaboration between the applicant/customer team and the City.  Timelines may be influenced by a number of factors, some of which include: the volume of instream applications to be processed, completeness of the application, site and project specific requirements impacting application requirements (number of reviews, conditions, design decisions, etc.), staff and customer response times. | 59 |
| ProjectValue | decimal | Estimated construction value at time of original permit issuance; base permit fees are calculated on this value. For commercial and mixed-use projects with multiple buildings on one site, the project value may be entered only on the site permit (and not the permits for each individual building where a $0 value will be shown) | 0 |
| TypeOfWork | text | Categories Include: Addition / Alteration, Demolition / Deconstruction, New Buildings, Outdoor Uses (No Buildings Proposed), Salvage and Abatement, Temporary Buildings / Structures | Salvage and Abatement |
| Address | text | Specific Property Address | 4094 W 30TH AVENUE, Vancouver, BC V6S 1X5 |
| ProjectDescription | text | Scope of work (note: data file prior to 2018 does not include this field) | Low Density Housing - Salvage and Abatement - SALVAGE AND ABATEMENT PERMIT Salvage and Abatement Permit only for Building permit: DB-2019-04161 and to be completed under the supervision of a registered professional.  This permit does not authorize demolition, deconstruction or construction work. QP:  MCA Environmental Consulting Inc. (Tarlochan (Terry) Sunar) Demolition permit: DB-2019-04162 |
| PermitCategory | text | A high level grouping providing a focus on higher volume, lower complexity project scopes. The categorization is derived from data in the TypeofWork, PropertyUse and ProjectDescription fields. This field was added in December 2021 and will be modified to take into account feedback from dataset users | - |
| Applicant | text | Applicant may be property owner or official agent for owner and is often the design professional or their firm | Scott Posno DBA: Scott Posno Design |
| ApplicantAddress | text | Contact information as provided on Permit Application | 1595 W 3rd Avenue Vancouver, BC  V6J 1J8 |
| PropertyUse | text | General use of property; where there is more than one, they are separated by a comma | Dwelling Uses |
| SpecificUseCategory | text | Category of property use; where there is more than one, they are separated by a comma | Single Detached House |
| BuildingContractor | text | Contractor information, if known, at time of permit issuance | Mercia Construction Ltd |
| BuildingContractorAddress | text | Contractor information, as provided by the applicant | - |
| IssueYear | text | Year which permit was first issued | 2019 |
| GeoLocalArea | text | The local area where the building with the Issued Building Permit is found, derived from the building's coordinates or address. The City of Vancouver has 22 local areas (also known as local planning areas). For more details, please see the Local Area Boundary data set. | Dunbar-Southlands |
| Geom | geo shape | These are mapping coordinates for the building corresponding to a Building Permit. Data from the Address attribute are processed by the BC Address Geocoder API. An unmatched address returns null coordinates and will not display on the Map. The permit will still be listed in the Table view. | {"coordinates":[-123.1965627,49.2450036],"type":"Point"} |
| YearMonth | text | No description available for this field. | 2019-11 |
| geo_point_2d | geo point | No description available for this field. | [49.2450036,-123.1965627] |

### 🗂️ Data Source <a class="anchor" id="data-source"></a>
Dataset can be found [here](https://opendata.vancouver.ca/explore/dataset/issued-building-permits/information/)

### 🗺️ Data Coverage <a class="anchor" id="data-coverage"></a>
- Temporal Coverage
    - Starting Date: 2016
    - Ending Date: 2024
    
- Geospatial Coverage
    - Vancouver, Canada
      
[Back to top](#toc)

---
## 📅  Project Plan <a class="anchor" id="plan"></a>

### ✅ Data Cleaning / Preprocessing 🚿  <a class="anchor" id="cleaning"></a>  
- Formatting & Validity (Objects -> Date)
- Cheking for duplicates
- Remove records with the missing data which makes up less than 3% of the total observations in a column
- Remove the column with missing data more than 35%

### ✅ Exploratory Data Analysis 🔍 <a class="anchor" id="eda"></a>
The analysis of permit data based on the below plots reveals valuable insights into the dynamics of construction activities and the permit application process in the given dataset.

_General Insights:_

**Property Usage and Permit Types:**
- Predominantly, permits are issued for Dwelling Uses (single detached house, duplex) and Office Uses (General office). The number of permits for Dwelling Uses is approximately five times higher than that for Office Uses.
- Addition/Alteration is the most common permit type, outnumbering New Building permits by a factor of five.

**Yearly Trends:**
- The year 2020 witnessed the lowest number of issued permits, possibly attributed to the impact of COVID-19 lockdown measures.
- The Downtown area stands out with the highest number of issued permits, indicating increased construction or renovation activity.

**Processing Times:**
- On average, the waiting time for permit issuance is 136 days. However, the presence of numerous outliers suggests significant variations in processing times.

_Relationships and Correlations:_

**Property Values and Waiting Times:**
- There is a positive correlation between higher property values and longer waiting times for permits, which is reasonable as more expensive projects often require more thorough analysis.
- The average waiting time for a new building permit is 248 days, while for Addition/Alteration, it is 81 days. This disparity is expected, considering that new building projects typically involve more complexities.
- Dwelling Uses exhibit an average waiting time of 159 days, significantly higher than other property uses such as Office Uses, which averages 52 days. This discrepancy may be attributed to a higher volume of Dwelling Uses applications, potentially leading to a shortage of staff resources.

_Seasonal Trends:_

**Monthly Permit Applications:**
- There is a consistent upward trend in monthly permit applications, with May and June consistently exhibiting the highest numbers on average.
- The sharp decline in the middle can be attributed to the impact of the Covid lockdown.
- Surprisingly, the year 2023 shows an even lower number of applications compared to the Covid period.

**Monthly Issued Permits:**
- There is a consistent upward trend in monthly issued permits, with May and June consistently exhibiting the highest numbers on average.
- The sharp decline in the middle can be attributed to the impact of the Covid lockdown.
- The year 2023 shows an even lower number of issued permits compared to the Covid period, due to the lower number of applications.

_Overall Insights:_
After experiencing a decline during the COVID-19 period, the number of permit applications exhibited a subsequent increase around the beginning of 2022. However, surprisingly, in 2023, the application count dropped even lower than during the COVID-19 period. It's important to note that the decrease in issued permits in 2023 is directly tied to the overall low level of applications rather than any issues related to permit approval.

### Distribution of categorical columns
![Property Use Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PropertyUse.png)
![Type of Work Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/TypeOfWork.png)
![Specific Use Category Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/SpecificUseCategory.png)
![Issue Year Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/IssueYear.png)
![Geo Local Area Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/GeoLocalArea.png)
### Distribution of numerical columns
![Project Value Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/ProjectValue.png)
![Permit Elapsed Days Plot](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PermitElapsedDays.png)
### Multivariate Visualizations
![Permit Elapsed Days vs Project Value](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PermitElapsedDaysVsProjectValue.png)
![Permit Elapsed Days vs Property Use](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PermitElapsedDaysVsPropertyUse.png)
![Permit Elapsed Days vs Specific Use Category](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PermitElapsedDaysVsSpecificUseCategory.png)
![Permit Elapsed Days vs Type of Work](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/PermitElapsedDaysVsTypeOfWork.png)
### Time Series
![Seasonal Plot of Issued Permits](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/SeasonalPlotIssuedPermits.png)
![Seasonal Plot of Created Permits](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/SeasonalPlotCreatedPermits.png)
### Trend-Seasonal Decomposition for IssueDate
![Trend Seasonal Decomposition of Issue Date](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/TrendSeasonalDecompositionIssueDate.png)
### Trend-Seasonal Decomposition for PermitNumberCreatedDate
![Trend Seasonal Decomposition of Permit Number Created Date](https://raw.githubusercontent.com/tmozgach/brainstation_capstone_building_permits/main/plots/TrendSeasonalDecompositionPermitNumberCreatedDate.png)

[Back to top](#toc)

---

### ✅ Feature Engineering 🔧 <a class="anchor" id="engine"></a>
- **One Hot Encoding**:  TypeOfWork, PropertyUse (top 12 frequent), SpecificUseCategory (top 22), GeoLocalArea
- **Drop columns**: IssueYear, IssueDate , PermitNumber, YearMonth, Geom
- **Bag-of-Words (Count)**: ProjectDescription, Applicant
![Frequency of Words in Project Description](https://github.com/tmozgach/brainstation_capstone_building_permits/raw/main/plots/FreqWordsProjectDescription.png)
![Frequency of Words in Applicant](https://github.com/tmozgach/brainstation_capstone_building_permits/raw/main/plots/FreqWordsApplicant.png)
- **Sine and cosine transformations** are used to capture the cyclical nature of time: PermitNumberCreatedDate

[Back to top](#toc)

---

### ⏳ Model Development 🔨 <a class="anchor" id="develop"></a>
- Notes:
0) Predict: _PermitElapsedDays_
1) `Robust scaler` is used because there are a lot of outliers.
2) `Ridge` regression is useful when multicollinearity is present among the predictors. 
3) Max depth for the `Decision tree` is 8.
4) `Polynomial Regression` has degree 2, Ridge, PCA = 50 -> Cumulative Explained Variance = 97%
5) Neural Networks can offer great flexibility and performance on large datasets, but `XGBoost` is often a more practical choice for smaller datasets due to its simplicity, efficiency, and ease of use in terms of training, tuning and interpretability. Thus, there are only 40k record in the data set, XGBoost is trained and tuned.
6) With a dataset of 34747 rows and 1069 columns, where most of the columns represent bag-of-words features, here's a suggested approach for parameter tuning and cross-validation for XGBoost:

    `learning_rate`: Start with a small value (e.g., 0.3 or lower) and tune it along with other parameters. 

    `max_depth`: Experiment with different values, but avoid very deep trees to prevent overfitting. 

    `subsample and colsample_bytree`: These parameters control the fraction of data and features used for each boosting round. Try values around 0.8 to 1.0 for subsample and colsample_bytree.

    `n_estimators`: The number of boosting rounds. 

    `Regularization parameters` like gamma, reg_alpha, and reg_lambda can also be tuned.

    Due to the size of the dataset, I may opt for a faster `cross-validation` strategy such as k-fold cross-validation with a smaller value of k (e.g., `3`). This will reduce the computational cost while still providing a reasonable estimate of model performance.


| Model | Linear Regression (Train) | Linear Regression (Test) | Ridge (Train) | Ridge (Test) | Decision Tree Regressor (Train) | Decision Tree Regressor (Test) | Polynomial Regression (Train) | Polynomial Regression (Test) | XGBoost (Train) | XGBoost (Test) |
|-------|---------------------------|--------------------------|---------------|--------------|---------------------------------|--------------------------------|-------------------------------|-----------------------------|-----------------|----------------|
| MAE | 63.58 | 36297850 | 63.61 | 65 | 62.85 | 64.46 | 63.03 | 66.25 | 53.95 | 59.61 |

Mean Absolute Error (`MAE`): On average, the best model's prediction (XGBoost) on the training set are off by approximately 54 days and on the testing set are off 60 days.

`Best Parameters`: {'colsample_bytree': 1.0, 'gamma': 0, 'learning_rate': 0.3, 'max_depth': 5, 'min_child_weight': 3, 'n_estimators': 100, 'reg_alpha': 0.1, 'reg_lambda': 1.0, 'subsample': 1.0}

`Time taken for training the model:` 18.856444160275988 hours

[Back to top](#toc)

---

### ✅ Model Interpretation 🔢 <a class="anchor" id="interpret"></a>
Keep in mind that `SHAP` values provide insights into the contribution of each feature to individual predictions and do not necessarily indicate a causal relationship.
### Most important features:
### ProjectValue:

`Positive` SHAP Value: Higher project values correlate with longer permit approval times, suggesting that larger or more complex projects undergo additional scrutiny.

`Negative` SHAP Value: Lower project values are associated with shorter approval times, indicating a streamlined process for smaller projects.

Color Distribution:

Mostly `Red`: Indicates longer approval times for higher project values.

Mostly `Blue`: Suggests shorter approval times for lower project values.

`Mixed Colors`: Reflects a nuanced relationship influenced by other factors.

### x0_New_Building:

`Positive` SHAP Value: Permits for new buildings are associated with longer approval times.
This reflects the complex nature of new construction projects, which may require extensive planning and regulatory compliance.

`Negative` SHAP Value: Indicates shorter approval times for other permit types.
These may include renovations or alterations, which could involve less extensive review processes.

Color Representation:

Mostly `Red`: Indicates longer approval times for new building permits.

Mostly `Blue`: Suggests shorter approval times for other permit types

### pd_density
if the project description mentions density, it may lead to a longer permit processing time due to additional precautions or considerations required for projects in densely populated areas.

### pd_vbbl 
Vancouver Building By-law the presence of "pd_vbbl" in the project description could potentially lead to a longer permit processing time. This feature likely indicates references to the Vancouver Building By-law in the project description. Compliance with building by-laws may require additional scrutiny or steps in the permit approval process, thereby contributing to delays in obtaining the permit.

### Month_sin
There is a seasonal pattern here, which were explored before.

### Location
if a project is planned to be built in `Downtown` or `Fairview`, it might take more time to obtain the permit compared to other areas. This could be due to various factors such as higher population density, stricter regulations, or more complex approval processes in these areas.

![SHAP](https://github.com/tmozgach/brainstation_capstone_building_permits/blob/main/plots/SHAP.png)

[Back to top](#toc)

---

### ✅  Model Deployment 🚛 <a class="anchor" id="deploy"></a>
### Run the Web Application locally

Clone the project

```git clone https://github.com/tmozgach/brainstation_capstone_building_permits.git ```

Go to `brainstation_capstone_building_permits/streamlit` folder

```cd brainstation_capstone_building_permits/streamlit```

Create the required building_permit environment for this notebook:

```
conda create -n building_permit python=3.8 numpy pandas matplotlib seaborn jupyter jupyterlab scikit-learn=0.24.1
conda activate building_permit
conda install -c plotly plotly=4.12.0
conda install -c bokeh bokeh=2.2.3
conda install streamlit
pip install --upgrade streamlit
pip install --upgrade plotly
pip install nltk
pip install shap
ipython kernel install --name "building_permit" --user
```
Run it

```streamlit run app.py```

[Back to top](#toc)

---
### ✅ User Interface Development 🖥️ <a class="anchor" id="ui"></a>
The simple web UI with streamlit Python API, where the user may input the data and make prediction with the best model.
![UI Screenshot](https://github.com/tmozgach/brainstation_capstone_building_permits/raw/main/plots/UI.png)

[Back to top](#toc)

---

### Next Steps... <a class="anchor" id="next"></a>
`User Interface (UI) Enhancement:` 
Enable users to select a location directly from the map instead of manually inputting latitude and longitude coordinates.

`Data Enhancement:`
Collect data from other municipalities in British Columbia or the Greater Vancouver area.

`Mode Enhancement:`
With more data available, try NN models.

[Back to top](#toc)

---
