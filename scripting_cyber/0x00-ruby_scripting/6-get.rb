#!/usr/bin/env ruby

require 'net/http'
require 'json'

def get_request(url)
  uri = URI('http://example.com/index.html?count=10')
  response = Net::HTTP.get_response(uri)
  puts response
