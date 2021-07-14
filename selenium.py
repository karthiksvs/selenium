# Python program to demonstrate
# selenium

# import webdriver
from selenium import webdriver
from csv import writer
# create webdriver object
file_name=input("Enter file location:")
header=['Name','Designation','Number','Email']
with open(file_name, 'a+', newline='') as write_obj:
    # Create a writer object from csv module
    csv_writer = writer(write_obj)
    # Add contents of list as last row in the csv file
    csv_writer.writerow(header)
    driver = webdriver.Firefox()

    # get geeksforgeeks.org
    driver.get("www.")#website link
    print("Started")
    # get element
    lnks=driver.find_elements_by_tag_name("a")
    # traverse list
    list_link=[]
    link=0
    for a in driver.find_elements_by_xpath('.//a'):
        list_link.insert(link,a.get_attribute('href'))
        link=link+1
    for x in range(36,69):
        final=[]
        driver.get(list_link[x])
        element = driver.find_element_by_xpath("//*[@class ='col-md-8']")   
        # print complete element
        #print(element.text)
        val=str(element.text)
        value1=val.split("\n")
        if(x<43):
            for fin in range(0,len(value1)):
                final.insert(fin+1,value1[fin])
            csv_writer.writerow(final)
        elif(x<55):
            for fin in range(0,len(value1)):
                final.insert(fin+1,value1[fin])
            csv_writer.writerow(final)
        elif(x<63):
            for fin in range(0,len(value1)):
                final.insert(fin+1,value1[fin])
            csv_writer.writerow(final)
        else:
            for fin in range(0,len(value1)):
                final.insert(fin+1,value1[fin])
            csv_writer.writerow(final)
        print(value1)
    print("Completed")
    driver.close()
