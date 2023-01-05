import pandas as pd

import matplotlib.pyplot as plt

def GrowMap(data):
    '''This is the main function that is used to plot the geo-location dataset (consisting of longitudes and latittudes) on 
    the UK map. To do this, two sub-functions are required to process the data before plotting'''
    
    
    #First sub-function
    def col_rename(dataframe):
        '''This function is used to read the csv data, extract the longitude and latitude only.
        The names are swapped so this function also renames the variables'''
        #reading the csv file with pandas
        raw_data = pd.read_csv(dataframe)
        
        #extracting only longitudes and latitudes
        raw_data = raw_data[['Latitude','Longitude']]
        new_col_name= {'Longitude':'latitude', 'Latitude':'longitude'}
        
        #renaming the swapped variables or columns
        raw_data.rename(columns=new_col_name, inplace=True)
        return raw_data
    
    #second sub-function
    def data_filter(renamed_df):
        '''This function applies filters to the longitudes and latitudes based on some upper and lower limit rules
        to be able to eliminate all outliers'''
        #eliminating outliers below the lower limit
        lowerlimit = renamed_df.loc[(renamed_df['latitude']>=50.681) 
                          & (renamed_df['longitude']>=-10.592)]
        
        #eliminating outliers that exceed the upper limit
        final_data = lowerlimit.loc[(lowerlimit['latitude']<=57.985) 
                                    & (lowerlimit['longitude']<=1.6848)]
        return final_data


    #using the sub-functions to process the GeoLocations.csv file
    
    #reading the data and renaming columns using the first sub-function
    dataframe = col_rename(data)
    
    #applying lower and upper limit filter to clean the data using the second sub-function
    dataframe = data_filter(dataframe)


    #Plotting the cleaned data in the main function: GrowMap()
    
    #generating the x and y axis of the plot
    y_axis = dataframe['latitude']
    x_axis = dataframe['longitude']
    
    #creating a figure and axis for the plot in matplotlib
    figure, axis = plt.subplots()
    axis.set_title('A Plot of the Grow Map Data')
    axis.set_xlabel('Longitude')
    axis.set_ylabel('Latitude')
    
    #reading the UK map and setting it as the background for the plot
    growmap = plt.imread('resources/uk_map.png')
    axis.imshow(growmap, extent=(-10.5,1.8,50.6,57.8))
    
    #plotting the longitudes and latitudes on the map
    axis.scatter(x_axis,y_axis)
    
    #the final plot is saved in the working directory where the GrowMap.py is located
    figure.savefig('Denu_GrowMap.png')
    

#run this file to obtain the final plot, which will be saved
if __name__ == '__main__':
    file_name = 'resources/GrowLocations.csv'
    GrowMap(data=file_name)