
# creating the xml for indesign
def write_xml_to_file(element: etree._Element, file_path: str | Path):

    element_tree = etree.ElementTree(element)
    element_tree.write(
        str(file_path), encoding='utf-8', xml_declaration=True
    )


# removing lines called in the next function to convert the json into xml
def normalize_xml_newlines(element: etree._Element) -> None:

    """
    Replace multiple consecutive newlines with a single newline
    in the XML element.
    """

    for element in element.iterdescendants():
        if element.text is not None:
            element.text = re.sub(r'\n+', '\n', element.text)
        if element.tail is not None:
            element.tail = re.sub(r'\n+', '\n', element.tail)




def convert_mps_contributions_to_xml():

    # convert the speech to xml
    output_element = etree.Element('root')

    for contribution in :
        # get the tag name (which will map to the style in InDesign)
        tag = contribution.get('HRSTag', 'hs_Para')
        contribution_text = contribution.get('Value', '')
        contribution_element = etree.fromstring(f'<{tag}>{contribution_text}</{tag}>')
        contribution_element.tail = '\n'  # add a newline after closing tag
        output_element.append(contribution_element)

    normalize_xml_newlines(output_element)

    return output_element
