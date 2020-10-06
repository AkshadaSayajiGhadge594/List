print("-----Demonstration of List-------");

batches=["PPA","LB","Angular","Python"]

print(batches);
print(batches[0]);
print(batches[1]);
print(batches[1:]);
print(batches[-1]);
print(batches[:3]);

#we can store heterogeneous Data
data1=[11,"Akshada",308]
print(data1);

data2=[21,"Priyanka",225]

#we can create list of List
combined=[data1,data2]

print(combined);

# There are multiple methods that we can use to manioulate list
batches.append("MEAN")
print(batches);

batches.insert(2,"LSP")
print(batches);

batches.remove("LSP")
print(batches);

batches.pop();
print(batches);

batches.pop(2);
print(batches);

batches.extend(["LB","Python","Angular",'MEAN']);
print(batches);

batches.sort()
print(batches);

