# Project Plan

## Title
<!-- Give your project a short title. -->
New York - Correlation between Census Data and EV Registrations

## Main Question

<!-- Think about one main question you want to answer based on the data. -->
1. Is there a correlation between Census Data and the amount of registered EVs in the counties of New York.

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->
In this project, I look at how different demographic characteristics, based on U.S. Census data, relate to the number of registered electric vehicles (EVs) in New York State counties. 
As more people turn to sustainable energy and green transportation, it's important to understand which demographic factors affect EV adoption.
I aim to find out if certain factors—like age, income, racial makeup, education level, and whether an area is urban or rural—are linked to higher numbers of EV registrations.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: NY Registration records
* Metadata URL: https://data.ny.gov/Transportation/Vehicle-and-Boat-Registrations-by-Fuel-Type-per-Co/vw9z-y4t7/about_data
* Data URL: https://data.ny.gov/resource/vw9z-y4t7.csv
* Data Type: CSV

### Datasource1: NY Census
* Metadata URL: https://data.census.gov/table/ACSST5Y2022.S0101?g=040XX00US36$0500000
* Data URL: https://api.census.gov/data/2022/acs/acs5/subject?get=group(S0101)&ucgid=pseudo(0400000US36$0500000)
* Data Type: JSON


## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Calculate EV Percentage for each county
2. Match both datasources on country
3. Normalize census data
4. Calculate correlation
