independence_stages = ["Inicio", "Organización", "Resistencia", "Consumación"]
print(independence_stages[0])
print(len(independence_stages))

#List Methods 
leaders = []
leaders.append("Miguel Hidalgo")
leaders.append("Vicente Guerrero")
#leaders.extend(independence_stages) //mixed list togehther
leaders.insert(1, "Jose Maria Morelos")
#leaders.remove("Vicente Guerrero") //remove specific information
leaders.append("Agustin de Ituurbide")
#leaders.pop(1) //delete an index
#leaders.clear()//remove everything form the list
print(leaders.index("Miguel Hidalgo"))
print(leaders.count("Vicente Guerrero"))
#leaders.sort()     
#leaders.reverse()
new_leaders = leaders.copy()



print(leaders)
print(new_leaders)