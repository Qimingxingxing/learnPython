hashMap = {}
hashMapInit = {
    "qiming" : 1,
    "yiming" : 2
}
# del hashMapInit["qiming"]
print(hashMapInit["qiming"])
print("qiming" in hashMapInit)
print(hashMapInit.get("qimig"))
print(hashMapInit.get("qimin",-1))
print(hashMapInit.pop("qiming"))
hashMap[0] = "qing"
hashMap[1] = "xixi"
hashMap[2] = "helo"
hashMap.update(red = 1, green = 2)
print(hashMap.items())
print(hashMap.keys())
print(hashMap.values())
for key, item in hashMap.items():
    print(key, item)
