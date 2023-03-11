
import numpy as np                 #import numpy as np
import matplotlib.pyplot as plt    #import matplotlib as plt

class Country:
    """Class used to create Country object.
    
       Attributes:
         name: String that represents the country's name
         region: String that represents the country's region
         subregion: String that represents the country;s subregion
         area: String that represents the country's area
         population: String that represents the country's population
         population change: Integer that represents the country's change in population from 2000 to 2020
    
    """
    def __init__(self, name, region, subregion, area, population, population_change):
        self.name = name
        self.region = region
        self.subregion = subregion
        self.area = area
        self.population = population 
        self.population_change = population_change

    def print_all_stats(self):
        """A function that prints name, region, subregion, area, population and population change of the country instance
         
           Parameters: None
           Return: None

        """
        print('Country:', self.name)
        print('Region: ', self.region)
        print('Sub region: ',self.subregion)
        print('Area: ', self.area, 'Sq Km')
        print('Current Population:', self.population)
        print(f'Population change from 2000 to 2020 in {self.name} is: {self.population_change} people')

def most_threatened(position,data,country):    
    """ 
    Summary:
    Finds the maximum value from a list of numbers of threatened species and displays the information to user
    
    Parameters:
    position - represents the index of the country chosen by user in list of countries.
    data - represents the threatened species data imported from csv file as a numpy array
    country - represents the name of country input by user
    
    Returns:
    None
    """                                    
    num_threatened = list(data[position,:])    #index of country in list of countries is used to identify the row in the numpy array containing the country's threatened species and convert it into a list 
    num_threatened.pop(0)                      #first item in the list (the name of the country in the csv file) is remove
    list_num_threatened = [int(i) for i in num_threatened]      #all items in the list of number of threatened species are converted into integers
    species = list(data[0,:])            #list created from the top row of the data numpy array (types of organisms)
    species.pop(0)                       #first item in the list (header in the csv file) is removed
    dict_num_threatened_to_specie= dict(zip(list_num_threatened,species))   #dictionary that maps number of threatened species to organism category is created
    most_threatened_specie = np.array([int(i) for i in list_num_threatened]).max()  #items in list of number of threatened species are converted to integers and maximum value is found
    for key, values in dict_num_threatened_to_specie.items():   #for each key (number of threatened species) and value (the organism category) in dictionary:
        if key == most_threatened_specie:                       #if key equals to the maximum value:    
            print(f'\n{values} have the greatest number of threatened species in {country}. {key} species of {values.lower()} are currently considered threatened.' )  #dsplay the number of threatened species and which their organism category 
    
def graph_population(position,data):
    """
    Summary:
    Uses the data in the provided numpy array to create a graph of the country's population 
    from 2000 to 2020 (x-axis : years, y-axis : population)

    Parameters:
    position - represents the index of the country chosen by user in list of countries.
    data - represents the population data imported from csv file as a numpy array

    Returns:
    None
    """
    plt.figure(1)                     #figure 1 is created
    y_axis = list(data[position,:])   #index of country in list of countries is used to identify the row in the numpy array containing the country's population from 2000 to 2020 and convert it into a list 
    y_axis.pop(0)                     #first item in the list (the name of the country in the csv file) is remove
    x_axis = list(data[0,:])          #list created from the top row of the data numpy array 
    x_axis.pop(0)                     #first item in the list (header in the csv file) is removed
    plt.plot(x_axis,y_axis,'r', markersize = 5, alpha = 1.00, label = 'Population trend')  #line graph plotted with years on x-axis, population of country requested by user through the years on y-axis, line drawn in red  
    plt.xlabel('Years')                           #x-axis labeled
    plt.ylabel('Population')                      #y-axis labeled
    plt.xticks([0,2,5,8,11,14,17,20],['2000','2002','2005','2008','2011','2014','2017','2020'])  #8 labels are created on the x-axis only of even years from 2000 to 2020
    plt.legend(shadow=True, loc = 'upper left')   #legend created in the upper left corner of the graph
    plt.title('Population by year')               #figure 1 is titled
    plt.show()                                    #figure 1 is displayed
    
def average(position,data,country):         
    """
    Summary:
    Uses the data in the provided numpy array to find the mean population of the country requested by user 

    Parameters:
    position - represents the index of the country chosen by user in list of countries.
    data - represents the population data imported from csv file as a numpy array
    country - represents the name of country input by user

    Returns:
    None
    """
    list_population = list(data[position,:])  #index of country from list of countries is used to identify the row in the numpy array containing the country's population fro 2000 to 2020 and convert it into a list 
    list_population.pop(0)                       #first item in the list (the name of the country in the csv file) is remove 
    int_list= [int(i) for i in list_population]   #all items in the list of populations are converted into integers
    a = np.array(int_list)                        #the list of populations is converted into a numpy array a
    mean = int(np.mean(a))                        #mean function is called to find mean population
    print(f'\nThe average population of {country} from 2000 to 2020 was {mean} people')   #mean population of the country requested by user is displayed

