# 🏡 Unraveling Vancouver's Housing Challenge through Building Permits Analysis 🏡 

## 📒 Table of Contents <a class="anchor" id="toc"></a>
- [Project Overview](#overview)
    - [Introduction](#intro)
    - [Problem Statement](#problem)
    - [The Big Ideas](#ideas)
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
    - [Feature Selection](#select)
    - [Model Development](#develop)
    - [Model Interpretation](#interpret)
    - [Model Deployment](#deploy)
    - [User Interface Development](#ui)
---

## ✏️ Project Overview <a class="anchor" id="overview"></a>

### ℹ Introduction <a class="anchor" id="intro"></a>

Vancouver is currently grappling with a significant housing challenge marked by soaring property prices and a scarcity of affordable housing. This project endeavors to investigate the intricate relationship between Vancouver's housing crisis and the city's building permit dynamics.

By looking at the dataset of building permits issued since 2017, I aim to uncover insights into how the permitting process contributes to or mitigates the housing shortage. The analysis will delve into the patterns, timelines, and characteristics of issued permits to identify potential bottlenecks and inefficiencies. Understanding the nuances of the permitting process, including the types of constructions and regional variations, can offer valuable information for crafting effective urban development and housing solutions.


### 🎯 Problem Statement <a class="anchor" id="problem"></a>
The goal is to provide evidence-based insights that inform policy decisions, aid city planning, and foster collaborations among stakeholders. Through this project, I aspire to contribute meaningful knowledge towards addressing Vancouver's housing affordability challenge and creating a more accessible and equitable living environment for its residents.

**City Planners and Officials** can use the predictions to optimize the workflow, allocate resources efficiently, and improve the overall efficiency of the permitting process.

Knowing the estimated permit issuance time can help **Applicants and Developers** plan construction timelines more accurately.

### 💡 The Big Ideas <a class="anchor" id="ideas"></a> 💡
 
**Identifying High-Demand Areas:** Use the building permits data to identify neighborhoods or zones with high demand for housing. This information can help city planners and developers target specific areas for new construction projects.

**Predicting Future Trends:** Utilize machine learning algorithms to analyze historical building permits data and predict future trends in housing demand. This can assist in proactive planning and resource allocation.

**Optimizing Permit Processing Times:** Analyze the dataset to identify bottlenecks or inefficiencies in the permit processing timeline. Streamlining this process could accelerate housing development.

**Spatial Analysis:** Use geospatial data to visualize the distribution of building permits across the city. This can help in identifying areas with concentrated development and areas that may need more attention

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
- Formatting & Validity
- Remove records with the missing data which makes up less than 3% of the total observations in a column 

### ✅ Exploratory Data Analysis 🔍 <a class="anchor" id="eda"></a>
- Univariate Visualizations
- Multivariate Visualizations
- Time Series
- Statistical Analysis
- Correlation Analysis

### ✅ Feature Engineering 🔧 <a class="anchor" id="engine"></a>
- One Hot Encoding
- The Bag-of-Words (Count)

### ⏳ Model Development 🔨 <a class="anchor" id="develop"></a>
- Model Tested:
    - ✅ Logistic Regression **(Baseline Model)**
    - ✅ Decision Tree **(Baseline Model)**
    - 🔜 Seasonal ARIMA
    - 🔜 XGBoost
    - 🔜 Random Forest
    - 🔜 Neural Networks
 
- 🔜  Model Evaluation 📏 

- 🔜 Model Performance  🚀 

### 🔜 Model Interpretation 🔢 <a class="anchor" id="interpret"></a>

### 🔜 Feature Selection 📤 <a class="anchor" id="select"></a>
- Principal Component Analysis

### 🔜  Model Deployment 🚛 <a class="anchor" id="deploy"></a>

### 🔜 User Interface Development 🖥️ <a class="anchor" id="ui"></a>
