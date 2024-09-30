import requests

# insert share link from website below 
share_link = "https://hansard.parliament.uk/commons/2015-05-28/debates/5463f0bf-0a1c-4c18-8f91-49cf0ce01cf4/CommonsChamber#contribution-15052828000532"

# splitting the share link based on the logic that there is integer after /CommonsChamber#contribution-

string_split = share_link.split("CommonsChamber#contribution-")

content_item_external_id = string_split[1]

find_debate_section_id_url = "https://hansard-api.parliament.uk/search/debatebyexternalid.json?contentItemExternalId={content_item_external_id}&house=Commons"

print(find_debate_section_id_url.format(content_item_external_id=content_item_external_id))