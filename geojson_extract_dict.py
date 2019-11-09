"""
Daniel Bitters 2018

This script extracts data from a GeoJSON file using dictionaries.

Data that is extracted is:
    1)State name
    2)State FIPS code
    3)Area of state in integer square miles
    4)The following stats:
        -Longitude Min
        -Longitude Max
        -Latitude Min
        -Latitude Max

"""

def extract_state_data(filein):

    import json
    #filein="c:/VSProjects/states.json"
    indata=open(filein,'r')
    jsonstr=indata.read()
    geodict=json.loads(jsonstr)

    for x in range(0,len(geodict['features'])):
        #extract state properties
        state_name=(geodict['features'][x]['properties']['STATE_NAME'])
        state_fips=(geodict['features'][x]['properties']['STATE_FIPS'])
        state_area=(geodict['features'][x]['properties']['Area'])
 
        #extract coordinates
        coord_list= geodict['features'][x]['geometry']['coordinates']
        x_list=[]
        y_list=[]
        i=0
        for n in range(0,len(coord_list[0])):
            x_list.append(coord_list[0][i][0])
            y_list.append(coord_list[0][i][1])
            i=i+1      
        long_min=min(y_list)
        long_max=max(y_list)
        lat_min=min(x_list)
        lat_max=max(x_list)

        print("State name is: {0}".format(state_name))
        print("State fips is: {0}".format(state_fips))
        print("State area is: {0}".format(int(round(state_area))) ,"square miles")
        print("Longitude minimum is: {0}".format(long_min))
        print("Longitude maximum is: {0}".format(long_max))
        print("Latitude minimum is: {0}".format(lat_min))
        print("Longitude maximum is: {0}".format(lat_max))
        print("\n")

extract_state_data("c:/VSProjects/states.json")