#!/usr/bin/env ruby
puts ARGV[0].scan(/from:(\+?[a-zA-z0-9]+)\] \Wto:(\+?[a-zA-z0-9]+)\] \Wflags:([-0-9:]+)\]/).join(",")
