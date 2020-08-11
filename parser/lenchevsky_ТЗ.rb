require 'open-uri'
require 'nokogiri'

url = 'https://www.petsonic.com/snacks-de-pollo-en-monodosis-para-perro.html')
html = open(url)

byebug

puts html.inspect