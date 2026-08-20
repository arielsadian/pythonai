smokers = {"John Smith","Maya Levi","Noam Cohen","Liam Patel"}
ride_bikes = {"Maya Levi","Omer Halevi","Liam Patel"}
ride_motorcycles = {"John Smith","Noam Cohen","Rina Gold"}
likes_skyjump = {"John Smith","Rina Gold","Dina Bar"}
suspects = smokers |ride_bikes |ride_motorcycles | likes_skyjump
print(f"Suspects:  {suspects}\n")
print("clues:")
print("1) the suspect SMOKES")
print("2)the suspect likes SKYDIVING")
print("3)the suspect rides a bike or a MOTORCYCLES")
guilty = smokers & likes_skyjump & (ride_bikes |ride_motorcycles)
print(guilty)

#targil 2
smokers = {"Avi Ron","Sara Kim","Ben Azulay","Nina Fox"}
ride_bikes = {"Sara Kim","Tom Green","Nina Fox"}
ride_motorcycles = {"Avi Ron", "Ben Azulay","Nina Fox", "Eli Stone"}
likes_skyjump ={"Avi Ron","Nina Fox", "Dana Wolf"}
suspects = smokers |ride_bikes |ride_motorcycles | likes_skyjump
print(f"Suspects:  {suspects}\n")
print("clues:")
print("1)the suspect rides a BIKE or a MOTORCYCLES")
print("2)the suspect smokes")
print("3)the suspect likes SKYDIVING")
print("4)the suspect is NOT someone who rides BOTH bike AND motorcycles")
guilty = (ride_bikes | ride_motorcycles) &smokers & likes_skyjump - (ride_bikes &ride_motorcycles)
print(guilty)
# targil 3
night_shift = {"Alex","Jordan","Taylor","Casey"}
access_server_room = {"Jordan","Casey","Morgan","Riley"}
hardware_expert = {"Taylor","Riley","Casey","Alex"}
management_role = {"Jordan","Morgan"}
print("1) the suspect was on the NIGHT SHIFT.")
print("2) the suspect has access to the SERVER ROOM.")
print("3) the suspect is a HAEDWARE EXPERT.")
print("4) the suspect is NOT in a MANAGEMENT ROLE.")
guilty = night_shift & access_server_room & hardware_expert -management_role
print(len(guilty))
print(guilty <= night_shift)