from googletrans  import  Translator

#1. 번역기 만들기
translator  =  Translator()

#2. 번역을 원하는 문장 설정
sentence =  input("번역을 원하는 문장을 입력해주세요 : ")
detected = translator.detect(sentence)

#3.  번역을 원하는 언어 설정
lang  =  input("어떤 언어로  번역을 원하시나요? : ")
result = translator.translate(sentence, lang)

#4.  번역하기
print("===========출 력 결 과===========")
print(detected.lang,  ":",  sentence)
print(result.dest,  ":",  result.text)
print("=================================")