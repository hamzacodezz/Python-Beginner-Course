# dictionaries let you store info in key value pairs

monthConversions={
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    "Jul":"July",
    "Aug":"August",
    "Sep":"September",
    "Oct":"October",
    "Nov":"November",
    "Dec":"December",
}
#How to access Dictionary Enteries
#1
print(monthConversions["Nov"]) #Posts full name for Key

#2
print(monthConversions.get("Dec","Not a valid key"))#Posts second phrase if key not found