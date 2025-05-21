#SAX
import xml.sax
import datetime

#SAX handler
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.namespace = ""
        self.name = ""
        self.is_a_count = 0
        self.max_depth = {
            "molecular_function": ("", 0),
            "biological_process": ("", 0),
            "cellular_component": ("", 0)
        }

    def startElement(self, tag, attributes):
        self.current_data = tag
        if tag == "term":
            self.namespace = ""
            self.name = ""
            self.is_a_count = 0

    def characters(self, content):
        if self.current_data == "namespace":
            self.namespace += content.strip()
        elif self.current_data == "name":
            self.name += content.strip()
        elif self.current_data == "is_a":
            self.is_a_count += 1

    def endElement(self, tag):
        if tag == "term":
            if self.namespace in self.max_depth:
                if self.is_a_count > self.max_depth[self.namespace][1]:
                    self.max_depth[self.namespace] = (self.name, self.is_a_count)
        self.current_data = ""

#Run the parser
start_time = datetime.datetime.now()

parser = xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces, 0)
Handler = GOHandler()
parser.setContentHandler(Handler)
parser.parse("go_obo.xml")

end_time = datetime.datetime.now()
duration = end_time - start_time

#Print the result
for ns, (term_name, count) in Handler.max_depth.items():
    print(f"{ns}:\n  GO Term: {term_name}\n  is_a count: {count}\n")

print("SAX time: ", duration)

#Faster

#SAX is faster than DOM in this task