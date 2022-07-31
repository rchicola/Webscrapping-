import requests
#pip install beautifulsoup4 --user
from bs4 import BeautifulSoup as bs
import re
#!pip install pandas --user
import pandas as pd
import numpy as np
import os
os.getcwd()
import string
#!pip install xlsxwriter --user
import xlsxwriter
import itertools
#!pip install selenium --user
import selenium
#Gives access to escape key, Enter key, etc so we program can "click" enter to get search results
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#pip install requests_html
#import requests_html

#Set up Webdriver
from selenium import webdriver

# Install chrome driver for your OS in a filepath of your choosing
# create variable for that path

PATH = "C:\Program Files (x86)\chromedriver.exe"
#Pick your browser
driver = webdriver.Chrome(PATH)

#Open the website you want
driver.get("https://www.washoecounty.us/assessor/cama/index.php")

#Use right-click ->"Inspect" to find html for search box, for Washoe, name="search_term"
search = driver.find_element_by_name("search_term")
#Types the Test search using test APN 038-211-14 into the search bar
search.send_keys("038-211-14")
#Clicks Enter
search.send_keys(Keys.RETURN)

#Access entire page source
#print(driver.page_source)
URL ='https://www.washoecounty.us/assessor/cama/?command=assessment_data&parid=038-211-14'
page = requests.get(URL)

driver.implicitly_wait(5)
# Create a Beautiful Soup Object
soup = bs(page.content)
print(soup.prettify())


#########################################################################
#Owner Information
#########################################################################
APN = driver.find_elements_by_xpath('//tr/th')

for elem in APN:
	if elem.text == "APN":
		APN_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(APN_Elem.text)


Situs1 = driver.find_elements_by_xpath('//tr/th')

for elem in Situs1:
	if elem.text == "Situs 1":
		Situs1_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Situs1_Elem.text)

Owner1 = driver.find_elements_by_xpath('//tr/th')

for elem in Owner1:
	if elem.text == "Owner 1":
		Owner1_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Owner1_Elem.text)


mailHeading = driver.find_elements_by_xpath('//tr/th')

for elem in mailHeading:
	if elem.text == "Mail Address":
		addressElem = elem.find_element_by_xpath('./following-sibling::td')
		print(addressElem.text)

#########################################################################
#Parcel Information
#########################################################################
Keyline_Desc = driver.find_elements_by_xpath('//tr/th')

for elem in Keyline_Desc:
	if elem.text == "Keyline Desc":
		KeylineDesc_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(KeylineDesc_Elem.text)


Subdivision = driver.find_elements_by_xpath('//tr/th')

for elem in Subdivision:
	if elem.text == "Subdivision":
		Subdivision_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Subdivision_Elem.text)

Section = driver.find_elements_by_xpath('//tr/th')

for elem in Section:
	if elem.text == "Section":
		Section_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Section_Elem.text)

Township = driver.find_elements_by_xpath('//tr/th')

for elem in Township:
	if elem.text == "Township":
		Township_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Township_Elem.text)

Range = driver.find_elements_by_xpath('//tr/th')

for elem in Range:
	if elem.text == "Range":
		Range_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Range_Elem.text)

Surv_Map_Rec = driver.find_elements_by_xpath('//tr/th')

for elem in Surv_Map_Rec:
	if elem.text == "Record of Survey Map":
		Surv_Map_Rec_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Surv_Map_Rec_Elem.text)

Parcel_Map_Num = driver.find_elements_by_xpath('//tr/th')

for elem in Parcel_Map_Num:
	if elem.text == "Parcel Map#":
		Parcel_Map_Num_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Parcel_Map_Num_Elem.text)

Sub_Map = driver.find_elements_by_xpath('//tr/th')

for elem in Sub_Map:
	if elem.text == "Sub Map#":
		Sub_Map_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Sub_Map_Elem.text)

Spec_Prop_Code = driver.find_elements_by_xpath('//tr/th')

for elem in Spec_Prop_Code:
	if elem.text == "Special Property Code":
		Spec_Prop_Code_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Spec_Prop_Code_Elem.text)

