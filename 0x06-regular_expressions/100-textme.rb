#!/usr/bin/env ruby
def extract_infos(argument)
    sender = argument.match(/\[from:(.*?)\]/)[1]
    receiver = argument.match(/\[to:(.*?)\]/)[1]
    flags = argument.match(/\[flags:(.*?)\]/)[1]
  
    "#{sender},#{receiver},#{flags}"
  end
  
  if ARGV.length == 1
    argument = ARGV[0]
    result = extract_infos(argument)
    puts result
  else
    puts "Usage: #{$PROGRAM_NAME} 'logFile'"
  end