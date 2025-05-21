#DOM
import xml.dom.minidom
import datetime

#timing
start_time = datetime.datetime.now()

#start parsing
DOMTree = xml.dom.minidom.parse("go_obo.xml")
collection = DOMTree.documentElement
terms = collection.getElementsByTagName("term")

#dictionary to store the depth
max_depth = {
    "molecular_function": (None, 0),
    "biological_process": (None, 0),
    "cellular_component": (None, 0)
}

#check each terms and count the <is_a> number
for term in terms:
    ns_tag = term.getElementsByTagName("namespace")
    if ns_tag:
        namespace = ns_tag[0].firstChild.nodeValue
        is_a_tags = term.getElementsByTagName("is_a")
        is_a_count = len(is_a_tags)
        if namespace in max_depth:
            if is_a_count > max_depth[namespace][1]:
                name = term.getElementsByTagName("name")[0].firstChild.nodeValue
                max_depth[namespace] = (name, is_a_count)

end_time = datetime.datetime.now()
duration = end_time - start_time

#print the results and time
for ns, (term_name, count) in max_depth.items():
    print(f"{ns}:\n  GO Term: {term_name}\n  is_a count: {count}\n")

print("DOM time: ", duration)

#Slower

#SAX is faster than DOM in this task