def graph_threatened(position, data):
    """
    Summary:
    Uses data in the provided numpy array to create a bar chart of the number of threatened species in four different organism 
    categories within the country requested by user

    Parameters:
    position - represents the index of the country chosen by user in list of countries.
    data - represents the threatened species data imported from csv file as a numpy array

    Returns:
    None
    """ 
    plt.figure(2)                            #figure 2 is created                           
    x = list(data[0,:])                      #list created from the top row of the data numpy array (types of organisms)
    x.pop(0)                                 #first item in the list (header in the csv file) is removed
    y = list(data[position,:])               #index of country in list of countries is used to identify the row in the numpy array containing the country's threatened species and convert it into a list 
    y.pop(0)                                 #first item in the list (the name of the country in the csv file) is remove
    int_y = [int(n) for n in y]              #items in list converted to integers
    plt.bar(x, int_y, color = ['green', 'blue', 'orange', 'red'])   #bar chart plotted with category of organisms on x-axis, number of threatened species on y-axis, different colours of bars
    plt.ylabel('Number of threatened species')                      #y-axis labeled
    plt.title('Threatened species in nation')                       #graph titles
    plt.show()                                                      #graph displayed

def main():    
   
    country_data = np.genfromtxt('Country_Data.csv', delimiter=',',dtype = str)               #numpy array created from data in file 'Country_Data.csv'. Data imported as strings
    threatened_species = np.genfromtxt('Threatened_Species.csv', delimiter=',', dtype= str)   #numpy array created from data in file 'Threatened_Species.csv'. Data imported as strings
    population_data = np.genfromtxt('Population_Data.csv',delimiter=',',dtype= str)           #numpy array created from data in file 'Population_Data.csv'. Data imported as strings
    list_country_names = [country.lower() for country in list(country_data[:,0])]             #list of countries created from first column of numpy array country_data and names of countries converted to all lower case  
    print('                                       ****** WELLCOME T0 STATS PROGRAM ******  ')     #welcome to the program displayed
    print()  #line of space

    all_countries = list(country_data[:,0])  #list of countries created from first column of numpy array country_data
    all_countries.pop(0)                     #first item in the list (header in csv file) removed 
    all_regions = list(country_data[:,1])    #list of regions created from second column of numpy array country_data
    all_regions.pop(0)                       #first item in the list (header in csv file) removed
    dict_countries_to_regions = dict(zip(all_countries,all_regions))   #dictionary created that maps countries to the regions they are in

    choice_region = str(input('Please choose a region (Asia, Europe, Africa, Oceania or Americas): '))  #user promted to choose a region of interest

    while choice_region not in all_regions:      #while user's choice is not one of the available regions:
        choice_region = str(input('Please check for spelling of the region. Re-enter the region (Asia, Europe, Africa, Oceania or Americas): '))   #request user to re-enter region of interest

    list_available_countries = [x for x in dict_countries_to_regions.keys() if dict_countries_to_regions[x] == choice_region]   #creates a list of countries only in the region requested by user
    available_countries_lower = [country.lower() for country in list_available_countries]     #converts all country names in list to lower case
    print()   #line of space
    print(list_available_countries)   #displays all countries in the region chosen by user

    input1 = str(input('\nFor which country would you like to know the stats about?: ').lower())    #propmts user to choose a country out of the list displayed and converts input to lower case

    while input1 not in available_countries_lower:   #while user's choice is not one of the country's in the displayed list:
        input1 = str(input('\nPlease check for spelling, avoid abbrevations and ensure country is in the above list. Re-enter the country name or press 0 to choose a different region: ').lower())  #requests user to re-enter country name or re-choose the region
        if input1 == '0':  #if user enters 0:

            choice_region = str(input('\nPlease choose a region (Asia, Europe, Arica, Oceania or Americas: '))                            #user promted to choose a region of interest
            list_available_countries = [x for x in dict_countries_to_regions.keys() if dict_countries_to_regions[x] == choice_region]     #creates a list of countries only in the region requested by user
            available_countries_lower = [country.lower() for country in list_available_countries]                                         #converts all country names in list to lower case
            print()       #line of space
            print(list_available_countries)    #displays all countries in the region chosen by user

            input1 = str(input('\nFor which country would you like to know the stats about?: ').lower())   #propmts user to choose a country out of the list displayed and converts input to lower case

    print("\n***Requested Country Statistics***\n")        
    index = list_country_names.index((input1))         #finds index of country requested by user in the list of countries and stores under variable index
    country1 = Country(country_data[index, 0], country_data[index, 1], country_data[index, 2], country_data[index, 3], population_data[index, 21], (int(population_data[index,21]) - int(population_data[index,1])))   #creates an instance with attributes name, region, subregion, area, population and population change of the country requested by user
    country1.print_all_stats()         #calls an instance method to display all stats about the country requested by user
    country = country_data[index,0]    

    input2 = 1           #sets variable input2 equal to 1
    while input2 != 0:   #while input2 does not equal 0 the program is ran
        print(f'\nWould you like to know anything else about {input1.title()}? Please choose from the options below: ')   #displays possible options for user to pick
        print('Press 1 for the group of organisms with the greatest number of threatened species.')
        print('Press 2 to graph a population trend. ')
        print('Press 3 to know the average population.')
        print('Press 4 to graph threatened specie')
        print('Press 0 to exit')
        input2 = int(input('Please input a number: '))     #user prompted to choose an option from the menu
        
        if input2 == 1:                                    #if user inputs 1:
            most_threatened(index,threatened_species,country)   #calls funtion to display most threatened species in the country of user's choice
        elif input2 == 2:                                  #if user inputs 2:
            graph_population(index,population_data)        #calls function to graph the population of country of user's choice over years
        elif input2 == 3:                                  #if user inputs 3:
            average(index,population_data,country)         #calls function to calculate average population in country of user's choice from 2000 to 2020
        elif input2 == 4:                                  #if user inputs 4:
            graph_threatened(index,threatened_species)     #calls function to graph the number of threatened species in the country of user's choice
    print('Thank you for using stats progam.')             #displays thank you message
    
if __name__ == '__main__':
    main()