Tax_Distr_2021 = driver.find_elements_by_xpath('//tr/th')

for elem in Tax_Distr_2021:
	if elem.text == "2021 Tax District":
		Tax_Distr_2021_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Tax_Distr_2021_Elem.text)

Prior_APN = driver.find_elements_by_xpath('//tr/th')

for elem in Prior_APN:
	if elem.text == "Prior APN":
		Prior_APN_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Prior_APN_Elem.text)

Tax_Distr_2020 = driver.find_elements_by_xpath('//tr/th')

for elem in Tax_Distr_2020:
	if elem.text == "2020 Tax District":
		Tax_Distr_2020_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Tax_Distr_2020_Elem.text)

Tax_Cap_Status = driver.find_elements_by_xpath('//tr/th')

for elem in Tax_Cap_Status:
	if elem.text == "Tax Cap Status":
		Tax_Cap_Status_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Tax_Cap_Status_Elem.text)

#########################################################################
#Building Information
#########################################################################

Building1 = driver.find_elements_by_xpath('//tr/th')

for elem in Building1:
	if elem.text == "Bld #1 Situs":
		Building1_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Building1_Elem.text)

Quality = driver.find_elements_by_xpath('//tr/th')

for elem in Quality:
	if elem.text == "Quality":
		Quality_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Quality_Elem.text)

Stories = driver.find_elements_by_xpath('//tr/th')

for elem in Stories:
	if elem.text == "Stories":
		Stories_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Stories_Elem.text)


YearBuilt = driver.find_elements_by_xpath('//tr/th')

for elem in YearBuilt:
	if elem.text == "Year Built":
		YearBuilt_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(YearBuilt_Elem.text)


Bedrooms = driver.find_elements_by_xpath('//tr/th')

for elem in Bedrooms:
	if elem.text == "Bedrooms":
		Bedrooms_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Bedrooms_Elem.text)

FullBaths = driver.find_elements_by_xpath('//tr/th')

for elem in FullBaths:
	if elem.text == "Full Baths":
		FullBaths_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(FullBaths_Elem.text)

HalfBaths = driver.find_elements_by_xpath('//tr/th')

for elem in FullBaths:
	if elem.text == "Half Baths":
		HalfBaths_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(HalfBaths_Elem.text)


Fixtures = driver.find_elements_by_xpath('//tr/th')

for elem in Fixtures:
	if elem.text == "Fixtures":
		Fixtures_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Fixtures_Elem.text)


Fireplaces = driver.find_elements_by_xpath('//tr/th')

for elem in Fireplaces:
	if elem.text == "Fireplaces":
		Fireplaces_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Fireplaces_Elem.text)


HeatType = driver.find_elements_by_xpath('//tr/th')

for elem in HeatType:
	if elem.text == "Heat Type":
		HeatType_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(HeatType_Elem.text)

HeatType2nd = driver.find_elements_by_xpath('//tr/th')

for elem in HeatType2nd:
	if elem.text == "2nd Heat Type":
		HeatType2nd_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(HeatType2nd_Elem.text)

ExteriorWalls = driver.find_elements_by_xpath('//tr/th')

for elem in ExteriorWalls:
	if elem.text == "Exterior Walls":
		ExteriorWalls_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(ExteriorWalls_Elem.text)

ExtWall2nd = driver.find_elements_by_xpath('//tr/th')

for elem in ExtWall2nd:
	if elem.text == "2nd Ext Walls":
		ExtWall2nd_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(ExtWall2nd_Elem.text)

RoofCover = driver.find_elements_by_xpath('//tr/th')

for elem in RoofCover:
	if elem.text == "Roof Cover":
		RoofCover_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(RoofCover_Elem.text)

Perc_Compl = driver.find_elements_by_xpath('//tr/th')

for elem in Perc_Compl:
	if elem.text == "% Complete":
		Perc_Compl_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Perc_Compl_Elem.text)

Obso_bldg_adj = driver.find_elements_by_xpath('//tr/th')

