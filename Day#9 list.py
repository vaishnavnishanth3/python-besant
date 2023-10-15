#1)List:
print("")
print("1) List: ")
nums=["integers","decimals","duplicates","realnumbers",26,15,35,86] 
print(type(nums)) 
print(nums)
#squarebrackets,multipleitems,ordered,duplicates

#2)Indexing in list:

print("")
print("2) Indexing in list: ")
print(nums[2])
print(nums[1:3])

#3)Changing an item in a list to other element:

print("")
print("3) Changing value or item: ") 
nums[2]="nonduplicates"
print(nums)
print("")

#4)append() to add a single item on the end (Default):
print("4) Append(): ")
nums.append(6)
print(nums)
print("")

#5)Insert() to add an item between other two:
print("5) Insert(): ")
nums.insert(1,"greater")
nums.insert(2,"civil")
print(nums)
print("")

#6)Remove() is used to remove the specified elements in the list:
print("6) Remove(): ")
nums.remove("civil")
print(nums)

#7a)pop(n) [pop method] - Remove using Index.
print("")
print("7):")
print("a) pop(i): ")
nums.pop(3)
print(nums)
print("")

#7b)pop() [empty pop] displays the last item.
print("b) Empty pop: ")
nums.pop()
print(nums)
print("")

#8)Clear() - Clear all the items/values of list.
print("8) Clear(): ")
nums.clear()
print(nums)
print("")

#9)Count() - to count no.of.repeated values
nums1=["integers","decimals","duplicates","realnumbers",26,15,35,86]
print("9) Count(): ")
a=nums1.count("integers")
print(a)
print("")

#10)Len() - to count total no. of. item/values in list
print("10) Len:")
y=len(nums1)
print(y)
print("")

#11)reverse() - to reverse the order.
print("11) Reverse(): ")
nums2=["Digital, Real, Imaginary, Decimal"]
nums2.reverse()
print(nums2)
print("")

#12)sort()-to arrange in an order.
print("12a) Sort(): ")
nums3=[2,4,7,5,53,43,54,24,86,2,676,9,63]
nums3.sort()
print(nums3)

#12b)decending order:
print("")
print("12b) Descending sort: ")
nums3.sort(reverse=True)
print(nums3)