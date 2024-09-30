import requests

# insert ####### share link from website 
# example https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber#contribution-15052828000532
share_link = "https://hansard.parliament.uk/Commons/2024-07-25/debates/7ED17C14-2C73-4EA7-B442-DE6E08BD66E3/CodeOfConductAndModernisationCommittee#contribution-DE998E9F-7E79-4110-97F7-0CDE6146E433"

# splitting the share link based on the logic that there is integer after /CommonsChamber#contribution-
string_split = share_link.split("#contribution-")

# getting second value out of a list of two 0,1
content_item_external_id = string_split[1]

# creating a variable which adds the string from above which is the external ID
find_debate_section_id_url = "https://hansard-api.parliament.uk/search/debatebyexternalid.json?contentItemExternalId={content_item_external_id}&house=Commons"

# formatting the variable with the externalid
ext_id_url = ((find_debate_section_id_url.format(content_item_external_id=content_item_external_id)))

# requesting the new URL
response = requests.get(ext_id_url)

# creating a variable with the response from the above request
DebateSectionExtId_data = response.json()

# use the response to get the DebateSectionExtId value

for item in DebateSectionExtId_data.get("Results", []):
    DebateSectionExtId = item.get("DebateSectionExtId")

# create URL that fetches the maiden speech content and the title of the speech

create_url = "https://hansard-api.parliament.uk/debates/debate/{DebateSectionExtId}.json"

url = ((create_url.format(DebateSectionExtId=DebateSectionExtId)))

# requesting the new URL
response_api = requests.get(url)

# creating a variable with the response from the above request
maiden_speech_data = response_api.json()

title = maiden_speech_data.get("Overview", [])


for item in maiden_speech_data.get("Items", []):
    if item.get("ExternalId") == content_item_external_id:   
        # open and create new file and print value of "Value:"
        f = open("maiden-speech.txt", "w")
        f.write(f"{item.get("Value")}")
        f.write("<h1>")
        f.write(f"{title.get("Title")}")
        f.write("</h1>")