for elem in Obso_bldg_adj:
	if elem.text == "Obso/Bldg Adj":
		Obso_bldg_adj_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Obso_bldg_adj_Elem.text)

Construct_Modifier = driver.find_elements_by_xpath('//tr/th')

for elem in Construct_Modifier:
	if elem.text == "Construction Modifier":
		Construct_Modifier_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Construct_Modifier_Elem.text)

Property_Name = driver.find_elements_by_xpath('//tr/th')

for elem in Property_Name:
	if elem.text == "Property Name":
		Property_Name_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Property_Name_Elem.text)


Bldg_type = driver.find_elements_by_xpath('//tr/th')

for elem in Bldg_type:
	if elem.text == "Building Type":
		Bldg_type_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Bldg_type_Elem.text)


Occupy_2nd = driver.find_elements_by_xpath('//tr/th')

for elem in Occupy_2nd:
	if elem.text == "2nd Occupancy":
		Occupy_2nd_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Occupy_2nd_Elem.text)

WAY = driver.find_elements_by_xpath('//tr/th')

for elem in WAY:
	if elem.text == "WAY":
		WAY_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(WAY_Elem.text)


Sqr_feet = driver.find_elements_by_xpath('//tr/th')

for elem in Sqr_feet:
	if elem.text == "Square Feet":
		Sqr_feet_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Sqr_feet_Elem.text)

Fin_Bsmt = driver.find_elements_by_xpath('//tr/th')

for elem in Fin_Bsmt:
	if elem.text == "Finished Bsmt":
		Fin_Bsmt_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Fin_Bsmt_Elem.text)


Unfin_Bsmt = driver.find_elements_by_xpath('//tr/th')

for elem in Unfin_Bsmt:
	if elem.text == "Unfin Bsmt":
		Unfin_Bsmt_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Unfin_Bsmt_Elem.text)

Bsmt_type = driver.find_elements_by_xpath('//tr/th')

for elem in Bsmt_type:
	if elem.text == "Basement Type":
		Bsmt_type_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Bsmt_type_Elem.text)

Gar_Conv_Sq_Feet = driver.find_elements_by_xpath('//tr/th')

for elem in Gar_Conv_Sq_Feet:
	if elem.text == "Gar Conv Sq Feet":
		Gar_Conv_Sq_Feet_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Gar_Conv_Sq_Feet_Elem.text)


Tot_Gar_Area = driver.find_elements_by_xpath('//tr/th')

for elem in Tot_Gar_Area:
	if elem.text == "Total Garage Area":
		Tot_Gar_Area_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Tot_Gar_Area_Elem.text)


Gar_Type = driver.find_elements_by_xpath('//tr/th')

for elem in Gar_Type:
	if elem.text == "Garage Type":
		Gar_Type_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Gar_Type_Elem.text)

Detach_Gar = driver.find_elements_by_xpath('//tr/th')

for elem in Detach_Gar:
	if elem.text == "Detached Garage":
		Detach_Gar_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Detach_Gar_Elem.text)


Bsmt_Gar_Door = driver.find_elements_by_xpath('//tr/th')

for elem in Bsmt_Gar_Door:
	if elem.text == "Basement Gar Door":
		Bsmt_Gar_Door_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Bsmt_Gar_Door_Elem.text)

Sub_Floor = driver.find_elements_by_xpath('//tr/th')

for elem in Sub_Floor:
	if elem.text == "Sub Floor":
		Sub_Floor_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Sub_Floor_Elem.text)

Frame = driver.find_elements_by_xpath('//tr/th')

for elem in Frame:
	if elem.text == "Frame":
		Frame_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Frame_Elem.text)

Frame = driver.find_elements_by_xpath('//tr/th')

for elem in Frame:
	if elem.text == "Frame":
		Frame_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Frame_Elem.text)

Units_Bldg = driver.find_elements_by_xpath('//tr/th')

for elem in Units_Bldg:
	if elem.text == "Units/Bldg":
		Units_Bldg_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Units_Bldg_Elem.text)


Units_Parcel = driver.find_elements_by_xpath('//tr/th')

