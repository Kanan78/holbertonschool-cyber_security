#!/usr/bin/env ruby

require 'digest'

def crack_password(hashed_password, dictionary_file)
  File.foreach(dictionary_file) do |word|
    word = word.chomp
    if Digest::SHA256.hexdigest(word) == hashed_password
      puts "Password found: #{word}"
      return
    end
  end
  puts 'Password was not found in dictionary.'
end

if ARGV.length < 2
  puts 'Usage: 10-password_cracked.rb HASHED_PASSWORD DICTIONARY_FILE'
else
  crack_password(ARGV[0], ARGV[1])
end
