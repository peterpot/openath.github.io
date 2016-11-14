from json import dumps
from types import StringTypes
from lxml import etree


"""

"""

def tag_to_dict(node):
    """Assume tag has one layer of children, each of which is text, e.g.

      <medalline>
        <rank>1</rank>
        <organization>USA</organization>
        <gold>13</gold>
        <silver>10</silver>
        <bronze>9</bronze>
        <total>32</total>
      </medalline>

    """

    d = {}
    for child in node:
        d[child.tag] = child.text
    return d




def simple_dict(node):
    "one layer of children, text content only"
    pass

def all_children_different(node):
    seen = set()
    for child in node:
        if child.tag in seen:
            return False
        seen.add(child.tag)
    return True

def all_children_same(node):
    first = node[0]
    for rest in node[1:]:
        if rest.tag != first.tag:
            return False
    return True


def node_to_json(node):
    "transform into a Python value, top down"

    childCount = len(node)
    # print node.tag, childCount
    if childCount == 0:  #no children
        return node.text#{node.tag: node.text}
    elif childCount == 1:
        if isinstance(node[0], StringTypes):
            return node[0].strip()
        return {node.tag: node_to_json(node[0])}
    else:
        if all_children_different(node):
            d = {}
            for child in node:
                d[child.tag] =  node_to_json(child)  
            return d

        elif all_children_same(node):
            return [node_to_json(x) for x in node]
        else:
            #make lists for any multi-valued ones
            d = {}
            for child in node:
                transformed = node_to_json(child)
                tag = child.tag
                # print tag
                if not d.has_key(tag):
                    d[tag] = transformed
                elif isinstance(d[tag], list):
                    d[tag].append(transformed)
                else: #not a list yet
                    d[tag] = [d[tag],transformed]
            return d



def xml_to_json(xml):
    root = etree.fromstring(xml)

    out = node_to_json(root)

    return dumps(out, indent=2)

if __name__=="__main__":
    fn_in = "rio_athletics_results.xml"
    fn_out = "rio_athletics_results.json"
    xml = open(fn_in).read()
    json = xml_to_json(xml)
    open(fn_out, "w").write(json)
    print "wrote", fn_out