for elem in Units_Parcel:
	if elem.text == "Units/Parcel":
		Units_Parcel_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Units_Parcel_Elem.text)


#########################################################################
#Land Information
#########################################################################
Land_Use = driver.find_elements_by_xpath('//tr/th')

for elem in Land_Use:
	if elem.text == "Land Use":
		Land_Use_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Land_Use_Elem.text)

Sewer = driver.find_elements_by_xpath('//tr/th')

for elem in Sewer:
	if elem.text == "Sewer":
		Sewer_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Sewer_Elem.text)

Neighborhood = driver.find_elements_by_xpath('//tr/th')

for elem in Neighborhood:
	if elem.text == "Neighborhood":
		Neighborhood_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Neighborhood_Elem.text)

Size = driver.find_elements_by_xpath('//tr/th')

for elem in Size:
	if elem.text == "Size":
		Size_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Size_Elem.text)

Street_Road_type = driver.find_elements_by_xpath('//tr/th')

for elem in Street_Road_type:
	if elem.text == "Street":
		Street_Road_type_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Street_Road_type_Elem.text)

Zoning_Code = driver.find_elements_by_xpath('//tr/th')

for elem in Zoning_Code:
	if elem.text == "Zoning Code":
		Zoning_Code_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Zoning_Code_Elem.text)

Water = driver.find_elements_by_xpath('//tr/th')

for elem in Water:
	if elem.text == "Water":
		Water_Elem = elem.find_element_by_xpath('./following-sibling::td')
		print(Water_Elem.text)




#########################################################################
#Sales and Transfer Records
#########################################################################

Grantor_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[1]')
print(Grantor_R1.text)
Grantor_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[1]')
print(Grantor_R2.text)
Grantor_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[1]')
print(Grantor_R3.text)
Grantor_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[2]')
print(Grantor_R4.text)
Grantor_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[1]')
print(Grantor_R5.text)
########################################
Grantee_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[2]')
print(Grantee_R1.text)
Grantee_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[2]')
print(Grantee_R2.text)
Grantee_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[2]')
print(Grantee_R3.text)
Grantee_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[2]')
print(Grantee_R4.text)
Grantee_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[2]')
print(Grantee_R5.text)
########################################
Doc_Num_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[3]')
print(Doc_Num_R1.text)
Doc_Num_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[3]')
print(Doc_Num_R2.text)
Doc_Num_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[3]')
print(Doc_Num_R3.text)
Doc_Num_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[3]')
print(Doc_Num_R4.text)
Doc_Num_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[3]')
print(Doc_Num_R5.text)
########################################
Doc_Type_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[4]')
print(Doc_Type_R1.text)
Doc_Type_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[4]')
print(Doc_Type_R2.text)
Doc_Type_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[4]')
print(Doc_Type_R3.text)
Doc_Type_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[4]')
print(Doc_Type_R4.text)
Doc_Type_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[4]')
print(Doc_Type_R5.text)
########################################

Doc_Date_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[5]')
print(Doc_Date_R1.text)
Doc_Date_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[5]')
print(Doc_Date_R2.text)
Doc_Date_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[5]')
print(Doc_Date_R3.text)
Doc_Date_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[5]')
print(Doc_Date_R4.text)
Doc_Date_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[5]')
print(Doc_Date_R5.text)
########################################

DOR_code_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[6]')
print(DOR_code_R1.text)
DOR_code_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[6]')
print(DOR_code_R2.text)
DOR_code_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[6]')
print(DOR_code_R3.text)
DOR_code_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[4]')
print(DOR_code_R4.text)
DOR_code_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[6]')
print(DOR_code_R5.text)
########################################

Sale_Price_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[7]')
print(Sale_Price_R1.text)
Sale_Price_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[7]')
print(Sale_Price_R2.text)
Sale_Price_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[7]')
print(Sale_Price_R3.text)
Sale_Price_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[7]')
print(Sale_Price_R4.text)
Sale_Price_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[7]')
print(Sale_Price_R5.text)
########################################

