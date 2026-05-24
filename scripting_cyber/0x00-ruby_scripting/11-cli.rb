#!/usr/bin/env ruby
require 'optparse'

TASKS_FILE = 'tasks.txt'

def add_task(task)
  File.open(TASKS_FILE, 'a') do |file|
    file.puts(task)
  end
  puts "Task '#{task}' added."
end

def list_tasks
  return puts 'No tasks found.' unless File.exist?(TASKS_FILE)

  tasks = File.readlines(TASKS_FILE, chomp: true)
  tasks.each_with_index do |task, index|
    puts "#{index + 1}. #{task}"
  end
end

def remove_task(index)
  return puts 'No tasks found.' unless File.exist?(TASKS_FILE)

  tasks = File.readlines(TASKS_FILE, chomp: true)
  idx = index.to_i - 1

  if idx < 0 || idx >= tasks.length
    puts 'Invalid index.'
    return
  end

  removed = tasks.delete_at(idx)
  File.write(TASKS_FILE, tasks.join("\n") + "\n")
  puts "Task '#{removed}' removed."
end

options = {}

parser = OptionParser.new do |opts|
  opts.banner = 'Usage: cli.rb [options]'

  opts.on('-a', '--add TASK', 'Add a new task') do |task|
    options[:add] = task
  end

  opts.on('-l', '--list', 'List all tasks') do
    options[:list] = true
  end

  opts.on('-r', '--remove INDEX', 'Remove a task by index') do |index|
    options[:remove] = index
  end

  opts.on('-h', '--help', 'Show help') do
    puts opts
    exit
  end
end

parser.parse!

add_task(options[:add]) if options[:add]
list_tasks if options[:list]
remove_task(options[:remove]) if options[:remove]
