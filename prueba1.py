from twilio.twiml.voice_response import Gather, VoiceResponse, Say

response = VoiceResponse()
gather = Gather(input='speech dtmf', timeout=3, num_digits=1)
gather.say('Premi 1 per anar a on vulgui', voice='woman', language='ca-ES')
response.append(gather)

print(response)
file = open('prueba1.xml', 'w')
file.write(response.to_xml())

file.close()