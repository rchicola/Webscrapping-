# Webscrapping Code For Clark County
# By: Randall Chicola

# Let's start scraping the main  property text information
# of a single "Assesor Parcel Number (APN) (see NV clark county excel sheet)

#INSTALL & Library the RVEST package <----WEB Scrapping package
install.packages("rvest")
library(rvest)
# Other packages that may be useful
install.packages("xml2")
library(xml2)
install.packages("robotstxt")
library(robotstxt)
install.packages("selectr")
library(selectr)
install.packages("dplyr")
library(dplyr)
install.packages("stringr")
library(stringr)
install.packages("forcats")
library(forcats)
install.packages("magrittr")
library(magrittr)
install.packages("tidyr")
library(tidyr)
install.packages("ggplot")
library(ggplot)
install.packages("lubridate")
library(lubridate)
install.packages("tibble")
library(tibble)
install.packages("purrr")
library(purrr)
install.packages("XML")
library(XML)
#Test if path is allowed for scraping (if automated loop might be blocked)
paths_allowed(
  paths = c("https://maps.clarkcountynv.gov/assessor/AssessorParcelDetail/pcl.aspx")
  )
#Outputs "true" so it should be scrap-able 


# Using a sample APN (1st row from spreadsheet APN#  16327610009 in the
# Property Search by APN utility)

Clark_Assesor_APN_wbpg <- read_html("https://maps.clarkcountynv.gov/assessor/AssessorParcelDetail/ParcelDetail.aspx?hdnParcel=16327610009&hdnInstance=pcl7")

# test piping the webpage from the "view page source" html to print the title
Clark_Assesor_APN_wbpg %>%
  html_node("title") %>%
  html_text()  
#Success, it prints

#Use html_nodes to grabe table nodes
TestTable<- html_nodes(Clark_Assesor_APN_wbpg, "table")
#print out the top row ("head") of the table 
head(TestTable)
# prints error:     {xml_nodeset (0)}
# So looking in the html, the webpage has no "table" nodes, its in a weird nested structure form.




#Grabs and prints body node of the text
Clark_Assesor_APN_wbpg %>%
  html_node("body") %>%
  html_text()  
# So it seems to grab all the elements, but its unordered and has this \r\n crap
# Apparently these \r\n things are called "carriage return representations-- > https://www.scrapingbee.com/blog/web-scraping-r/

#First put the "Body node with text we want into a variable object
Body_node <- html_text(Clark_Assesor_APN_wbpg, "body")
Body_node
# So we use str_split command 
Clean_body <- str_split(Body_node, "\r\n")
Clean_body 

Squish_body <- str_squish(Clean_body)
#Clean out the \"
Clean_body2 <- str_split(Squish_body, "\"")
Clean_body2
#Squish again
Squish_body <- str_squish(Clean_body2)
Squish_body

#Wait, we want to remove substrings, want to be careful if we want to preserve  some commas for CSV
# Restart at Body node
Clean_body3 <- str_remove_all(Body_node,"\r\n")
Clean_body3
Squish_body3 <- str_squish(Clean_body3)
Squish_body3
Clean_body4 <- str_remove_all(Squish_body3,"\"")
Clean_body4 

#Kind of worked, Maybe easier to grab a select number of elements (e.g. "Assessed Value" )
#but let's try to squish text and clean other "junk"

# Need a way to grab more specific elements within the body
Clark_Assesor_APN_wbpg %>%
  html_node("p") %>%
  html_text( )  
# Did not work



Clark_Assesor_APN_wbpg %>%
  html_node("./html/body/table/tbody/tr[110]/td[2]/span[1]" )
  html_text() 


cast <- Clark_Assesor_APN_wbpg %>% html_nodes(".container-fluid") %>% html_text() 

cast
























































































































