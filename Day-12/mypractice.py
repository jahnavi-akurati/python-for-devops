def update_server_config_connections(path,key,value):  #the funct take 3parametrs file path, key abd the value key here is max-conn
    with open(path,"r") as file:
        lines=file.readlines() #reading all the lines of the file one by one & storing in lines
    
    with open(path,"w") as update:
        for line in lines:   #taking each line from lines
            if key in line:   #comparing each line with the kwy i.e, max connections
                update.write(key + "=" + value + "\n")  #writing/updating the key and the value
            else:
                update.write(line) #leave as it is

#calling the function
update_server_config_connections("server.conf","MAX_CONNECTIONS","9000")