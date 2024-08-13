def update_server_config(path,updates):
    file=open(path,"r")
    data=file.readlines()

    with open(path,"w") as new_data:
        for line in data:
            var=False
            for key, value in updates.items():
                 if line.startswith(key):
                     new_data.write(f"{key} = {value}\n")
                     var=True
                     break
            if not var:
                new_data.write(line)

settings_to_update = {
     "PORT": "465",     # New value for PORT
     "TIMEOUT": "62"    # New value for TIMEOUT
 }

update_server_config("server.conf",settings_to_update)

# def update_server_config(path, updates):
#     # Open the file in read mode
#     with open(path, "r") as file:
#         data = file.readlines()

#     # Open the file in write mode
#     with open(path, "w") as new_data:
#         for line in data:
#             var = False
#             for key, value in updates.items():
#                 if line.startswith(key):
#                     new_data.write(f"{key}={value}\n")  # Corrected from 'file.write' to 'new_data.write'
#                     var = True
#                     break
#             if not var:  # Write the line if no updates were applied
#                 new_data.write(line)

# # Dictionary of settings to update
# settings_to_update = {
#     "PORT": "465",     # New value for PORT
#     "TIMEOUT": "60"    # New value for TIMEOUT
# }

# # Call the function with the correct dictionary
# update_server_config("server.conf", settings_to_update)


        