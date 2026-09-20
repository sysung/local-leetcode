Resources
- https://protobuf.dev/getting-started/pythontutorial/
- https://www.youtube.com/watch?v=46O73On0gyI

# Problem Domain

Problems with serializing and retrieving structured data
- Python pickling is default, but can't deal with schema evolution and cross-language support (i.e. C++/Java)
- Custom encoding of data -> string is simple and flexible, but requires one-off encoding, parsing, and small runtime cost. Bad for complex data structures
- XML is good to share acorss applications, but is space intensive and XML DOM tree is complex

# Compile Protocol Buffers
`protoc --python_out=.  addressbook.proto` to generate .py file
`protoc --python_out=. --pyi_out=. addressbook.proto` to generate .pyi file

# Run scripts

Both of these scripts read from `addressbook.pb`. The file format can be .bin, .data, or .pb

`python main_write_msg.py addressbook.pb`
`python main_read_msg.py addressbook.pb`