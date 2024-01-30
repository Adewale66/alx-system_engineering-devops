#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+?[a-zA-z0-9]+)\]\W+to:(\+?[a-zA-z0-9]+)\]\W+flags:([-0-9:]+)\]/).join(",")
