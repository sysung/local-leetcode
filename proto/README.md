Resources
- https://protobuf.dev/getting-started/pythontutorial/
- https://protobuf.dev/programming-guides/proto3/
- https://www.youtube.com/watch?v=46O73On0gyI

# Problem Domain

Problems with serializing and retrieving structured data
- Python pickling is default, but can't deal with schema evolution and cross-language support (i.e. C++/Java)
- Custom encoding of data -> string is simple and flexible, but requires one-off encoding, parsing, and small runtime cost. Bad for complex data structures
- XML is good to share acorss applications, but is space intensive and XML DOM tree is complex

# Compile Protocol Buffers
- `protoc --python_out=.  addressbook.proto` to generate .py file
- `protoc --python_out=. --pyi_out=. addressbook.proto` to generate .pyi file

# Run scripts

Both of these scripts read from `addressbook.pb`. The file format can be .bin, .data, or .pb

- `python main_write_msg.py addressbook.pb`
- `python main_read_msg.py addressbook.pb`

# Pros and Cons

## Pros of Protobuf

- **Smaller payloads than JSON** because field names are replaced by numeric tags and values are encoded compactly.
- **Faster serialization/deserialization** in many cases because the format is binary and strongly defined.
- **Strong schema / contract** via .proto files, so producers and consumers agree on field names, types, and structure.
- **Language-neutral**: you define the schema once and generate code for multiple languages.
- **Good for internal services / high-throughput systems**, where bandwidth, CPU, latency, and consistency matter more than readability.
- **Supports schema evolution** when you follow compatibility rules, especially by keeping field numbers stable.

## Cons of Protobuf

- **Not human-readable**. Unlike JSON, you can’t just open the payload and immediately understand it.
- **Requires a schema**. You generally need the corresponding .proto definition to properly decode the message.
- **Adds tooling/code-generation overhead.** You need protoc, generated classes, build integration, and schema management.
- **Harder to debug manually.** JSON is easier to inspect with logs, curl, browser tools, Postman, etc.
- **Less convenient for public APIs. **JSON has much broader native support and is easier for external consumers.
- **Schema changes require discipline.** Reusing field numbers or making incompatible type changes can break consumers.