Sale_Code_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[8]')
print(Sale_Code_R1.text)
Sale_Code_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[8]')
print(Sale_Code_R2.text)
Sale_Code_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[8]')
print(Sale_Code_R3.text)
Sale_Code_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[8]')
print(Sale_Code_R4.text)
Sale_Code_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[8]')
print(Sale_Code_R5.text)
########################################

Note_R1 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[2]/td[9]')
print(Note_R1.text)
Note_R2 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[3]/td[9]')
print(Note_R2.text)
Note_R3 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[4]/td[9]')
print(Note_R3.text)
Note_R4 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[5]/td[9]')
print(Note_R4.text)
Note_R5 = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/table[6]/tbody/tr[6]/td[9]')
print(Note_R5.text)
########################################



#########################################################################
#Valuation Information
#########################################################################

########################################
Taxable_Land_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[2]')
print(Taxable_Land_2021_22_NR.text)
Taxable_Land_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[2]')
print(Taxable_Land_2021_22_VN.text)
Taxable_Land_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[2]')
print(Taxable_Land_2020_21_FV.text)
########################################
New_Value_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[3]')
print(New_Value_2021_22_NR.text)
New_Value_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[3]')
print(New_Value_2021_22_VN.text)
New_Value_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[3]')
print(New_Value_2020_21_FV.text)
########################################
Taxable_Imps_2021_22_NR = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[2]/td[5]')
print(Taxable_Imps_2021_22_NR.text)
Taxable_Imps_2021_22_VN = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[3]/td[5]')
print(Taxable_Imps_2021_22_VN.text)
Taxable_Imps_2020_21_FV = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[4]/td[5]')
print(Taxable_Imps_2020_21_FV.text)
########################################
OBSO_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[6]')
print(OBSO_2021_22_NR.text)
OBSO_2021_22_VN = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[3]/td[6]')
print(OBSO_2021_22_VN.text)
OBSO_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[6]')
print(OBSO_2020_21_FV.text)
########################################
Tax_Cap_Val_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[7]')
print(Tax_Cap_Val_2021_22_NR.text)
Tax_Cap_Val_2021_22_VN = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[3]/td[7]')
print(Tax_Cap_Val_2021_22_VN.text)
Tax_Cap_Val_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[7]')
print(Tax_Cap_Val_2020_21_FV.text)
########################################
Taxable_Total_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[8]')
print(Taxable_Total_2021_22_NR.text)
Taxable_Total_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[8]')
print(Taxable_Total_2021_22_VN.text)
Taxable_Total_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[8]')
print(Taxable_Total_2020_21_FV.text)
########################################
Land_Assessed_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[9]')
print(Land_Assessed_2021_22_NR.text)
Land_Assessed_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[9]')
print(Land_Assessed_2021_22_VN.text)
Land_Assessed_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[9]')
print(Land_Assessed_2020_21_FV.text)
########################################
Imps_Assessed_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[10]')
print(Imps_Assessed_2021_22_NR.text)
Imps_Assessed_2021_22_VN = driver.find_element_by_xpath('//*[@id="qi_parcel_div"]/div[10]/table/tbody/tr[3]/td[10]')
print(Imps_Assessed_2021_22_VN.text)
Imps_Assessed_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[10]')
print(Imps_Assessed_2020_21_FV.text)
########################################
Total_Assessed_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[12]')
print(Total_Assessed_2021_22_NR.text)
Total_Assessed_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[12]')
print(Total_Assessed_2021_22_VN.text)
Total_Assessed_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[12]')
print(Total_Assessed_2020_21_FV.text)
########################################
Exemption_Value_2021_22_NR = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[2]/td[13]')
print(Exemption_Value_2021_22_NR.text)
Exemption_Value_2021_22_VN = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[3]/td[13]')
print(Exemption_Value_2021_22_VN.text)
Exemption_Value_2020_21_FV = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[5]/div/article/div[2]/div/div[7]/div[10]/table/tbody/tr[4]/td[13]')
print(Exemption_Value_2020_21_FV.text)
########################################
























