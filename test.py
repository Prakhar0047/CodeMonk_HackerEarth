def longestEvenWord(s):
  ll = s.split()
  lon = ""
  for x in ll:
    if len(x)%2==0 and len(x) > len(lon):
      lon = x
  return lon

sentence = 'Time to write great code'
ans = longestEvenWord(sentence)
print(ans)