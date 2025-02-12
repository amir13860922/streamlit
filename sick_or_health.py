problem = input("pill want for soul or body, nothing: ").lower().strip()


headc = "estaminofen", "more wather"

cold = "adult cold", "multi vitamin"

depres = "fluxtin", "love"

will = "i hope you to better feeling"

did = "your body is healthy"

if problem == "body":
  body = input("your problem head ache or cold: ").lower().strip()
  if body == "head ache":
    print(headc, will)
  elif body == "cold":
    print(cold, will)
      
  elif problem == "soul":
    print(depres, will)

elif problem == "nothing":
  print(did)

else:
    problem_2 = input("try again, please return program!")
  
