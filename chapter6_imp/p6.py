def json_encode(data):
    """This function encodes a python module into a JSON encoded type 
        module """
    if isinstance(data, bool):
        if data:
            return "true"
        else:
            return "false"
    elif isinstance(data, (int, float)):
        return str(data)
    elif isinstance(data, str):
        return '"' + escape_string(data) + '"'
    elif isinstance(data, list):
        return "[" + ", ".join(json_encode(d) for d in data) + "]"
    elif isinstance(data, dict):
        return "{" + ", ".join((json_encode(i) + ' : ' + json_encode(j) for i,j in data.items())) +  "}"
    else:
        raise TypeError("%s is not JSON serializable" % repr(data))


def escape_string(s):
    """Escapes double-quote, tab and new line characters in a string."""
    s = s.replace('"', '\\"')
    s = s.replace("\t", "\\t")
    s = s.replace("\n", "\\n")
    return s

print json_encode(['gdf', 'rte', 'ktg', 'otu'])
print json_encode([1,2,3,5,6,3,46,3,369,23,14,63])
print json_encode({'gdf' : 78, 'rte' : 54, 'ktg' : 98, 'otu' : 210})
print json_encode({54 : 108, 98 : 196, 45 : 90, 100 : 200})
