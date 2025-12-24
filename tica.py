from tika import parser

parsed = parser.from_file("report.pdf")
print(parsed["content"])
