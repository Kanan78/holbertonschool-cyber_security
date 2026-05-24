#!/usr/bin/env ruby
require 'open-uri'
require 'uri'
require 'fileutils'

def download_file(url, path)
  puts "Downloading file from #{url}..."
  URI.open(url) do |file|
    FileUtils.cp(file.path, path)
  end
  puts "File downloaded and saved to #{path}."
end

if ARGV.length < 2
  puts 'Usage: 9-download_file.rb URL LOCAL_FILE_PATH'
else
  download_file(ARGV[0], ARGV[1])
end
