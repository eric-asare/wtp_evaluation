wtp_output = open('temp_wtp.txt', 'w')
unfiltered_file = open('/content/1399.txt')
unfiltered_input = unfiltered_file.read()
output = wtp.split(unfiltered_input)
pos = 0
ends = []
for sentences in output:
  ends += [(pos+len(sentences.rstrip()))]
  pos += len(sentences)
print(ends, file = wtp_output)
